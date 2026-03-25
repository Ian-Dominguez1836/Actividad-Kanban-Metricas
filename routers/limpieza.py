"""
EQUIPO 9 — Módulo: Limpieza
  - Eliminar todas las tareas completadas
  - Duplicar una tarea existente (nuevo ID, estado "pendiente")
  - Listar todas las tareas archivadas
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 9: Implementar los endpoints ↓

@router.delete("/limpiar/completadas", summary="R9.1 Eliminar todas las tareas completadas")
def limpiar_completadas(db: Session = Depends(get_db)):
    # Retornar cuántas tareas fueron eliminadas
    pass


@router.post("/{id}/duplicar", summary="R9.2 Duplicar una tarea existente")
def duplicar_tarea(id: int, db: Session = Depends(get_db)):
    # La copia debe tener un nuevo ID, estado "pendiente" y completado_en = None
    pass


@router.get("/archivadas", summary="R9.3 Listar todas las tareas archivadas")
def listar_archivadas(db: Session = Depends(get_db)):
    pass
