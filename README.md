# Claude Code Workshop · Guadalajara · La práctica

Repo de ejercicios del workshop (Wizeline · 29 ago 2026 · Claude Community México).
Cada carpeta corresponde a una sección del deck y trae 1-2 ejercicios para practicar
por tu cuenta.

**Empieza aquí → abre [`guia/index.html`](guia/index.html) en tu navegador.**
Es el mapa visual de todos los ejercicios. O navega las carpetas: cada una trae su README.

## Requisitos

- **Claude Code** instalado y con sesión iniciada (`claude` en tu terminal)
- **jq** (lo usan los hooks): `brew install jq` / `sudo apt install jq`
- **Python 3.10+** solo para los ejercicios 05 (Agent SDK) y 06 (MCP)
- Git

## Importante antes de empezar

1. Al abrir `claude` por primera vez en este repo te va a pedir **confiar en el folder
   y revisar sus hooks**. Léelos (viven en `.claude/settings.json`) y acepta: ese
   trust dialog es parte de la lección de la sección 08.
2. **Todo lo "sensible" de este repo es falso**: el `.env`, las keys en el código,
   las vacantes. Son utilería para practicar.
3. Este repo es, él mismo, un ejemplo de context engineering: CLAUDE.md corto con
   pointers, un CLAUDE.md de subdirectorio, rules con scope por paths, skills,
   subagents y hooks. Espulga `.claude/` con confianza.

## Mapa (mismo orden que el deck)

| Carpeta | Sección del deck | Practicas |
|---|---|---|
| `03-conceptos/` | Conceptos · context engineering | El test de poda de CLAUDE.md · /clear vs /compact |
| `04-sdlc/` | El playbook SDLC AI-native | intent → spec → plan → diff con artefactos commiteados |
| `05-landscape/` | El landscape | Claude Agent SDK: el harness embebido en Python |
| `06-mcp/` | Proyectos · MCP | Tu propio MCP server con FastMCP en ~30 líneas |
| `07-primitivas/` | Primitivas · steering | Rules con paths · crear una skill desde cero |
| `08-practica/` | Práctica | Las 3 demos del taller: hook vs flag · subagent · skill |
| `09-economics/` | Token economics | Fan-out con `model: haiku` en subagents |
| `10-cowork/` | Code vs Cowork | El mismo análisis, sin terminal (para no-devs) |
| `11-insights/` | 5 insights | El combo `isolation: worktree` + `model: haiku` |

Las secciones 1 y 2 del deck (comunidad y momentum) no se practican: se viven en
[claudecommunity.mx](https://claudecommunity.mx).

## Licencia

MIT. Úsalo, fórkealo, llévalo a tu equipo.

Proyecto de la Claude Community México. No es material oficial de Anthropic.
