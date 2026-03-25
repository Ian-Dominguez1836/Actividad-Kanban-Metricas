"""
EQUIPO 2 — Módulo: Edición
  - Editar el título de una tarea
  - Editar la descripción de una tarea
  - Asignar o cambiar la prioridad (alta | media | baja)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 2: Implementar los endpoints ↓

@router.patch("/{id}/titulo", summary="R2.1 Editar el título de una tarea")
def editar_titulo(id: int, db: Session = Depends(get_db)):
    pass


@router.patch("/{id}/descripcion", summary="R2.2 Editar la descripción de una tarea")
def editar_descripcion(id: int, db: Session = Depends(get_db)):
    pass


@router.patch("/{id}/prioridad", summary="R2.3 Asignar prioridad (alta | media | baja)")
def asignar_prioridad(id: int, db: Session = Depends(get_db)):
    # Valores válidos: "alta", "media", "baja"
    pass
