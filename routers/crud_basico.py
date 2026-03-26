"""
EQUIPO 1 — Módulo: CRUD Básico para tareas
  - Crear una nueva tarea
  - Listar todas las tareas
  - Obtener una tarea por ID
  - Eliminar una tarea por ID
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# TODO Equipo 1: Implementar los endpoints ↓

@router.post("/", summary="R1.1 Crear una nueva tarea")
def crear_tarea(db: Session = Depends(get_db)):
    pass


@router.get("/", summary="R1.2 Listar todas las tareas")
def listar_tareas(db: Session = Depends(get_db)):
    pass


@router.get("/{id}", summary="R1.3 Obtener una tarea por ID")
def obtener_tarea(id: str, db: Session = Depends(get_db)):
    if not id.isdigit() or int(id) <= 0:
        raise HTTPException(status_code=400, detail="ID inválido")

    tarea_id = int(id)
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return {
        "id": tarea.id,
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "estado": tarea.estado,
        "prioridad": tarea.prioridad,
        "fecha_limite": tarea.fecha_limite,
        "creado_en": tarea.creado_en,
        "completado_en": tarea.completado_en,
    }


@router.delete("/{id}", summary="R1.4 Eliminar una tarea por ID")
def eliminar_tarea(id: str, db: Session = Depends(get_db)):
    if not id.isdigit() or int(id) <= 0:
        raise HTTPException(status_code=400, detail="ID inválido")

    tarea_id = int(id)
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(tarea)
    db.commit()

    return {"mensaje": f"Tarea con ID {tarea_id} eliminada correctamente"}
