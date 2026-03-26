"""
EQUIPO 5 — Módulo: Etiquetas
  - Agregar una etiqueta a una tarea
  - Listar todas las etiquetas de una tarea
  - Filtrar tareas que tengan una etiqueta específica
  - Eliminar una etiqueta de una tarea
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea, Etiqueta
from fastapi import Body
from fastapi import Query

router = APIRouter()


# TODO Equipo 5: Implementar los endpoints ↓

@router.post("/{tarea_id}", summary="R5.1 Agregar una etiqueta a una tarea")
def agregar_etiqueta(tarea_id: int, nombre: str = Query(...), db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    nueva = Etiqueta(tarea_id=tarea_id, nombre=nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


@router.get("/{tarea_id}", summary="R5.2 Listar etiquetas de una tarea")
def listar_etiquetas(tarea_id: int, db: Session = Depends(get_db)):
    etiquetas = db.query(Etiqueta).filter(Etiqueta.tarea_id == tarea_id).all()

    if not etiquetas:
        raise HTTPException(status_code=404, detail="No hay etiquetas para esta tarea")

    return etiquetas


@router.get("/buscar/{nombre}", summary="R5.3 Tareas que tienen cierta etiqueta")
def tareas_por_etiqueta(nombre: str, db: Session = Depends(get_db)):
    etiquetas = db.query(Etiqueta).filter(Etiqueta.nombre.ilike(f"%{nombre}%")).all()

    if not etiquetas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas con esa etiqueta")

    tareas = []
    for etiqueta in etiquetas:
        tarea = db.query(Tarea).filter(Tarea.id == etiqueta.tarea_id).first()
        if tarea:
            tareas.append(tarea)

    return tareas


@router.delete("/{tarea_id}/{nombre}", summary="R5.4 Eliminar una etiqueta de una tarea")
def eliminar_etiqueta(tarea_id: int, nombre: str, db: Session = Depends(get_db)):
    etiqueta = db.query(Etiqueta).filter(
        Etiqueta.tarea_id == tarea_id,
        Etiqueta.nombre == nombre
    ).first()

    if not etiqueta:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")

    db.delete(etiqueta)
    db.commit()

    return {"mensaje": "Etiqueta eliminada correctamente"}
