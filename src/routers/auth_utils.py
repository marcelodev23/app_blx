from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers.token_provider import verificar_access_token
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

oauth2_schema= OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token:str = Depends(oauth2_schema),db:Session=Depends(get_db)):
    try:
        telefone = verificar_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = 'Token inválido')
    if not telefone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Token inválido')
    usuario = RepositorioUsuario(db).getByTelefone(telefone)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Token inválido'
        )
    return usuario