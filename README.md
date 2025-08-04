# 🍽️ Mini-UberEats – Sistema Distribuido de Pedidos

Este proyecto es un sistema distribuido básico que simula una aplicación de pedidos en línea estilo UberEats. Está compuesto por microservicios que se comunican mediante eventos (RabbitMQ), expuestos a través de APIs REST, desplegados con Docker y orquestados por Docker Compose. El frontend se sirve mediante NGINX.

---

## 🚀 Tecnologías utilizadas

| Categoría              | Herramienta                             |
|------------------------|-----------------------------------------|
| Lenguajes              | Node.js (pedido-service), Python (inventario-service) |
| Contenedores           | Docker                                  |
| Orquestación           | Docker Compose                          |
| Infraestructura        | Docker + EC2 (opcional con Terraform)   |
| Comunicación           | RabbitMQ (Event Driven Architecture)    |
| Base de datos          | PostgreSQL                              |
| Frontend               | HTML + Bootstrap + JavaScript (con NGINX) |
| DevOps (opcional)      | GitHub Actions (para CI/CD)             |
| Monitoreo (opcional)   | Prometheus + Grafana                    |

---

## 📦 Estructura del proyecto


---

## 🔧 Servicios incluidos

| Servicio            | Puerto | Función Principal                             |
|---------------------|--------|-----------------------------------------------|
| pedido-service      | 3000   | Recibe pedidos (POST /pedido) y publica evento |
| inventario-service  | 5000   | Escucha eventos y descuenta stock (GET /inventario) |
| RabbitMQ            | 15672  | Broker de mensajes, UI en puerto 15672         |
| PostgreSQL          | 5432   | Base de datos para el inventario              |
| Frontend (NGINX)    | 8080   | Servidor web con HTML estático                |

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone 
cd mini-ubereats

👨‍💻 Autores
Tu Priscila Chisag – Estudiante de Ingeniería en Sistemas 

Contacto: pvchisag@uce.edu.ec

crear docker ec2
#!/bin/bash
# Actualiza la instancia
yum update -y

# Instala Docker
amazon-linux-extras install docker -y
yum install -y docker

# Inicia Docker
systemctl start docker
systemctl enable docker
