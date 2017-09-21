from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from equipamento import Equipamento
from aluno import Aluno

Base = declarative_base()
class Emprestimo(Base):
    __tablename__ = 'tb_equipamento_aluno'

    id_equip_aluno = Column(Integer, primary_key=True)
    id_equipamento = Column(Integer, ForeignKey(Equipamento.id_equipamento))
    id_usuario = Column(Integer, ForeignKey(Aluno.id_usuario))
    observacao = Column(String(255))
    data_retirada = Column(DateTime)
    data_entrega = Column(DateTime)

    def __init__(self, id_equipamento, id_usuario, data_retirada):
        self.id_equipamento = id_equipamento
        self.id_usuario = id_usuario
        self.data_retirada = data_retirada

    def __repr__(self):
        return "<Emprestimo(%s,%s,%s,%s,%s,%s)>" % (self.id_equip_aluno,
                                                    self.id_equipamento,
                                                    self.id_usuario,
                                                    self.observacao,
                                                    self.data_retirada,
                                                    self.data_entrega)
    