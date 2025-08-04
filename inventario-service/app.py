from flask import Flask, jsonify
from db import init_db, get_connection
import threading
from consumer import start_consumer
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
init_db()

@app.route('/inventario')
def inventario():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nombre, stock FROM platos")
            datos = cur.fetchall()
            return jsonify([{ "plato": d[0], "stock": d[1] } for d in datos])

# Hilo para escuchar eventos
threading.Thread(target=start_consumer, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('FLASK_PORT', 5001)))
