import json

import falcon
from config.connection import engine
from model.time_aluno import TimeAluno
from sqlalchemy.orm import sessionmaker
from util.util import new_alchemy_encoder


class TimeAlunoResources:
    def on_get(self, req, resp):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            output = {'TimeAluno': session.query(TimeAluno).all()}

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
