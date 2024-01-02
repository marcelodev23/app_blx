from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select,delete
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status

class RepositorioUsuario():
    def __init__(self ,db:Session) :
        self.db= db
        
    def setCreate(self,usuario:schemas.User):
        usuario_db = models.Usuario(nome= usuario.nome,telefone= usuario.telefone,senha=usuario.senha)
        try:
            self.db.add(usuario_db)
            self.db.commit()
            self.db.refresh(usuario_db)
            return usuario_db
        except IntegrityError as erro:
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'{str(erro)}'
            )
    
    
    def getByTelefone(self,telefone:str) -> models.Usuario :
        return self.db.execute(select(models.Usuario).where(models.Usuario.telefone==telefone)).scalars().first()
    
    def setDelete(self,idUser:int):
        self.db.execute(delete(models.Usuario).where(models.Usuario.id == idUser))
        self.db.commit()
        
      
    