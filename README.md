# Xiaozhi Radio Relay Server (ESP32-S3)

Servidor proxy y transcodificador de audio en tiempo real diseñado para expandir las capacidades multimedia del firmware **Xiaozhi AI** en placas **ESP32-S3**.

## ¿Qué problema resuelve?
Las emisoras de radio en internet transmiten en múltiples formatos y contenedores (AAC, MP3, redirecciones HTTP) que superan la capacidad de decodificación nativa del ESP32-S3. Este servidor recibe cualquier flujo en vivo y lo convierte al vuelo mediante **FFmpeg** a **Ogg/Opus (48 kbps, mono)**, entregando un stream ligero y estable listo para reproducirse en el dispositivo.

## Arquitectura y Tecnologías
* **Backend:** Python + Flask + Gunicorn
* **Procesamiento de audio:** FFmpeg (`libopus`)
* **Despliegue:** Contenedor Docker alojado en Render
