from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from src.infra.sqlalchemy.config.database import Base



class Produto(Base):
    __tablename__  = "produto"
    id = Column(Integer,primary_key=True,index=True )
    nome = Column(String)
    detalhes = Column(String)
    disponivel = Column(Boolean)
    preco=Column(Float)