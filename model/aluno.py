from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Aluno(Base):
    __tablename__ = 'tb_usuario'

    id_usuario = Column(Integer, primary_key=True)
    usuario = Column(String(45), nullable=False)
    status_usuario = Column(String(20), nullable=False)
    id_tipo_usuario = Column(Integer, ForeignKey('tb_tipo_usuario.id_tipo_usuario'))
    matricula = Column(String(45), nullable=False)
    nome = Column(String(80))
    email = Column(String(120))

    def __init__(self, usuario, status_usuario, id_tipo_usuario, matricula, nome, email):
        self.usuario = usuario
        self.status_usuario = status_usuario
        self.id_tipo_usuario = id_tipo_usuario
        self.matricula = matricula
        self.nome = nome
        self.email = email

    def __repr__(self):
        return "<Aluno(%s,%s,%s,%s,%s,%s,%s)>" % (self.id_usuario,
                                                  self.usuario,
                                                  self.status_usuario,
                                                  self.id_tipo_usuario,
                                                  self.matricula,
                                                  self.nome,
                                                  self.email)
    