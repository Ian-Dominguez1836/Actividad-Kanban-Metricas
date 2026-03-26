"""
EQUIPO 7 — Módulo: Orden
  - Listar tareas ordenadas por fecha de creación (más antigua primero)
  - Listar tareas ordenadas alfabéticamente por título (A → Z)
  - Listar tareas ordenadas por prioridad (alta → media → baja → sin prioridad)
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 7: Implementar los endpoints ↓

@router.get("/fecha", summary="R7.1 Tareas ordenadas por fecha de creación")
def ordenar_por_fecha(db: Session = Depends(get_db)):
    # Usar .order_by(Tarea.creado_en.asc())
    tareas = db.query(Tarea).order_by(Tarea.creado_en.asc()).all()
    return tareas


@router.get("/titulo", summary="R7.2 Tareas ordenadas alfabéticamente por título")
def ordenar_por_titulo(db: Session = Depends(get_db)):
    # Usar .order_by(Tarea.titulo.asc())
    pass


@router.get("/prioridad", summary="R7.3 Tareas ordenadas por prioridad")
def ordenar_por_prioridad(db: Session = Depends(get_db)):
    # Orden manual: alta=0, media=1, baja=2, None=3
    pass
