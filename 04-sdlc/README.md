# 04 · El playbook SDLC: artefactos que viajan

Sección del deck: "Cada etapa termina escribiendo un artefacto a version control.
La siguiente empieza leyéndolo."

## Ejercicio · intent → spec → plan → diff (20 min)

Vas a recorrer las primeras etapas del SDLC AI-native con una feature de verdad,
commiteando el artefacto de cada etapa.

1. **Plan.** Lee `intent.md`: es el pedido tal como lo escribió "negocio".
   Commitéalo tal cual: `git add intent.md && git commit -m "intent: recibos por whatsapp"`.
2. **Design.** Abre `claude` y pídele:
   > Lee 04-sdlc/intent.md y escribe 04-sdlc/spec.md: requirements concretos,
   > casos borde, y qué queda explícitamente fuera. Hazme las preguntas que
   > negocio dejó abiertas antes de escribir.
   Contesta sus preguntas (esa conversación ES la etapa de design). Commitea `spec.md`.
3. **Build, primera mitad.** Entra a plan mode (Shift+Tab dos veces) y pídele el plan
   de implementación sobre `../apps/pagos/`. Guarda el resultado como `plan.md` y commitéalo.
4. **Build, segunda mitad.** Aprueba el plan y deja que implemente. El diff es el
   4º artefacto: revísalo ANTES de commitear (tú eres el gate).

**El punto:** cada etapa empezó leyendo el artefacto de la anterior. Eso es context
engineering a nivel de proceso: la siguiente sesión no necesita la conversación
anterior, necesita el artefacto.

**Bonus separation of duties:** antes del commit final, corre `@security-reviewer
audita el diff` y anota qué encontró. El agente que escribió el código no lo aprueba.
