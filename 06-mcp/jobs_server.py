"""MCP server de vacantes (fake) con FastMCP, en ~30 líneas."""
import json
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("jobs")
VACANTES = json.loads((Path(__file__).parent / "vacantes.json").read_text())


@mcp.tool
def search_jobs(query: str = "", location: str = "") -> list[dict]:
    """Busca vacantes por texto libre (título, empresa, stack) y ciudad."""
    q, loc = query.lower(), location.lower()
    return [
        v for v in VACANTES
        if (not q or q in json.dumps(v, ensure_ascii=False).lower())
        and (not loc or loc in v["ciudad"].lower())
    ]


@mcp.tool
def get_job(job_id: str) -> dict:
    """Detalle completo de una vacante por su id."""
    for v in VACANTES:
        if v["id"] == job_id:
            return v
    return {"error": f"no existe la vacante {job_id}"}


if __name__ == "__main__":
    mcp.run()  # stdio por default
