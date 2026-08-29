# 11 · Insights: el combo que casi nadie configura

Sección del deck: "isolation: worktree + model: haiku, en el frontmatter del subagent."

## Ejercicio · Subagent aislado y barato (15 min)

1. Crea `.claude/agents/refactorizador.md`:

   ```markdown
   ---
   name: refactorizador
   description: Aplica refactors mecánicos de forma aislada, sin tocar tu working tree.
   tools: Read, Edit, Write, Grep, Glob, Bash
   model: haiku
   isolation: worktree
   ---

   Aplica el refactor pedido con cambios mínimos. No reformatees archivos
   completos. Reporta qué archivos tocaste y por qué.
   ```

2. Asegúrate de tener el repo en git (si lo clonaste, ya está) y pide:
   > @refactorizador renombra la función cobrar() de apps/pagos a cobrar_mxn()
   > actualizando todos sus usos
3. Observa: el subagent trabaja en un **worktree propio** (tu working tree queda
   intacto mientras tanto) y con **haiku** (el refactor mecánico no necesita al lead).
4. Revisa el resultado como un diff más: tú decides si entra.

## Verifica tú mismo el insight 1

Con el flag `--dangerously-skip-permissions` activo, el hook de este repo sigue
bloqueando `.env` (ejercicio 08). No nos creas: compruébalo. Esa es la diferencia
entre una instrucción y una pared.

## Y el insight 5

Pídele a Claude Code: "¿qué hay en tu memoria de este proyecto?" La memoria de
Code vive en archivos por proyecto, aparte de la de Chat/Cowork, a propósito.
