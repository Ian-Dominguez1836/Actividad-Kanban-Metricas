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

# EDWIN
@router.get("/titulo/{palabra}", summary="R4.1 Buscar tareas por palabra clave en el título")
def buscar_por_titulo(palabra: str, db: Session = Depends(get_db)):
    # Usar .ilike(f"%{palabra}%") para búsqueda parcial sin distinguir mayúsculas
    tareas = db.query(Tarea).filter(Tarea.titulo.ilike(f"%{palabra}%")).all()
    return {"palabra": palabra, "total": len(tareas), "tareas": tareas}

# JESUS
@router.get("/estado/{estado}", summary="R4.2 Filtrar tareas por estado")
def filtrar_por_estado(estado: str, db: Session = Depends(get_db)):
    # Estados válidos: "pendiente", "completada", "archivada"
     estados_validos = ["pendiente", "completada", "archivada"]
    if estado not in estados_validos:
        raise HTTPException(status_code=400, detail=f"Estado inválido. Valores permitidos: {estados_validos}")
    # Buscar todas las tareas que coincidan con el estado indicado
    tareas = db.query(Tarea).filter(Tarea.estado == estado).all()
    return {"estado": estado, "total": len(tareas), "tareas": tareas}



# Vicente
@router.get("/prioridad/{prioridad}", summary="R4.3 Filtrar tareas por prioridad")
def filtrar_por_prioridad(prioridad: str, db: Session = Depends(get_db)):
    # Prioridades válidas: "alta", "media", "baja"
    # Validar que la prioridad recibida sea una de las tres permitidas
    prioridades_validas = ["alta", "media", "baja"]
    if prioridad not in prioridades_validas:
        raise HTTPException(status_code=400, detail=f"Prioridad inválida. Valores permitidos: {prioridades_validas}")
    # Buscar todas las tareas que coincidan con la prioridad indicada
    tareas = db.query(Tarea).filter(Tarea.prioridad == prioridad).all()
    # Termina con la función y manda de regreso los resultados
    return {"prioridad": prioridad, "total": len(tareas), "tareas": tareas}
