from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db,criar_bd,engine
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.models import models
app = FastAPI()
#criar_bd()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"Msg":"Ok Porra"}



@app.post('/produtos')
async def criar_poduto(produto: Produto,db:Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
async def lista_produtos():
    return {"Msg":"Listagem de Produtos"}