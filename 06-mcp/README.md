# 06 · MCP: tu propio server en ~30 líneas

Sección del deck: "Así nació Hermes: el pegamento de los ATS era exactamente esto."

## Ejercicio · Un MCP server de vacantes con FastMCP (15 min)

`jobs_server.py` expone dos tools (`search_jobs`, `get_job`) sobre un archivo de
vacantes falsas de Guadalajara.

```bash
cd 06-mcp
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# regístralo en Claude Code (scope local del repo):
claude mcp add jobs -- $(pwd)/.venv/bin/python $(pwd)/jobs_server.py
```

Ahora abre `claude` (en la raíz del repo) y pregunta:

> ¿Qué vacantes de AI hay en Guadalajara? Usa el server de jobs y dame el top 3
> con sueldo.

Qué observar:
1. `claude mcp list` muestra tu server; sus **schemas entran al contexto** de cada
   sesión (la renta de la que hablamos en el deck).
2. Una función Python con docstring = una tool con schema. Eso es todo FastMCP.
3. Agrega una tercera tool (ej. `companies()`) y vuelve a probar: el ciclo completo
   toma minutos.

Para limpiar: `claude mcp remove jobs`.
