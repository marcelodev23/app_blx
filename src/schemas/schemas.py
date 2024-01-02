from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None
    #usuario: User
    nome: str
    detalhes:str
    preco: float
    disponivel: bool = False
    user_id:int
    class Config:
        extra = 'forbid'
        from_attributes = True


class User(BaseModel):
    id: Optional[int] = None
    nome: str
    senha:str
    telefone:str
    class Config:
        extra = 'forbid'
        from_attributes = True


class ProdutoOut(BaseModel):
    id:int
    nome: str
    detalhes:str
    preco: float
    user:Optional[User]
    class Config:
        extra = 'forbid'
        from_attributes = True

class ProdutoSaida(BaseModel):
    nome: str
    detalhes:str
    preco: float
    class Config:
        extra = 'forbid'
        from_attributes = True

class Usurio(BaseModel):
    nome: str
    telefone:str
    class Config:
        extra = 'forbid'
        from_attributes = True

class LoginData(BaseModel):
    telefone:str
    senha:str
    class Config:
        extra = 'forbid'
        from_attributes = True

class LoginSucesso(BaseModel):
    usuario:Usurio
    acess_token:str
    class Config:
        extra = 'forbid'
        from_attributes = True

class Pedido(BaseModel):
    id: Optional[int] = None
    quandidade:int
    local_entrega: Optional[str] 
    tipo_entraga: str
    observacoes: Optional[str] = 'Sem observacoes'
    usuario_id: Optional[int]
    produto_id: Optional[int]
    class Config:
        extra = 'forbid'
        from_attributes = True

class PedidoSaida(BaseModel):
    produtos:ProdutoSaida
    quandidade:int
    local_entrega: Optional[str] 
    tipo_entraga: str
    observacoes: Optional[str]
    class Config:
        extra = 'forbid'
        from_attributes = True


class PedidoLista(BaseModel):
    produtos:ProdutoSaida
    quandidade:int
    local_entrega: Optional[str] 
    tipo_entraga: str
    observacoes: Optional[str] 
    user:Optional[Usurio]
    class Config:
        extra = 'forbid'
        from_attributes = True

class UserOut(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone:str
    produtos:list[ProdutoSaida]
    meus_pedidos:list[PedidoSaida]
    class Config:
        extra = 'forbid'
        from_attributes = True


