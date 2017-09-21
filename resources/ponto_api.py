import json

import falcon
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from config.connection import engine
from model.ponto import Ponto
from util.util import new_alchemy_encoder
from datetime import datetime

class PontoResources:
    # Parametros da URL
    # id_aluno -> lista os pontos que ainda nao tiveram saida do aluno
    # id -> lista todos os pontos do aluno do mais atual para o mais antigo
    def on_get(self, req, resp):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            param_id_aluno = req.get_param("id_aluno")
            param_id = req.get_param("id")

            if param_id:
                output = {'Pontos':
                              session
                                  .query(Ponto)
                                  .filter(and_(Ponto.status_ponto == 'VALIDO', Ponto.id_usuario_aluno == param_id))
                                  .order_by(Ponto.id_ponto.desc())
                                  .all()}
            elif param_id_aluno:
                output = {'Pontos':
                              session
                                  .query(Ponto)
                                  .filter(and_(Ponto.data_saida == None, Ponto.id_usuario_aluno == param_id_aluno))
                                  .all()}
            else:
                output = {'Pontos': session.query(Ponto).all()}

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output,
                                   cls=new_alchemy_encoder(),
                                   check_circular=False,
                                   encoding='ISO-8859-1')
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

            aluno_hora_aberto = (session.query(Ponto)
                 .filter(and_(
                    Ponto.data_saida == None, Ponto.id_usuario_aluno == data['id_usuario_aluno']))
                 .count())

            if aluno_hora_aberto:
                session.rollback()
                resp.body = json.dumps({'error': 'Aluno com Ponto em aberto.'})
                resp.status = falcon.HTTP_401
                return resp

            query = Ponto(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                None,
                data['id_usuario_aluno'],
                "VALIDO"
            )

            session.add(query)
            session.commit()

            output = {
                'status': "Ponto cadastrado com sucesso!"
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

            ponto = (session.query(Ponto)
                          .filter(and_(Ponto.data_saida == None, Ponto.id_usuario_aluno == data['id_usuario_aluno']))
                          .first())

            ponto.data_saida = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            session.commit()
            output = {
                'status': "Ponto encerrado com sucesso!"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp
            session.close()

        except Exception as e:
            session.rollback()
            resp.body = json.dumps({'error': str(e)})
            resp.status = falcon.HTTP_500
            return resp
