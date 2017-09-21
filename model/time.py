from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Time(Base):
    __tablename__ = 'tb_time'

    id_time = Column(Integer, primary_key=True)
    id_orientador = Column(Integer, ForeignKey('tb_usuario'))
    id_projeto = Column(Integer, ForeignKey('tb_projeto'))
    semestre = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)
    status_time = Column(String, nullable=False)
    dt_inclusao = Column(DateTime, nullable=False)
    primeiro_dia = Column(Date, nullable=False)

    def __init__(self, id_orientador, id_projeto, semestre, ano,
                 status_time, dt_inclusao, primeiro_dia):
        self.id_orientador = id_orientador
        self.id_projeto = id_projeto
        self.semestre = semestre
        self.ano = ano
        self.status_time = status_time
        self.dt_inclusao = dt_inclusao
        self.primeiro_dia = primeiro_dia

    def __repr__(self):
        return "<Time(%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.id_time,
                                                    self.id_orientador,
                                                    self.id_projeto,
                                                    self.semestre,
                                                    self.ano,
                                                    self.status_time,
                                                    self.dt_inclusao,
                                                    self.primeiro_dia)
