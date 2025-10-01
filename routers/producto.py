from typing import List
from fastapi import APIRouter
from schemas.producto import Producto,ProductoIn
import services.producto as service

router = APIRouter()

@router.get("/", response_model=List[Producto])
async def get_productos_():
    return await service.get_productos()

@router.get("/{id}", response_model=Producto)
async def get_producto(id: int):
    return await service.get_producto_por_id(id)

@router.post("/", response_model=Producto)
async def post_producto(producto: ProductoIn):
    return await service.crear_producto(producto)

@router.put("/{id}", response_model=Producto)
async def put_producto(id:int, producto: ProductoIn):
    return await service.actualizar_producto(id, producto)

@router.delete("/{id}")
async def delete_producto(id: int):
    return await service.borrar_producto(id)