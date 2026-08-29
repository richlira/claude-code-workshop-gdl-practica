---
paths:
  - "apps/pagos/**"
---

- Todo monto se maneja en centavos, como entero. Jamás float para dinero.
- Nunca loguear ni imprimir un número de tarjeta completo: enmascara con `****` + últimos 4.
- SQL siempre con parámetros preparados, jamás f-strings.
- Errores de pago se loguean y se reportan; jamás `except: pass`.
