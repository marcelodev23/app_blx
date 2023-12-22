from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List,Dict
from src.schemas.schemas import Produto,ProdutoOut,User
from src.infra.sqlalchemy.config.database import get_db,criar_bd,engine
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.models import models
app = FastAPI()
#criar_bd()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"Msg":"Ok Porra"}


@app.post('/produtos',status_code=status.HTTP_201_CREATED,response_model=ProdutoOut)
async def criar_poduto(produto: Produto,db:Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos',status_code=status.HTTP_200_OK,response_model=List[ProdutoOut])
async def lista_produtos(db:Session = Depends(get_db)):
    return RepositorioProduto(db).listar()

@app.get('/protuto/{id}',status_code=status.HTTP_200_OK)
async def getIdProduto(id:int,db:Session=Depends(get_db)):
    get =RepositorioProduto(db).obter(id)
    #if get is None:
    #    raise HTTPException(status_code=404, detail="protuto not found")
    return get

@app.post('/user',status_code=status.HTTP_201_CREATED)
async def setUser(usuario:User,db:Session = Depends(get_db)):
    user = RepositorioUsuario(db).setCreate(usuario)
    return user 

@app.get('/user',status_code=status.HTTP_200_OK)
async def getUser(db:Session = Depends(get_db)):
    return RepositorioUsuario(db).getAll()

@app.get('/user/{idUser}',status_code=status.HTTP_200_OK)
async def getUserId(idUser,db:Session = Depends(get_db)):
    return RepositorioUsuario(db).getById(idUser)


@app.delete('/user/{idUser}',status_code=status.HTTP_200_OK)
async def getUserIdDelete(idUser,db:Session = Depends(get_db)):
    return RepositorioUsuario(db).setDelete(idUser)