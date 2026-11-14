# Xiaozhi Radio Relay Server (ESP32-S3)

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Gunicorn-000000?style=flat&logo=flask&logoColor=white)
![FFmpeg](https://img.shields.io/badge/Audio-FFmpeg%20%7C%20Opus-007808?style=flat&logo=ffmpeg&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Apoyar%20Proyecto-FF5E5B?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/soldigitalsolutions)

Servidor proxy y transcodificador de audio en tiempo real diseñado para expandir las capacidades multimedia del firmware **Xiaozhi AI** en placas **ESP32-S3**.

---

## ¿Qué problema resuelve?

Las emisoras de radio por internet transmiten en múltiples formatos, códecs y contenedores (`AAC`, `MP3`, redirecciones `HTTP/HTTPS`) que superan la capacidad de decodificación nativa o la memoria disponible del **ESP32-S3**. 

Este servidor recibe cualquier flujo de audio en vivo y lo transcodifica al vuelo mediante **FFmpeg** a **Ogg/Opus (48 kbps, mono)**, entregando un stream ligero, uniforme y estable listo para reproducirse directamente en el dispositivo.

---

## Arquitectura y Tecnologías

* **Backend:** Python 3.10 + Flask + Gunicorn
* **Procesamiento de audio:** FFmpeg (`libopus`)
* **Contenedor:** Docker (`python:3.10-slim`)
* **Despliegue:** Render

---

## Endpoints Disponibles

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Verifica que el servidor esté activo (utilizado también para monitoreo *keep-alive*). |
| `GET` | `/stream/<radio_id>` | Inicia la transcodificación en vivo a Ogg/Opus de la emisora configurada en `app.py`. |

---

## Notas de Despliegue y Rendimiento (Render)

* **Plan Gratuito (Free Tier):** El servicio entra en suspensión tras 15 minutos de inactividad para ahorrar recursos, lo que genera un retraso inicial (*cold start* de ~30–50 segundos) al encender la radio por primera vez. *(Tip: Puedes mitigar esto configurando un ping HTTP cada 10 minutos a la ruta raíz `/` mediante servicios gratuitos como cron-job.org o UptimeRobot).*
* **Instancia Dedicada / Plan de Pago:** Permite mantener el contenedor activo de forma continua sin suspensiones, logrando una reproducción instantánea y mayor fluidez en el cambio de emisoras.

---

## Apoyo al Proyecto y Contacto

Actualmente esta instancia pública se mantiene sobre infraestructura gratuita y desarrollo independiente. Si este servidor te resultó útil para tu placa **ESP32-S3** o quieres apoyar el desarrollo continuo de herramientas abiertas con IA, Python y robótica:

[![Apoya en Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/soldigitalsolutions)

* **Página de apoyo (Ko-fi):** [ko-fi.com/soldigitalsolutions](https://ko-fi.com/soldigitalsolutions)
* **Contacto directo / Patrocinio de tokens de IA (OpenRouter / Claude):** `soldigitalsolutions@gmail.com`
* **Desarrollado por:** [Sol Digital Solutions by EPamar](https://github.com/soldigitalsolutions)
