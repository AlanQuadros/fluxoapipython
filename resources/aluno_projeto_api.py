import json

import falcon
from config.connection import engine
from model.time import Time
from model.projeto import Projeto
from model.aluno import Aluno
from model.time_aluno import TimeAluno
from sqlalchemy.orm import sessionmaker
from util.util import new_alchemy_encoder

class AlunoProjetoResources:
    def on_get(self, req, resp):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()

            param_id_aluno = req.get_param('id_aluno')

            if param_id_aluno:
                output_array = (session
                               .query(Aluno.id_usuario, Aluno.nome, Aluno.matricula, Projeto.nome_projeto)
                               .join(TimeAluno, Aluno.id_usuario == TimeAluno.id_aluno)
                               .join(Time, TimeAluno.id_time == Time.id_time)
                               .join(Projeto, Time.id_projeto == Projeto.id_projeto)
                               .filter(Aluno.id_usuario == param_id_aluno)
                               .first()
                               )
                output = {'AlunoProjeto': []}
                output['AlunoProjeto'].append(output_array._asdict())
            else:
                output_array = (session
                               .query(Aluno.id_usuario, Aluno.nome, Aluno.matricula, Projeto.nome_projeto)
                               .join(TimeAluno, Aluno.id_usuario == TimeAluno.id_aluno)
                               .join(Time, TimeAluno.id_time == Time.id_time)
                               .join(Projeto, Time.id_projeto == Projeto.id_projeto)
                               .all()
                               )
                output = {'AlunoProjeto': []}
                for out in output_array:
                    output['AlunoProjeto'].append(out._asdict())

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
