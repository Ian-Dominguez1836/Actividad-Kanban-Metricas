from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()

# --- Endpoints de Edición ---

@router.patch("/{id}/titulo", summary="R2.1 Editar el título de una tarea")
def editar_titulo(id: int, titulo: str = Body(..., embed=True), db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    tarea.titulo = titulo
    db.commit()
    db.refresh(tarea)
    return tarea


@router.patch("/{id}/descripcion", summary="R2.2 Editar la descripción de una tarea")
def editar_descripcion(id: int, descripcion: str = Body(..., embed=True), db: Session = Depends(get_db)):
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    tarea.descripcion = descripcion
    db.commit()
    db.refresh(tarea)
    return tarea


@router.patch("/{id}/prioridad", summary="R2.3 Asignar prioridad (alta | media | baja)")
def asignar_prioridad(id: int, prioridad: str = Body(..., embed=True), db: Session = Depends(get_db)):
    # 1. Validar valores permitidos
    valores_validos = ["alta", "media", "baja"]
    if prioridad not in valores_validos:
        raise HTTPException(status_code=400, detail="Prioridad inválida. Use: alta, media o baja")

    # 2. Buscar la tarea
    tarea = db.query(Tarea).filter(Tarea.id == id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    # 3. Actualizar
    tarea.prioridad = prioridad
    db.commit()
    db.refresh(tarea)
    return tarea