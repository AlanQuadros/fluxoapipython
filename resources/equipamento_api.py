import json

import falcon
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from config.connection import engine
from model.equipamento import Equipamento
from util.util import new_alchemy_encoder

class EquipamentoResource:
    def on_get(self, req, resp):    
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            param_id = req.get_param("id")
            param_cod = req.get_param("codigo")
            param_numero = req.get_param("numero")

            if param_id:
                output = {'Equipamentos':
                              session.query(Equipamento)
                                  .filter(and_(Equipamento.id_equipamento==param_id, Equipamento.status=='ATIVO'))
                                  .all()}
            elif param_cod:
                output = {'Equipamentos':
                              session.query(Equipamento)
                                  .filter(and_(Equipamento.codigo==param_cod, Equipamento.status=='ATIVO'))
                                  .all()}
            elif param_numero:
                output = {'Equipamentos':
                              session.query(Equipamento)
                                  .filter(and_(Equipamento.numero==param_numero, Equipamento.status=='ATIVO'))
                                  .all()}
            else:
                output = {'Equipamentos':
                              session
                                  .query(Equipamento)
                                  .filter(Equipamento.status=='ATIVO')
                                  .all()}

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output, cls=new_alchemy_encoder(), check_circular=False, encoding='ISO-8859-1')    
            session.close()

        except Exception as e:
            resp.body = json.dumps({'error ':str(e)})
            resp.status = falcon.HTTP_500
            return resp
        