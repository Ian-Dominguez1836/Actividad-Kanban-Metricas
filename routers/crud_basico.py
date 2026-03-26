"""
EQUIPO 1 — Módulo: CRUD Básico para tareas
  - Crear una nueva tarea
  - Listar todas las tareas
  - Obtener una tarea por ID
  - Eliminar una tarea por ID
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea
from datetime import datetime
from typing import Literal

router = APIRouter()


# TODO Equipo 1: Implementar los endpoints ↓

@router.post("/", summary="R1.1 Crear una nueva tarea")
def crear_tarea(titulo: str, descripcion: str, estado: Literal["pendiente", "completada", "archivada"], fecha_limite: datetime | None = None, prioridad: Literal["alta", "media", "baja"] | None = None, db: Session = Depends(get_db)):
    nueva_tarea = Tarea(
        titulo=titulo,
        descripcion=descripcion,
        estado = estado if estado else "pendiente",
        fecha_limite=fecha_limite if fecha_limite else None,
        prioridad=prioridad 
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return {
        "mensaje": "Tarea creada exitosamente",
        "tarea": nueva_tarea
    }


@router.get("/", summary="R1.2 Listar todas las tareas")
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()


@router.get("/{id}", summary="R1.3 Obtener una tarea por ID")
def obtener_tarea(id: int, db: Session = Depends(get_db)):
    pass


@router.delete("/{id}", summary="R1.4 Eliminar una tarea por ID")
def eliminar_tarea(id: int, db: Session = Depends(get_db)):
    pass
