# 05 · El landscape: el harness embebido (Claude Agent SDK)

Sección del deck: "Para embeber ya no reconstruyes el harness: lo importas."

## Ejercicio · Tu primer agente embebido (15 min)

`triage_agent.py` usa el **Claude Agent SDK**: el mismo harness de Claude Code
(loop, tools, permisos) como librería de Python.

```bash
cd 05-landscape
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python triage_agent.py
```

Requisitos: tener Claude Code instalado y logueado (el SDK usa esa misma sesión).

Qué observar:
1. El agente **lee el repo con tools reales** (Read/Grep/Glob) sin que tú
   implementaras ninguna: venían en el harness.
2. `allowed_tools` restringe qué puede tocar: es de solo lectura por diseño.
3. Cambia el `prompt` y vuelve a correr: ya tienes un agente embebible en
   cualquier servicio o cron tuyo.

## Reto opcional · dynamic workflows

Si tu cuenta tiene acceso, abre `claude` en la raíz del repo y pide:
> use a workflow: revisa apps/pagos con 3 dimensiones (seguridad, correctness,
> estilo) en paralelo y verifica cada hallazgo con un agente distinto

Observa el script de orquestación que Claude escribe antes de correrlo. Eso que
antes era tu framework, ahora es un artefacto generado.
