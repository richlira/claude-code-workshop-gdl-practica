"""Agente de triage embebido con el Claude Agent SDK.

El mismo harness de Claude Code (loop, tools, permisos) como librería.
Requiere Claude Code instalado y con sesión iniciada: pip install claude-agent-sdk
"""
import anyio
from claude_agent_sdk import ClaudeAgentOptions, query


async def main():
    options = ClaudeAgentOptions(
        system_prompt=(
            "Eres el reviewer del equipo de pagos. Reporta hallazgos "
            "accionables con archivo:línea y severidad. En español."
        ),
        allowed_tools=["Read", "Grep", "Glob"],
        permission_mode="default",
        cwd="..",  # el repo completo, desde 05-landscape/
    )
    async for message in query(
        prompt="Audita apps/pagos y dame tus 3 hallazgos principales",
        options=options,
    ):
        print(message)


if __name__ == "__main__":
    anyio.run(main)
