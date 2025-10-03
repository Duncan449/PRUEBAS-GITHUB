from typing import List
from fastapi import HTTPException
from config.database import db
from schemas.cliente import Cliente, ClienteIn


async def get_all_clientes() -> List[Cliente]:
    query = "SELECT * FROM clientes"
    rows = await db.fetch_all(query=query)
    return rows


async def get_cliente_by_id(id: int) -> Cliente:
    query = "SELECT * FROM clientes WHERE id = :id"
    row = await db.fetch_one(query=query, values={"id": id})
    if not row:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return row


async def create_cliente(cliente: ClienteIn) -> Cliente:
    query = """
        INSERT INTO clientes (dni, nombre, apellido, direccion, telefono)
        VALUES (:dni, :nombre, :apellido, :direccion, :telefono)
    """
    last_record_id = await db.execute(query=query, values=cliente.dict())
    return {**cliente.dict(), "id": last_record_id}


"""
** desempaquetado de diccionario (Dictionary Unpacking)

cliente.dict() convierte un objeto Pydantic en un diccionario
"""


async def update_cliente(cliente_id: int, cliente: ClienteIn) -> Cliente:
    query = """
        UPDATE clientes
        SET dni = :dni,
            nombre = :nombre,
            apellido = :apellido,
            direccion = :direccion,
            telefono = :telefono
        WHERE id = :id
    """
    values = {**cliente.dict(), "id": cliente_id}
    await db.execute(query=query, values=values)
    return {**cliente.dict(), "id": cliente_id}


async def delete_cliente(id: int) -> dict:
    query = "DELETE FROM clientes WHERE id = :id"
    result = await db.execute(query=query, values={"id": id})
    if not result:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"message": "Cliente eliminado correctamente"}

async def nada():
    return {"Hola"}

#Puto d emierda" 
