"""
EQUIPO 8 — Módulo: Fechas Límite
  - Asignar o actualizar la fecha límite de una tarea (formato YYYY-MM-DD)
  - Listar tareas cuya fecha límite ya venció
  - Listar tareas que vencen en los próximos N días
  - Eliminar la fecha límite de una tarea
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 8: Implementar los endpoints ↓

@router.patch("/{id}/fecha-limite", summary="R8.1 Asignar fecha límite (YYYY-MM-DD)")
def asignar_fecha_limite(id: int, db: Session = Depends(get_db)):
    pass


@router.get("/vencidas", summary="R8.2 Tareas cuya fecha límite ya venció")
def tareas_vencidas(db: Session = Depends(get_db)):
    # Solo tareas con fecha_limite asignada y estado != "completada"
    pass


@router.get("/proximas/{dias}", summary="R8.3 Tareas que vencen en los próximos N días")
def tareas_proximas(dias: int, db: Session = Depends(get_db)):
    pass


@router.delete("/{id}/fecha-limite", summary="R8.4 Eliminar la fecha límite de una tarea")
def eliminar_fecha_limite(id: int, db: Session = Depends(get_db)):
    pass
