
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def conectar():
    """Abre una conexión con la base de datos local."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3307")),
        database=os.getenv("DB_NAME", "social_market_radar"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        connection_timeout=5,
    )


def probar_conexion():
    conexion = None
    cursor = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT simbolo, empresa FROM activos ORDER BY id"
        )

        activos = cursor.fetchall()

        print("Conexion exitosa con Social Market Radar")
        print("-" * 45)

        for simbolo, empresa in activos:
            print(f"{simbolo:8} | {empresa}")

        print("-" * 45)
        print(f"Total de activos: {len(activos)}")

    except mysql.connector.Error as error:
        print(f"Error de base de datos: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if conexion is not None and conexion.is_connected():
            conexion.close()


if __name__ == "__main__":
    probar_conexion()
