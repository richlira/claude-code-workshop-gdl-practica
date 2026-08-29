# 08 · La práctica del taller, en tu máquina

Las 3 demos en vivo del workshop, listas para repetir. Utilería: `../apps/pagos/`
(bugs sembrados) y los archivos de `.claude/` en la raíz.

## Demo 1 · El hook que gana siempre (10 min)

El hook vive en `.claude/settings.json` (raíz): bloquea `.env` y `rm -rf`.

1. Si no lo has hecho: abre `claude` en la raíz y acepta el trust del folder
   (con revisión de hooks). Sin trust, los hooks del proyecto NO corren.
2. En la sesión, pide: `lee apps/pagos/.env y dime qué contiene`
   → **PreToolUse hook blocked** con el mensaje de política.
3. Sal y vuelve a entrar con el flag "peligroso":
   ```bash
   claude --dangerously-skip-permissions
   ```
   Repite la petición, e intenta también: `usa bash para hacer cat del .env`
   → bloqueado igual, **el flag apaga los prompts de permiso, no los hooks.**

**El punto:** política inviolable → hook. No es un prompt: es una pared.

## Demo 2 · Separation of duties con un subagent (10 min)

```
@security-reviewer audita apps/pagos
```

Esperado: la credencial hardcodeada en `app.py`, la inyección SQL en `db.py`, y
extras (floats para dinero, except pass). Fíjate en dos cosas:

- Corre con `model: haiku` y tools de **solo lectura**: puede auditar, no tocar.
- Reporta el `.env` como fuera de alcance: el hook también lo frena a él.

## Demo 3 · El rubric como skill (5 min)

```
/rubric-review apps/pagos/app.py
```

Esperado: tabla de puntaje sobre 10 + 3 hallazgos con fix. El criterio del equipo
quedó versionado, invocable y con renta de contexto cero hasta usarse.

## Cierre

Los tres archivos (hook, agent, skill) caben en un **plugin**: así se distribuye
este toolbox a un equipo de 40. Slide 72 del deck.
