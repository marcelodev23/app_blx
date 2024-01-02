from passlib.context import CryptContext

pwd = CryptContext(schemes=['bcrypt'],deprecated="auto")
#sha256_crypt

def gerar_hash(text):
    return pwd.hash(text)

def verificar_hash(text,hash):
    return pwd.verify(text,hash)

