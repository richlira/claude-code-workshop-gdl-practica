---
name: rubric-review
description: Code review con el rubric del equipo. Úsala cuando pidan revisar un archivo o un diff.
---

Revisa $ARGUMENTS con este rubric, 0 a 2 puntos cada criterio:

1. **Correctness** · ¿hace lo que promete? ¿casos borde?
2. **Seguridad** · ¿secretos, inyección, validación de inputs?
3. **Legibilidad** · ¿nombres claros, funciones cortas?
4. **Tests** · ¿happy path y al menos un error cubiertos?
5. **Simplicidad** · ¿hay código que sobra?

Entrega:
- Tabla con el puntaje por criterio y total sobre 10
- Los 3 hallazgos más importantes, priorizados, con archivo:línea
- El fix concreto de cada hallazgo

No modifiques archivos: esto es un review, no un fix.
