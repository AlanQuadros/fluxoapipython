from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model.aluno import Aluno

Base = declarative_base()
class Ponto(Base):
    __tablename__ = 'tb_ponto'

    id_ponto = Column(Integer, primary_key=True)
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date, nullable=False)
    id_usuario_aluno = Column(Integer)
    id_usuario_responsavel = Column(Integer)
    status_ponto = Column(String, nullable=False)

    def __init__(self, data_entrada, data_saida, id_usuario_aluno, status_ponto):
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.id_usuario_aluno = id_usuario_aluno
        self.status_ponto = status_ponto

    def __repr__(self):
        return "<Ponto(%s,%s,%s,%s,%s,%s)>" % (self.id_ponto,
                                               self.data_entrada,
                                               self.data_saida,
                                               self.id_usuario_aluno,
                                               self.id_usuario_responsavel,
                                               self.status_ponto)