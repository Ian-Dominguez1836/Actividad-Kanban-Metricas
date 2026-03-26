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
 
 
@router.get("/", summary="R6.1 Resumen general de tareas")
def resumen_general(db: Session = Depends(get_db)):
    return {
        "total":       db.query(Tarea).count(),
        "completadas": db.query(Tarea).filter(Tarea.estado == "completada").count(),
        "pendientes":  db.query(Tarea).filter(Tarea.estado == "pendiente").count(),
        "archivadas":  db.query(Tarea).filter(Tarea.estado == "archivada").count(),
    }
 
 
@router.get("/estado/{estado}", summary="R6.2 Contar tareas por estado")
def contar_por_estado(estado: str, db: Session = Depends(get_db)):
    return {
        "estado": estado,
        "total":  db.query(Tarea).filter(Tarea.estado == estado).count(),
    }
 
 
@router.get("/prioridad/{prioridad}", summary="R6.3 Contar tareas por prioridad")
def contar_por_prioridad(prioridad: str, db: Session = Depends(get_db)):
    return {
        "prioridad": prioridad,
        "total":     db.query(Tarea).filter(Tarea.prioridad == prioridad).count(),
    }