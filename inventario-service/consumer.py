import pika
import json
from db import get_connection
import time

def callback(ch, method, properties, body):
    try:
        pedido = json.loads(body)
        plato = pedido.get('plato')
        cantidad = int(pedido.get('cantidad', 0))

        print(f"📥 Pedido recibido: {cantidad} x {plato}")

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT stock FROM platos WHERE nombre = %s", (plato,))
        stock_actual = cur.fetchone()[0]

        if stock_actual >= cantidad:
                cur.execute("UPDATE platos SET stock = stock - %s WHERE nombre = %s", (cantidad, plato))
                conn.commit()
                print(f"✅ Stock actualizado para {plato}")
        else:
                print(f"❌ Stock insuficiente para {plato}. Disponible: {stock_actual}, Requerido: {cantidad}")

def start_consumer():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            channel = connection.channel()
            channel.queue_declare(queue='pedido_creado',durable=True)
            channel.basic_consume(queue='pedido_creado', on_message_callback=callback, auto_ack=True)
            print('🔄 Esperando mensajes en "pedido_creado"...')
            channel.start_consuming()

        except Exception as e:
            print(f"❌ Error conectando a RabbitMQ: {e}")
            print("🔁 Reintentando conexión en 5 segundos...")
            time.sleep(5)

if __name__ == '__main__':
    start_consumer()
