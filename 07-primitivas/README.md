# 07 · Primitivas: rules con scope y tu primera skill

Sección del deck: "Política inviolable → hook. Playbook repetible → skill.
Expertise aislada → subagent. Distribución → plugin. El porqué → CLAUDE.md."

## Ejercicio 1 · Dispara una rule path-scoped (10 min)

Este repo trae `.claude/rules/pagos.md` con `paths: apps/pagos/**`: solo entra al
contexto cuando tocas ese módulo.

1. Abre `claude` en la raíz y pide:
   > Agrega a apps/pagos/app.py una función descuento(monto, porcentaje)
2. Observa el resultado: debería llegar en **centavos enteros** (no float) y sin
   imprimir tarjetas completas, porque la rule entró al contexto al tocar la carpeta.
3. Ahora pide algo FUERA de pagos (ej. un cambio en 06-mcp/jobs_server.py) y
   nota que esas reglas no estorbaron ahí.

**El punto:** contexto quirúrgico. La regla existe solo cuando aplica.

## Ejercicio 2 · Crea una skill desde cero (10 min)

El repo ya trae `/rubric-review` como ejemplo. Ahora la tuya:

1. Pídele a Claude:
   > Crea .claude/skills/release-notes/SKILL.md: una skill que lea los commits
   > desde el último tag (o los últimos 5 commits) y escriba release notes con
   > secciones Features / Fixes / Breaking, tono para cliente final.
2. Revisa el archivo generado: frontmatter con name y description, cuerpo = playbook.
3. Úsala al instante: `/release-notes`
4. Bonus: ¿cuándo se cargó su cuerpo al contexto? (Pista: progressive disclosure,
   slide 52 del deck.)

## Ejercicio 3 (bonus) · Un subagent nuevo

Copia el patrón de `.claude/agents/explorador.md` y crea `docs-writer.md` con
`tools: Read, Grep, Glob, Write` y `model: sonnet`, que documente módulos en
`docs/`. Pruébalo con `@docs-writer documenta apps/pagos`.
