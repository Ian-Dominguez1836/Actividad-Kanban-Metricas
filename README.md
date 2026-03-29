# To Do — Sistema de Gestión de Tareas
**UACJ · Métricas del Software · 2025**

## Estructura del proyecto

```
proyecto_kanban/
├── main.py          ← Punto de entrada (NO modificar)
├── database.py      ← Modelos y conexión SQLite (NO modificar)
├── requirements.txt
└── routers/
    ├── crud_basico.py   ← Equipo 1
    ├── edicion.py       ← Equipo 2
    ├── estados.py       ← Equipo 3
    ├── busqueda.py      ← Equipo 4
    ├── etiquetas.py     ← Equipo 5
    ├── estadisticas.py  ← Equipo 6
    ├── orden.py         ← Equipo 7
    ├── fechas.py        ← Equipo 8
    └── limpieza.py      ← Equipo 9
```

## Instalación

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Abre **http://127.0.0.1:8000/docs** para probar todos los endpoints.

## Instrucciones por equipo

1. Trabaja **únicamente** en el archivo de tu equipo dentro de `routers/`.
2. **No modificar** `database.py`, `main.py` ni archivos de otros equipos.
3. Importa lo que necesites así: `from database import get_db, Tarea, Etiqueta`
4. Implementa los endpoints marcados con `# TODO`.
5. Prueba en `/docs` que respondan correctamente antes de marcar tu tarjeta como **Terminado** en el tablero.

## Modelos disponibles

### `Tarea`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | int | ID único autoincremental |
| `titulo` | str | Título de la tarea |
| `descripcion` | str | Descripción detallada |
| `estado` | str | `"pendiente"` \| `"completada"` \| `"archivada"` |
| `prioridad` | str \| None | `"alta"` \| `"media"` \| `"baja"` \| `None` |
| `fecha_limite` | str \| None | Formato `"YYYY-MM-DD"` |
| `creado_en` | datetime | Fecha y hora de creación |
| `completado_en` | datetime \| None | Fecha y hora de completado |

### `Etiqueta`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | int | ID único |
| `tarea_id` | int | FK → `tareas.id` |
| `nombre` | str | Nombre de la etiqueta |
