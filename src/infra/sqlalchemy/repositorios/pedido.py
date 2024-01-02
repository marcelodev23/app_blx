from sqlalchemy.orm import Session
from sqlalchemy import select,delete,update
from fastapi import HTTPException,status
from src.infra.sqlalchemy.models.models import Pedido as pedido_models
from src.infra.sqlalchemy.models.models import Produto as produto_models
from src.schemas import schemas

class RepositorioPidido():
    def __init__(self,db:Session):
        self.db = db
    
    def setCreate(self,pedido:schemas.Pedido):
        db_pedido = pedido_models(**pedido.model_dump())
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)
        return db_pedido
    
    def getAll(self):
        return self.db.execute(select(pedido_models)).scalars().all()
    
    def getById(self,id):
        return self.db.execute(select(pedido_models).where(pedido_models.id ==id)).scalars().first()
    
    def setUpdate(self,id:int,pedido:schemas.Pedido):
        update_stml = update(select(pedido_models).where(pedido_models.id == id)).values(**pedido.model_dump())
        self.db.execute(update_stml)
        self.db.commit()
    
    def SetDelete(self,id:int):
        self.db.execute(delete(pedido_models).where(pedido_models.id == id))
        self.db.commit()

    def SetMeusPedidosByIdUser(self,idUser:int):
        return self.db.execute(select(pedido_models).where(pedido_models.usuario_id == idUser)).scalars().all()
    
    def SetMinhaVendasByIdUser(self,idUser:int):
        query = select(pedido_models).join_from(pedido_models,produto_models).where(produto_models.user_id==idUser)
        resultado = self.db.execute(query).scalars().all()
        return resultado