from pydantic import BaseModel  

class ProductoIn(BaseModel):
    nombre: str
    descripcion: str | None = None
    stock: int
    precio_compra: float
    precio_venta: float

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None
    stock: int
    precio_compra: float
    precio_venta: float
