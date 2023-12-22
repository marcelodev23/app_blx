from sqlalchemy.orm import Session
from sqlalchemy import select,delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    def __init__(self, db:Session):
        self.db = db
    
    def criar(self,produto:schemas.Produto):
        db_produto = models.Produto(nome  = produto.nome,
                                    preco = produto.preco,
                                    detalhes   = produto.detalhes,
                                    disponivel = produto.disponivel
                                    )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        produtos= self.db.query(models.Produto).all()
        return produtos
    
    def obter(self,idProduto:int):
       return self.db.execute(select(models.Produto).filter_by(id=idProduto)).one_or_none()
    
    def remover(self,idProduto:int):
        self.db.execute(delete(models.Produto).where(models.Produto.id==idProduto))
        self.db.commit()
