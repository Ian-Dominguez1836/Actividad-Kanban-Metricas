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

router = APIRouter()


# TODO Equipo 1: Implementar los endpoints ↓

@router.post("/", summary="R1.1 Crear una nueva tarea")
def crear_tarea(db: Session = Depends(get_db)):
    pass


@router.get("/", summary="R1.2 Listar todas las tareas")
def listar_tareas(db: Session = Depends(get_db)):
    pass


@router.get("/{id}", summary="R1.3 Obtener una tarea por ID")
def obtener_tarea(id: int, db: Session = Depends(get_db)):
    pass


@router.delete("/{id}", summary="R1.4 Eliminar una tarea por ID")
def eliminar_tarea(id: int, db: Session = Depends(get_db)):
    pass
