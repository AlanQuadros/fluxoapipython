from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TimeAluno(Base):
    __tablename__ = 'tb_time_aluno'

    id_time = Column(Integer, ForeignKey('tb_time'), primary_key=True)
    id_aluno = Column(Integer, ForeignKey('tb_usuario'), primary_key=True)
    matricula = Column(String, ForeignKey('tb_usuario'), primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<TimeAluno(%s,%s,%s)>' % (self.id_time, self.id_aluno, self.matricula)
