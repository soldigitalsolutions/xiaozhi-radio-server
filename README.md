# Xiaozhi Radio Relay Server (ESP32-S3)

Servidor proxy y transcodificador de audio en tiempo real diseñado para expandir las capacidades multimedia del firmware **Xiaozhi AI** en placas **ESP32-S3**.

## ¿Qué problema resuelve?
Las emisoras de radio en internet transmiten en múltiples formatos y contenedores (AAC, MP3, redirecciones HTTP) que superan la capacidad de decodificación nativa del ESP32-S3. Este servidor recibe cualquier flujo en vivo y lo convierte al vuelo mediante **FFmpeg** a **Ogg/Opus (48 kbps, mono)**, entregando un stream ligero y estable listo para reproducirse en el dispositivo.

## Arquitectura y Tecnologías
* **Backend:** Python + Flask + Gunicorn
* **Procesamiento de audio:** FFmpeg (`libopus`)
* **Contenedor:** Docker (`python:3.10-slim`)
* **Despliegue:** Render

## Endpoints disponibles
* `GET /`: Verifica que el servidor esté activo (usado también para monitoreo *keep-alive*).
* `GET /stream/<radio_id>`: Inicia la transcodificación en vivo de la emisora configurada en `app.py`.

## Notas de Despliegue y Rendimiento (Render)
* **Plan Gratuito (Free Tier):** El servicio entra en suspensión tras 15 minutos de inactividad para ahorrar recursos, lo que genera un retraso inicial (*cold start* de ~30-50 segundos) al encender la radio por primera vez. *(Tip: Se puede mitigar configurando un ping HTTP cada 10 minutos a la ruta raíz `/` mediante servicios gratuitos como cron-job.org o UptimeRobot).*
* **Plan de Pago / Instancia Dedicada:** Permite mantener el contenedor activo de forma continua sin suspensiones, logrando una reproducción instantánea y mayor fluidez en el cambio de emisoras.
