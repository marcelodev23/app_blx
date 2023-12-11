from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db,criar_bd,engine
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.models import models
app = FastAPI()
#criar_bd()

#models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"Msg":"Ok Porra"}


@app.post('/produtos',status_code=status.HTTP_201_CREATED)
async def criar_poduto(produto: Produto,db:Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
async def lista_produtos(db:Session = Depends(get_db)):
    return RepositorioProduto(db).listar()

@app.get('/protuto/{id}')
async def getIdProduto(id:int,db:Session=Depends(get_db)):
    get =RepositorioProduto(db).obter(id)
    return get

@app.post('/user')
async def setUser(db:Session = Depends(get_db)):
    user = RepositorioUsuario(db)
    return user 

@app.get('/user')
async def getUser(db:Session = Depends(get_db)):
    return RepositorioUsuario(db).get()