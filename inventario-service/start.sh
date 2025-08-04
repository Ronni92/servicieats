#!/bin/bash
echo "🚀 Iniciando inventario-service (Flask + Consumer)"
python app.py &    # Lanza Flask en segundo plano
python consumer.py # Lanza el consumidor en primer plano
