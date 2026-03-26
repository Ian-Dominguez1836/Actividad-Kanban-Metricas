"""
EQUIPO 8 — Módulo: Fechas Límite
  - Asignar o actualizar la fecha límite de una tarea (formato YYYY-MM-DD)
  - Listar tareas cuya fecha límite ya venció
  - Listar tareas que vencen en los próximos N días
  - Eliminar la fecha límite de una tarea
"""

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, date
from database import get_db, Tarea
from sqlalchemy import and_

router = APIRouter()


# TODO Equipo 8: Implementar los endpoints ↓

@router.patch("/{id}/fecha-limite", summary="R8.1 Asignar fecha límite (YYYY-MM-DD)")
def asignar_fecha_limite(id: int,
    fecha_limite: date = Body(..., embed=True),
    db: Session = Depends(get_db)
):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea.fecha_limite = fecha_limite
    db.commit()
    db.refresh(tarea)

    return {
        "message": "Fecha límite asignada correctamente",
        "tarea": {
            "id": tarea.id,
            "fecha_limite": tarea.fecha_limite,
            "estado": tarea.estado
        }
    }
    


@router.get("/vencidas", summary="R8.2 Tareas cuya fecha límite ya venció")
def tareas_vencidas(db: Session = Depends(get_db)):
    # Solo tareas con fecha_limite asignada y estado != "completada"
    hoy = date.today()

    tareas = (
        db.query(Tarea)
        .filter(
            and_(
                Tarea.fecha_limite.isnot(None),
                Tarea.fecha_limite < hoy,
                Tarea.estado != "completada"
            )
        )
        .all()
    )
    if not tareas:
        return {
            "message": "No hay tareas vencidas",
            "total": 0,
            "tareas": []
        }
    return {
        "total": len(tareas),
        "tareas": tareas
    }


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
