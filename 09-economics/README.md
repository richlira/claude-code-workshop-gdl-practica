# 09 · Token economics: el fan-out barato

Sección del deck: "Haiku brilla en subagents, no sustituyendo al lead."

## Ejercicio · Fan-out con model: haiku (10 min)

El repo trae `.claude/agents/explorador.md` con `model: haiku` y tools de lectura.

1. Abre `claude` en la raíz y pide:
   > Lanza 3 exploradores en paralelo: uno para apps/pagos, uno para 06-mcp
   > y uno para .claude/. Cada uno me regresa SOLO su mapa y hallazgos.
2. Observa en la UI cómo delega (agentes con contexto propio) y qué regresa:
   conclusiones, no file dumps.
3. Ahora pregunta al lead algo que exija criterio sobre lo que regresó:
   > Con esos mapas, ¿qué refactor de apps/pagos harías primero y por qué?

**Qué acabas de hacer:** lectura mecánica en el modelo barato (fan-out), juicio en
el modelo grande (lead). El main no se ensució con los archivos leídos.

## Las 5 caveman rules (slide 80)

1. Un modelo por sesión.
2. Haiku para el fan-out, no para el lead.
3. /clear al cambiar de tarea, /compact temprano.
4. El contexto es el costo: menos MCP servers, CLAUDE.md podado.
5. Mide wall-clock, no tokens.

Pega estas 5 en tu monitor y ya amortizaste el workshop.
