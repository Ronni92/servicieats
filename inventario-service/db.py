import psycopg2
import os

# Obtener variables de entorno con valores por defecto para facilitar pruebas locales
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'pedidosdb')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'postegres01')

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        print("❌ Error conectando a la base de datos:", e)
        raise

def init_db():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS platos (
                        id SERIAL PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        stock INTEGER NOT NULL
                    );
                """)
                conn.commit()
                print("✅ Tabla 'platos' verificada/creada")
    except Exception as e:
        print("❌ Error inicializando la base de datos:", e)

def descontar_stock(plato, cantidad):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT stock FROM platos WHERE nombre = %s", (plato,))
                fila = cur.fetchone()
                if not fila:
                    print(f"❌ Plato '{plato}' no encontrado.")
                    return False
                stock_actual = fila[0]
                if stock_actual < cantidad:
                    print(f"⚠️ Stock insuficiente para '{plato}'. Stock actual: {stock_actual}")
                    return False
                nuevo_stock = stock_actual - cantidad
                cur.execute("UPDATE platos SET stock = %s WHERE nombre = %s", (nuevo_stock, plato))
                conn.commit()
                print(f"✅ Stock actualizado: {plato} → {nuevo_stock}")
                return True
    except Exception as e:
        print(f"❌ Error al descontar stock para {plato}:", e)
        return False
