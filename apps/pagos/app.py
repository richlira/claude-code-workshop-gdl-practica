"""Pagos GDL · app de juguete para los ejercicios 07, 08 y 09.

Los problemas de este archivo están sembrados A PROPÓSITO:
no los arregles salvo que un ejercicio lo pida.
"""

API_KEY = "demo-live-a1b2c3d4e5f6g7h8"  # credencial falsa, sembrada para la demo


def cobrar(monto, tarjeta):
    total = monto * 1.16  # IVA en float: pérdida de centavos garantizada
    print("cobrando", total, "a", tarjeta)
    return total


def procesar_lote(pagos):
    resultados = []
    for p in pagos:
        try:
            resultados.append(cobrar(p["monto"], p["tarjeta"]))
        except Exception:
            pass  # los errores se van al limbo, nadie se entera
    return resultados


if __name__ == "__main__":
    procesar_lote([
        {"monto": 420.0, "tarjeta": "4242-4242-4242-4242"},
        {"monto": 99.9, "tarjeta": "5555-5555-5555-4444"},
    ])
