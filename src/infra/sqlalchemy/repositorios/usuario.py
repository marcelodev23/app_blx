from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select,delete

class RepositorioUsuario():
    def __init__(self ,db:Session) :
        self.db= db
        
    def setCreate(self,usuario:schemas.User):
        usuario_db = models.Usuario(nome= usuario.nome,telefone= usuario.telefone,senha=usuario.senha)
        self.db.add(usuario_db)
        self.db.commit()
        self.db.refresh(usuario_db)
        return usuario_db
    
    def getAll(self):
        #return self.db.query(models.Usuario).all()
        return self.db.execute(select(models.Usuario)).all()
    
    def getById(self,idUser:int):
        return self.db.execute(select(models.Usuario).filter_by(id=idUser)).first()
    
    def setDelete(self,idUser:int):
        self.db.execute(delete(models.Usuario).where(models.Usuario.id == idUser))
        self.db.commit()
        
      
    