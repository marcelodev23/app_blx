from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import engine,Base
from src.infra.sqlalchemy.models import models
from src.routers import produtos as produtos_router
from src.routers import auth as usuarios_router
from src.routers import pedido   as pedido_router 

app = FastAPI(title='App BLX')

#models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produtos_router.router)
app.include_router(usuarios_router.route,prefix='/auth')
app.include_router(pedido_router.router)

@app.get('/')
async def root():
    return {"Msg":"Ok Porra"}
