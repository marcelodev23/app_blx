from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.schemas.schemas import Produto,ProdutoOut
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

@router.post('/produtos',status_code=status.HTTP_201_CREATED,response_model=ProdutoOut)
async def criar_poduto(produto: Produto,db:Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.get('/produtos',status_code=status.HTTP_200_OK,response_model=List[ProdutoOut])
async def lista_produtos(db:Session = Depends(get_db)):
    return RepositorioProduto(db).listar()



@router.get('/produtos/{id}',status_code=status.HTTP_200_OK,response_model=List[ProdutoOut])
async def getIdProduto(id:int,db:Session=Depends(get_db)):
    get =RepositorioProduto(db).obter(id)
    if not get :
        raise HTTPException(status_code=404, detail="Não há um produto com este id")
    return get

@router.delete('/produtos/{id}',status_code=status.HTTP_200_OK)
async def getUserIdDelete(id,db:Session = Depends(get_db)):
    return RepositorioProduto(db).remover(id)

@router.put('/produtos/{id}',status_code=status.HTTP_200_OK)
async def editaProdutos(id:int,produto: Produto,db:Session = Depends(get_db)):
    RepositorioProduto(db).editar(produto,id)
    return {"msg":"protudo atualizado"}