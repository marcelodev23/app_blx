from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido as pedido_schemas
from src.schemas.schemas import PedidoLista
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPidido
from typing import List

router = APIRouter()


@router.post('/pedido',status_code=status.HTTP_201_CREATED)
async def criaPedio(pedido:pedido_schemas,db:Session=Depends(get_db)):
    return RepositorioPidido(db).setCreate(pedido)

@router.get('/pedido',status_code=status.HTTP_200_OK,response_model=List[PedidoLista])
async def getPedido(db:Session=Depends(get_db)):
    return RepositorioPidido(db).getAll()

@router.get('/pedido/{id}',status_code=status.HTTP_200_OK,response_model=PedidoLista)
async def getIdPedido(id:int,db:Session = Depends(get_db)):
    pedido = RepositorioPidido(db).getById(id)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'id = {id} Not found'
        )
    return pedido

@router.get('/pedido/{id}/vendas',status_code=status.HTTP_200_OK)
async def getIdPedido_vendas(id:int,db:Session = Depends(get_db)):
    vendas = RepositorioPidido(db).SetMinhaVendasByIdUser(id)
    #if not vendas:
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail=f'id = {id} Not found'
    #    )
    return vendas


@router.get('/pedido/{id}/compras',status_code=status.HTTP_200_OK)
async def getIdPedido_meus(id:int,db:Session = Depends(get_db)):
    compras = RepositorioPidido(db).SetMeusPedidosByIdUser(id)
    #if not compras:
    #    raise HTTPException(
    #        status_code=status.HTTP_404_NOT_FOUND,
    #        detail=f'id = {id} Not found'
    #    )
    return compras


@router.put('/pedido/{id}',status_code=status.HTTP_202_ACCEPTED)
async def editePedido(id:int,pedido:pedido_schemas,db:Session= Depends(get_db)):
    try:
        RepositorioPidido(db).setUpdate(id=id,pedido=pedido)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = 'Erro ao editar o produto'
        )

@router.delete('/pedido/{id}',status_code=status.HTTP_202_ACCEPTED)
async def deletePetido(id:int,db:Session = Depends(get_db)):
    try:
        RepositorioPidido(db).SetDelete(id)
    except:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = 'Erro ao deleta o produto'
        )