from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)
    produtos = relationship('Produto',back_populates='user')
 
class Produto(Base):
    __tablename__  = "produto"
    id = Column(Integer,primary_key=True,index=True )
    nome = Column(String)
    detalhes = Column(String)
    disponivel = Column(Boolean)
    preco=Column(Float)
    user_id = Column(Integer,ForeignKey('usuario.id'))
    user = relationship('Usuario',back_populates='produtos')


