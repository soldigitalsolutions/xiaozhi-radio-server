import subprocess
from flask import Flask, Response, abort

app = Flask(__name__)

# Catálogo de emisoras: puedes agregar más siguiendo este mismo formato
RADIOS = {
    "olimpica-barranquilla": (
        "https://master.letio.com/io/?gs=9102&type=live.mp3"
    ),
    "la-reina": (
        "https://playerservices.streamtheworld.com/api/livestream-redirect/RNA_BARRANQUILLAAAC.aac"
    ),
    # "nombre-de-otra-emisora": "https://url-de-la-radio.mp3",
}


@app.route("/")
def index():
  return (
      "Servidor Relay de Radio Activo. Usa /stream/nombre-de-la-emisora"
  )


@app.route("/stream/<radio_id>")
def stream(radio_id):
  # Verificamos si la emisora existe en la lista
  if radio_id not in RADIOS:
    return abort(404, description="Emisora no encontrada")

  radio_url = RADIOS[radio_id]

  def generate():
    cmd = [
        "ffmpeg",
        "-i",
        radio_url,
        "-acodec",
        "libopus",
        "-b:a",
        "48k",
        "-ac",
        "1",
        "-f",
        "ogg",
        "pipe:1",
    ]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    )
    try:
      while True:
        chunk = process.stdout.read(4096)
        if not chunk:
          break
        yield chunk
    finally:
      process.terminate()

  return Response(generate(), mimetype="audio/ogg")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
