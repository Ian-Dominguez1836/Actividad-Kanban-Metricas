"""
To-Do — Base de datos compartida
Todos los equipos importan desde aquí: from database import get_db, Base, Tarea
NO modificar este archivo.
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime

DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# MODELOS

class Tarea(Base):
    __tablename__ = "tareas"

    id              = Column(Integer, primary_key=True, index=True)
    titulo          = Column(String,  nullable=False)
    descripcion     = Column(String,  nullable=False)
    estado          = Column(String,  default="pendiente")   # pendiente | completada | archivada
    prioridad       = Column(String,  nullable=True)         # alta | media | baja | None
    fecha_limite    = Column(String,  nullable=True)         # YYYY-MM-DD | None
    creado_en       = Column(DateTime, default=datetime.utcnow)
    completado_en   = Column(DateTime, nullable=True)


class Etiqueta(Base):
    __tablename__ = "etiquetas"

    id       = Column(Integer, primary_key=True, index=True)
    tarea_id = Column(Integer, ForeignKey("tareas.id"), nullable=False)
    nombre   = Column(String,  nullable=False)


# DEPENDENCIA FastAPI 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
