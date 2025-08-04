const express = require('express');
const amqp = require('amqplib');
const app = express();

app.use(express.json());

let canal = null;
let conexion = null;

async function conectarRabbitMQ() {
  const RABBITMQ_URL = 'amqp://rabbitmq';

  try {
    conexion = await amqp.connect(RABBITMQ_URL);
    canal = await conexion.createChannel();
    await canal.assertQueue('pedido_creado', { durable: true });
    console.log('✅ Conectado a RabbitMQ desde pedido-service');

    // Manejar cierres inesperados
    conexion.on('close', () => {
      console.error('⚠️ Conexión a RabbitMQ cerrada. Reintentando...');
      canal = null;
      setTimeout(conectarRabbitMQ, 5000); // Reintento en 5s
    });

    conexion.on('error', err => {
      console.error('❌ Error en RabbitMQ:', err.message);
    });

  } catch (error) {
    console.error('❌ Error al conectar a RabbitMQ:', error.message);
    setTimeout(conectarRabbitMQ, 5000); // Reintento en 5s
  }
}

app.post('/pedido', async (req, res) => {
  const { cliente, plato, cantidad } = req.body;

  if (!cliente || !plato || !cantidad) {
    return res.status(400).json({ mensaje: 'Datos incompletos del pedido' });
  }

  if (!canal) {
    return res.status(503).json({ mensaje: 'Canal RabbitMQ no disponible. Intente más tarde.' });
  }

  const pedido = { cliente, plato, cantidad: parseInt(cantidad) };

  try {
    canal.sendToQueue('pedido_creado', Buffer.from(JSON.stringify(pedido)));
    console.log('📤 Pedido enviado a RabbitMQ:', pedido);
    res.json({ mensaje: `Pedido recibido: ${cantidad} x ${plato} para ${cliente}` });
  } catch (error) {
    console.error('❌ Error enviando pedido a RabbitMQ:', error.message);
    res.status(500).json({ mensaje: 'Error interno al procesar el pedido' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`🚀 Pedido-service escuchando en puerto ${PORT}`);
  conectarRabbitMQ(); // Intentar conexión al iniciar
});
