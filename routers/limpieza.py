"""
EQUIPO 9 — Módulo: Limpieza
  R9.1  DELETE /tareas/limpiar/completadas   — Eliminar todas las tareas completadas
  R9.3  GET    /tareas/archivadas            — Listar todas las tareas archivadas
  R9.2  POST   /tareas/{id}/duplicar         — Duplicar una tarea existente

IMPORTANTE: El orden de los endpoints NO es aleatorio.
FastAPI evalúa las rutas de arriba hacia abajo. Si /{id}/duplicar estuviera
antes que /archivadas, FastAPI intentaría convertir "archivadas" a entero
y lanzaría un error 422. Las rutas estáticas siempre van antes que las dinámicas.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Tarea

router = APIRouter()


# ─────────────────────────────────────────────────────────────────────────────
# R9.1 — Eliminar todas las tareas completadas
# ─────────────────────────────────────────────────────────────────────────────

@router.delete(
    "/limpiar/completadas",
    summary="R9.1 Eliminar todas las tareas completadas",
    description=(
        "Elimina de forma permanente todas las tareas cuyo estado sea **completada**. "
        "Retorna la cantidad de registros eliminados."
    )
)
def limpiar_completadas(db: Session = Depends(get_db)):
    """
    Limpia la base de datos eliminando todas las tareas con estado 'completada'.

    - No requiere parámetros.
    - La eliminación es permanente.
    - Retorna { eliminadas: N } con el total de registros borrados.
    - Si no hay tareas completadas retorna { eliminadas: 0 } sin error.
    """
    completadas = db.query(Tarea).filter(Tarea.estado == "completada").all()
    total = len(completadas)

    for tarea in completadas:
        db.delete(tarea)

    db.commit()

    return {
        "mensaje": "Limpieza completada exitosamente",
        "eliminadas": total
    }


# ─────────────────────────────────────────────────────────────────────────────
# R9.3 — Listar todas las tareas archivadas
# Va antes que /{id}/duplicar para evitar conflicto de rutas en FastAPI
# ─────────────────────────────────────────────────────────────────────────────

@router.get(
    "/limpieza/archivadas",
    summary="R9.3 Listar todas las tareas archivadas",
    description=(
        "Devuelve todas las tareas cuyo estado sea **archivada**, "
        "junto con el conteo total."
    )
)
def listar_archivadas(db: Session = Depends(get_db)):
    """
    Lista todas las tareas con estado 'archivada'.

    - No requiere parámetros.
    - Retorna { total: N, tareas: [...] }.
    - Si no hay tareas archivadas retorna { total: 0, tareas: [] } sin error.
    """
    archivadas = db.query(Tarea).filter(Tarea.estado == "archivada").all()

    return {
        "total": len(archivadas),
        "tareas": [
            {
                "id":           t.id,
                "titulo":       t.titulo,
                "descripcion":  t.descripcion,
                "estado":       t.estado,
                "prioridad":    t.prioridad,
                "fecha_limite": t.fecha_limite,
                "creado_en":    t.creado_en,
            }
            for t in archivadas
        ]
    }


# ─────────────────────────────────────────────────────────────────────────────
# R9.2 — Duplicar una tarea existente
# Ruta dinámica — siempre al final para no interferir con rutas estáticas
# ─────────────────────────────────────────────────────────────────────────────

@router.post(
    "/{id}/duplicar",
    summary="R9.2 Duplicar una tarea existente",
    description=(
        "Crea una copia de la tarea indicada por **id**. "
        "La copia recibe un nuevo ID automático, su estado se fija en **pendiente** "
        "y completado_en se establece en null."
    )
)
def duplicar_tarea(id: int, db: Session = Depends(get_db)):
    """
    Duplica una tarea existente.

    - id: ID de la tarea original a duplicar.
    - Copia título, descripción, prioridad y fecha_limite de la original.
    - La copia siempre inicia con estado 'pendiente' y completado_en = None.
    - Retorna los datos de la tarea nueva junto con el ID original.
    - Lanza 404 si la tarea original no existe.
    """
    original = db.query(Tarea).filter(Tarea.id == id).first()
    if not original:
        raise HTTPException(status_code=404, detail=f"Tarea con id {id} no encontrada")

    copia = Tarea(
        titulo        = original.titulo,
        descripcion   = original.descripcion,
        estado        = "pendiente",
        prioridad     = original.prioridad,
        fecha_limite  = original.fecha_limite,
        completado_en = None,
    )
    db.add(copia)
    db.commit()
    db.refresh(copia)

    return {
        "mensaje":           f"Tarea {id} duplicada exitosamente",
        "tarea_original_id": id,
        "tarea_nueva": {
            "id":           copia.id,
            "titulo":       copia.titulo,
            "descripcion":  copia.descripcion,
            "estado":       copia.estado,
            "prioridad":    copia.prioridad,
            "fecha_limite": copia.fecha_limite,
            "creado_en":    copia.creado_en,
        }
    }