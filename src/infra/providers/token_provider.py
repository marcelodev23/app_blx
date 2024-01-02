from datetime import datetime,timedelta
from jose import jwt

SECRET_KEY = '967ebedd18483e4cfa3e18401388e2a4'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_access_token(data:dict):
    dados = data.copy()
    dados.update({'exp':datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)})
    return jwt.encode(dados,SECRET_KEY,algorithm = ALGORITHM)

def verificar_access_token(token:str):
    payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
    return payload.get('sub')