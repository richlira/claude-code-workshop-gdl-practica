# 03 · Conceptos: context engineering en tus manos

Sección del deck: "El modelo no falló. El contexto sí."

## Ejercicio 1 · El test de poda (10 min)

`CLAUDE-inflado.md` es un CLAUDE.md real-ista de 70+ líneas: mezcla reglas vitales,
obviedades, instrucciones muertas y contradicciones. Como en el paper de agosto 2026
(arXiv 2608.11095): creció +226% y nadie se atrevió a borrar.

1. Abre `claude` en esta carpeta y pídele:
   > Aplica el test "would removing this cause mistakes?" a CLAUDE-inflado.md,
   > línea por línea. Proponme la versión podada (target: menos de 25 líneas)
   > y para cada línea que sobreviva, agrégale su PORQUÉ en una frase.
2. Discute con Claude 2-3 líneas donde no estés de acuerdo.
3. Compara: ¿cuánto contexto pagabas por sesión antes vs después?

**El punto:** el porqué no es cortesía. En el paper, documentar la razón elimina
el 99.3% del exceso, porque vuelve borrable la instrucción.

## Ejercicio 2 · /clear vs /compact, sentido en vivo (5 min)

1. En una sesión, pide algo pequeño sobre `../apps/pagos/app.py` (ej. "explícame cobrar()").
2. Corre `/compact` y observa el resumen: la conversación sigue, la historia pesa menos.
3. Ahora corre `/clear` y pregunta "¿de qué hablábamos?": no hay historia, pero
   CLAUDE.md y rules regresaron frescos.

**El punto:** /compact = misma tarea, sesión larga. /clear = tarea nueva; la historia
de la anterior es poison para la siguiente.
