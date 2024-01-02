from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.schemas.schemas import User,Usurio,LoginData,LoginSucesso
from src.infra.providers.hash_provider import gerar_hash,verificar_hash
from src.infra.providers.token_provider import criar_access_token
from src.routers.auth_utils import obter_usuario_logado

route = APIRouter() 

@route.post('/signup',status_code=status.HTTP_201_CREATED,response_model=Usurio)
async def setUser(usuario:User,db:Session = Depends(get_db)):
    if RepositorioUsuario(db).getByTelefone(usuario.telefone):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = 'já existe um usuário para este telefone'
        )
    usuario.senha = gerar_hash(usuario.senha)
    user = RepositorioUsuario(db).setCreate(usuario)
    return user 

@route.post('/login',status_code=status.HTTP_202_ACCEPTED,response_model=LoginSucesso)
async def login(login_data:LoginData,db:Session=Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    usuario = RepositorioUsuario(db).getByTelefone(telefone) 
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Usuario not found'
        )
    if not verificar_hash(senha,usuario.senha):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = 'Senha not found'
        )
    return {
        'usuario':usuario,
        'acess_token':criar_access_token({'sub':usuario.telefone})
    }

@route.get('/me',response_model=Usurio)
async def me(usuario:User = Depends(obter_usuario_logado)):
    return usuario

@route.delete('/me',status_code=status.HTTP_200_OK)
async def getUserIdDelete(db:Session = Depends(get_db),usuario:User = Depends(obter_usuario_logado)):
    try:
        RepositorioUsuario(db).setDelete(usuario.id)
        return {
            'msg':f'Usuario {usuario.nome} deletado'
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )