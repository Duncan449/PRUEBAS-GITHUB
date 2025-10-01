from typing import List
from fastapi import HTTPException
from config.database import db
from schemas.producto import ProductoIn, Producto

async def get_productos() -> List[Producto]:    #GET todos los productos
    query = "SELECT * FROM productos"
    rows = await db.fetch_all(query=query)
    return rows

async def get_producto_por_id(id: int) -> Producto:   #GET producto por id
    query = "SELECT * FROM productos WHERE id = :id "
    row = await db.fetch_one(query=query, values={"id": id})
    if not row:
        raise HTTPException(status_code=404, detail="Producto no encontrado")  #Retorna error si no lo encuentra
    return row

async def crear_producto(producto: ProductoIn) -> Producto:   #POST producto
    query = """
        INSERT INTO productos (nombre, descripcion, stock, precio_compra, precio_venta)
        VALUES (:nombre, :descripcion, :stock, :precio_compra, :precio_venta)
    """

    id_del_ultimo_registro = await db.execute(query=query, values=producto.dict())
    return {"id": id_del_ultimo_registro,**producto.dict()}

async def actualizar_producto(producto_id:int, producto: ProductoIn) -> Producto:   #POST producto
    query = """
        UPDATE productos
        SET nombre = :nombre,
            descripcion = :descripcion,
            stock = :stock,
            precio_compra = :precio_compra,
            precio_venta = :precio_venta
        WHERE id = :id
    """
    values = {**producto.dict(), "id": producto_id}
    await db.execute(query=query, values = values)
    return {"id": producto_id, **producto.dict()}

async def borrar_producto(id:int) -> dict:         #DELETE producto
    query = "DELETE FROM productos WHERE id = :id"
    result = await db.execute(query=query, values={"id": id})
    if not result:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado correctamente"}