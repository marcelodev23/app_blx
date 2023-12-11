from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():
    def __init__(self ,db:Session) :
        self.db= db
        
    def criar(self,usuario:schemas.User):
        usuario_db = models.Usuario(nome= usuario.nome,telefone= usuario.telefone)
        self.db.add(usuario_db)
        self.db.commit(usuario_db)
        self.db.refresh(usuario_db)
        return usuario_db
    
    def get(self):
        return self.db.query(models.Usuario).all()