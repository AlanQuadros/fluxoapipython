from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

Base = declarative_base()
class Equipamento(Base):
    __tablename__ = 'tb_equipamento'

    id_equipamento = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    numero = Column(Integer, nullable=False)
    codigo = Column(String(100), nullable=False)
    descricao = Column(String(255))
    data_movimentacao = Column(Date, nullable=False)
    id_tipo_equipamento = Column(Integer, ForeignKey('tb_tipo_equipamento.id_tipo_equipamento'))
    status = Column(String(15))

    def __init__(self, nome, numero, codigo, descricao, data_movimentacao, id_tipo_equipamento,status):
        self.nome = nome
        self.numero = numero
        self.codigo = codigo
        self.descricao = descricao
        self.data_movimentacao = data_movimentacao
        self.id_tipo_equipamento = id_tipo_equipamento
        self.status = status

    def __repr__(self):
        return "<Equipamento(%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.id_equipamento,
                                                           self.nome,
                                                           self.numero,
                                                           self.codigo,
                                                           self.descricao,
                                                           self.data_movimentacao,
                                                           self.id_tipo_equipamento,
                                                           self.status)
    