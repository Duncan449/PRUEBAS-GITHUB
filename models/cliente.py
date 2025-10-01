"""
Este archivo es solo un ejemplo, porque no estamos
utilizando un ORM (Object Relational Mapping)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dni = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    direccion = Column(String(100), nullable=True)
    telefono = Column(String(20), nullable=True)

    def __repr__(self):
        return (
            f"<Cliente(id={self.id}, nombre={self.nombre}, apellido={self.apellido})>"
        )
