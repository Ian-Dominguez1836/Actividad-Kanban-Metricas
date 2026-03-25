"""
EQUIPO 5 — Módulo: Etiquetas
  - Agregar una etiqueta a una tarea
  - Listar todas las etiquetas de una tarea
  - Filtrar tareas que tengan una etiqueta específica
  - Eliminar una etiqueta de una tarea
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea, Etiqueta

router = APIRouter()


# TODO Equipo 5: Implementar los endpoints ↓

@router.post("/{tarea_id}", summary="R5.1 Agregar una etiqueta a una tarea")
def agregar_etiqueta(tarea_id: int, db: Session = Depends(get_db)):
    pass


@router.get("/{tarea_id}", summary="R5.2 Listar etiquetas de una tarea")
def listar_etiquetas(tarea_id: int, db: Session = Depends(get_db)):
    pass


@router.get("/buscar/{nombre}", summary="R5.3 Tareas que tienen cierta etiqueta")
def tareas_por_etiqueta(nombre: str, db: Session = Depends(get_db)):
    pass


@router.delete("/{tarea_id}/{nombre}", summary="R5.4 Eliminar una etiqueta de una tarea")
def eliminar_etiqueta(tarea_id: int, nombre: str, db: Session = Depends(get_db)):
    pass
