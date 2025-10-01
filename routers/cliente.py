from typing import List
from fastapi import APIRouter
from schemas.cliente import Cliente, ClienteIn
import services.cliente as service

router = APIRouter()

@router.get("/", response_model=List[Cliente])
async def read_clientes():
    return await service.get_all_clientes()


@router.get("/{id}", response_model=Cliente)
async def read_cliente(id: int):
    return await service.get_cliente_by_id(id)


@router.post("/", response_model=Cliente)
async def create_cliente(cliente: ClienteIn):
    return await service.create_cliente(cliente)


@router.put("/{id}", response_model=Cliente)
async def update_cliente(id: int, cliente: ClienteIn):
    return await service.update_cliente(id, cliente)


@router.delete("/{id}")
async def delete_cliente(id: int):
    return await service.delete_cliente(id)
