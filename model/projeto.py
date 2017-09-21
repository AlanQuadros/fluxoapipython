from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Projeto(Base):
    __tablename__ = 'tb_projeto'

    id_projeto = Column(Integer, primary_key=True)
    nome_projeto = Column(String, nullable=False)
    status_projeto = Column(String, nullable=False)
    workspace = Column(String, nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime)
    data_fim_previsto = Column(DateTime, nullable=False)
    data_inclusao = Column(DateTime, nullable=False)

    def __init__(self, nome_projeto, status_projeto,
                 workspace, data_inicio, data_fim, data_fim_previsto, data_inclusao):
        self.nome_projeto = nome_projeto
        self.status_projeto = status_projeto
        self.workspace = workspace
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.data_fim_previsto = data_fim_previsto
        self.data_inclusao = data_inclusao

    def __repr__(self):
        return "<Projeto(%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.id_projeto,
                                                       self.nome_projeto,
                                                       self.status_projeto,
                                                       self.workspace,
                                                       self.data_inicio,
                                                       self.data_fim,
                                                       self.data_fim_previsto,
                                                       self.data_inclusao)