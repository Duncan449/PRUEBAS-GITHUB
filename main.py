#Herrera Valentino Gabriel - EISI1089 - 44921920 -ISI 
from fastapi import FastAPI
from config.database import db
from routers import cliente
from routers import producto
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
async def root():
    return {"message": "Bienvenidos a mi API REST"}


app.include_router(cliente.router, prefix="/clientes")
app.include_router(producto.router, prefix="/productos")