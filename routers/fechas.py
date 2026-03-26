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
    if dias < 0:
        raise HTTPException(status_code=400, detail="El número de días debe ser no negativo")
    hoy = datetime.now().date()
    fecha_limite_max = hoy + timedelta(days=dias)

    tareas = db.query(Tarea).filter(
        Tarea.fecha_limite != None,
        Tarea.estado != "completada",
        Tarea.fecha_limite >= hoy,
        Tarea.fecha_limite <= fecha_limite_max
    ).all()
    if not tareas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas que vencen en los próximos días")
    return tareas

@router.delete("/{id}/fecha-limite", summary="R8.4 Eliminar la fecha límite de una tarea")
def eliminar_fecha_limite(id: int, db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.fecha_limite = None
    db.commit()
    db.refresh(tarea)
    return {"message": "Fecha límite eliminada exitosamente", "tarea": tarea}
