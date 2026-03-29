"""
EQUIPO 3 — Módulo: Estados de tareas
  - Marcar una tarea como completada (registra fecha y hora)
  - Revertir una tarea a pendiente (limpia completado_en)
  - Archivar una tarea
  - Restaurar una tarea archivada a pendiente
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 3: Implementar los endpoints ↓

@router.patch("/{id}/completar", summary="R3.1 Marcar tarea como completada")
def marcar_completada(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.estado = "completada"
    tarea.completado_en = datetime.utcnow()
    db.commit()
    db.refresh(tarea)
    return tarea


@router.patch("/{id}/pendiente", summary="R3.2 Revertir tarea a pendiente")
def marcar_pendiente(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.estado = "pendiente"
    tarea.completado_en = None
    db.commit()
    db.refresh(tarea)
    return tarea


@router.patch("/{id}/archivar", summary="R3.3 Archivar una tarea")
def archivar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.estado = "archivada"
    tarea.completado_en = None
    db.commit()
    db.refresh(tarea)
    return tarea


@router.patch("/{id}/restaurar", summary="R3.4 Restaurar tarea archivada a pendiente")
def restaurar_tarea(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if tarea.estado != "archivada":
        raise HTTPException(status_code=400, detail="La tarea no está archivada")
    tarea.estado = "pendiente"
    db.commit()
    db.refresh(tarea)
    return tarea
