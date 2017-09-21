import json
import falcon
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from config.connection import engine
from model.emprestimo import Emprestimo
from util.util import new_alchemy_encoder

class EmprestimoResource:
    def on_get(self, req, resp):    
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            param_id = req.get_param("id")
            param_id_aluno = req.get_param("id_usuario")
            param_id_equipamento = req.get_param("id_equipamento")

            if param_id:
                output = {'Emprestimos': session.query(Emprestimo)
                .filter_by(id_equip_aluno=param_id)
                .all()}
            elif param_id_aluno:
                output = {'Emprestimos': session.query(Emprestimo)
                .filter(and_(Emprestimo.data_entrega == None, Emprestimo.id_usuario==param_id_aluno))
                .all()}
            elif param_id_equipamento:
                output = {'Emprestimos': session.query(Emprestimo)
                .filter(and_(Emprestimo.data_entrega == None, Emprestimo.id_equipamento==param_id_equipamento))
                .all()}
            else:
                output = {'Emprestimos': session.query(Emprestimo).all()}        

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output, cls=new_alchemy_encoder(), check_circular=False, encoding='ISO-8859-1')    
            session.close()

        except Exception as e:
            resp.body = json.dumps({'error ':str(e)})
            resp.status = falcon.HTTP_500
            return resp
        
    def on_post(self, req, resp):
        session = None
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            raw_json = req.stream.read()
            data = json.loads(raw_json, encoding='utf-8')

            equip_em_uso =  (session.query(Emprestimo)
            .filter(and_(Emprestimo.data_entrega == None, Emprestimo.id_equipamento == data['id_equipamento']))
            .count())

            if equip_em_uso:
                session.rollback()
                resp.body = json.dumps({'error':'Equipamento ja emprestado'})
                resp.status = falcon.HTTP_401
                return resp

            query = Emprestimo(data['id_equipamento'], data['id_usuario'], datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            session.add(query)
            session.commit()            

            output = {
            	'status': "Emprestimo cadastrado com sucesso!"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp
            session.close()
        except Exception as e:
            session.rollback()
            resp.body = json.dumps({'error':str(e)})
            resp.status = falcon.HTTP_500
            return resp

    def on_put(self, req, resp):
        session = None
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            raw_json = req.stream.read()
            data = json.loads(raw_json, encoding='utf-8')

            emprestimo = (session.query(Emprestimo)
                .filter(and_(Emprestimo.data_entrega == None, Emprestimo.id_usuario == data['id_usuario']))
                .first())

            emprestimo.observacao = data['observacao']
            emprestimo.data_entrega = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            session.commit()		    
            output = {
            	'status': "Emprestimo terminado com sucesso!"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp
            session.close()
    
        except Exception as e:
            session.rollback()
            resp.body = json.dumps({'error':str(e)})
            resp.status = falcon.HTTP_500
            return resp
        