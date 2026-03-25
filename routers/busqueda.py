"""
EQUIPO 4 — Módulo: Búsqueda
Requerimientos:
  R4.1  Buscar tareas por palabra clave en el título (parcial, sin distinguir mayúsculas)
  R4.2  Filtrar tareas por estado (pendiente | completada | archivada)
  R4.3  Filtrar tareas por prioridad (alta | media | baja)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 4: Implementar los endpoints ↓

@router.get("/titulo/{palabra}", summary="R4.1 Buscar tareas por palabra clave en el título")
def buscar_por_titulo(palabra: str, db: Session = Depends(get_db)):
    # Usar .ilike(f"%{palabra}%") para búsqueda parcial sin distinguir mayúsculas
    pass


@router.get("/estado/{estado}", summary="R4.2 Filtrar tareas por estado")
def filtrar_por_estado(estado: str, db: Session = Depends(get_db)):
    # Estados válidos: "pendiente", "completada", "archivada"
    pass


@router.get("/prioridad/{prioridad}", summary="R4.3 Filtrar tareas por prioridad")
def filtrar_por_prioridad(prioridad: str, db: Session = Depends(get_db)):
    # Prioridades válidas: "alta", "media", "baja"
    pass
