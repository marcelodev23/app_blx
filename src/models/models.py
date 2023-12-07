from pydantic import BaseModel
from typing import Optional,List

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone:str
   


class Produto(BaseModel):
    id: Optional[str] = None
    usuario: User
    nome: str
    detalhes:str
    preco: float
    disponivel: bool = False
    foto:Optional[str]

class Pedido(BaseModel):
    id: Optional[str]
    usuario: User
    produto: Produto
    quantidade:int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observacoes'
