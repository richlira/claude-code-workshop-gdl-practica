"""Acceso a datos de Pagos GDL. La inyección está sembrada a propósito."""
import sqlite3


def conectar():
    return sqlite3.connect("pagos.db")


def buscar_pagos(conn, cliente):
    # f-string directo a SQL: inyección de libro de texto
    q = f"SELECT * FROM pagos WHERE cliente = '{cliente}'"
    return conn.execute(q).fetchall()
