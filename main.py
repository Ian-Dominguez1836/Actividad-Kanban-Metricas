"""
To-Do — Sistema de Gestión de Tareas
UACJ · Métricas del Software · 2025
Archivo de integración - Equipo de presentación
Cada equipo registra su router aquí al terminar su módulo.
"""

from fastapi import FastAPI
from database import create_tables
from routers import crud_basico    # Equipo 1
from routers import edicion        # Equipo 2
from routers import estados        # Equipo 3
from routers import busqueda       # Equipo 4
from routers import etiquetas      # Equipo 5
from routers import estadisticas   # Equipo 6
from routers import orden          # Equipo 7
from routers import fechas         # Equipo 8
from routers import limpieza       # Equipo 9

app = FastAPI(
    title="TodoUACJ",
    description="Sistema de Gestión de Tareas · Práctica Kanban · UACJ 2025",
    version="1.0.0"
)

create_tables()

app.include_router(crud_basico.router,  prefix="/tareas",       tags=["CRUD Básico — E1"])
app.include_router(edicion.router,      prefix="/tareas",       tags=["Edición — E2"])
app.include_router(estados.router,      prefix="/tareas",       tags=["Estados — E3"])
app.include_router(busqueda.router,     prefix="/busqueda",     tags=["Búsqueda — E4"])
app.include_router(etiquetas.router,    prefix="/etiquetas",    tags=["Etiquetas — E5"])
app.include_router(estadisticas.router, prefix="/estadisticas", tags=["Estadísticas — E6"])
app.include_router(orden.router,        prefix="/orden",        tags=["Orden — E7"])
app.include_router(fechas.router,       prefix="/fechas",       tags=["Fechas — E8"])
app.include_router(limpieza.router,     prefix="/tareas",       tags=["Limpieza — E9"])


@app.get("/", tags=["Sistema"])
def root():
    return {
        "sistema": "To-Do Metricas",
        "version": "1.0.0",
        "docs": "Abre /docs para probar todos los endpoints",
        "modulos": {
            "E1": "/tareas       — CRUD básico",
            "E2": "/tareas/{id}  — Edición",
            "E3": "/tareas/{id}  — Estados",
            "E4": "/busqueda     — Búsqueda",
            "E5": "/etiquetas    — Etiquetas",
            "E6": "/estadisticas — Estadísticas",
            "E7": "/orden        — Orden",
            "E8": "/fechas       — Fechas límite",
            "E9": "/tareas       — Limpieza",
        }
    }
