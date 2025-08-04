const amqp = require('amqplib');

async function publishPedido(pedido) {
  const conn = await amqp.connect(process.env.RABBIT_URL);
  const channel = await conn.createChannel();
  const queue = 'pedido_creado';

  await channel.assertQueue(queue, { durable: true });
  channel.sendToQueue(queue, Buffer.from(JSON.stringify(pedido)));

  console.log('📤 Pedido enviado a RabbitMQ:', pedido);

  setTimeout(() => {
    channel.close();
    conn.close();
  }, 500);
}

module.exports = { publishPedido };
