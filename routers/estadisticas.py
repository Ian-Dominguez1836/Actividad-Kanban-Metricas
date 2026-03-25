"""
EQUIPO 6 — Módulo: Estadísticas
  - Resumen general (total, completadas, pendientes, archivadas)
  - Contar tareas por estado
  - Contar tareas por prioridad
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 6: Implementar los endpoints ↓

@router.get("/", summary="R6.1 Resumen general de tareas")
def resumen_general(db: Session = Depends(get_db)):
    # Retornar dict con: total, completadas, pendientes, archivadas
    pass


@router.get("/estado/{estado}", summary="R6.2 Contar tareas por estado")
def contar_por_estado(estado: str, db: Session = Depends(get_db)):
    pass


@router.get("/prioridad/{prioridad}", summary="R6.3 Contar tareas por prioridad")
def contar_por_prioridad(prioridad: str, db: Session = Depends(get_db)):
    pass
