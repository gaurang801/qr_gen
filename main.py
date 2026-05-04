from flask import Flask, render_template, request, send_file
import qrcode
import io
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate_qr")
def generate_qr():
    url = request.args.get('url')
    transparent = request.args.get('transparent', 'false')

    if not url:
        return "URL is required", 400

    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Transparent vs normal QR
    if transparent == "true":
        img = qr.make_image(
            fill_color="black",
            back_color="transparent"
        ).convert("RGBA")
    else:
        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


# ✅ IMPORTANT: Render compatible PORT fix
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
