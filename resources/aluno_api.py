import json

import falcon
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from config.connection import engine
from model.aluno import Aluno
from util.util import new_alchemy_encoder


class AlunoResource:
    def on_get(self, req, resp):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            param_id = req.get_param("id")
            param_mat = req.get_param("matricula")

            if param_id:
                output = {'Alunos': session.query(Aluno)
                    .filter(and_(Aluno.id_tipo_usuario == 2, Aluno.id_usuario == param_id))
                    .all()}
            elif param_mat:
                output = {'Alunos': session.query(Aluno)
                    .filter(and_(Aluno.id_tipo_usuario==2, Aluno.matricula==param_mat))
                    .all()}
            else:
                output = {'Alunos': session.query(Aluno)
                    .filter(and_(Aluno.id_tipo_usuario==2))
                    .all()}

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output, cls=new_alchemy_encoder(), check_circular=False, encoding='ISO-8859-1')
            session.close()

        except Exception as e:
            resp.body = json.dumps({'error ':str(e)})
            resp.status = falcon.HTTP_500
            return resp
