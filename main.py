from flask import Flask, render_template, request, send_file
import qrcode
import io
import os
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- QR GENERATOR ----------------
@app.route("/generate_qr")
def generate_qr():
    url = request.args.get("url")
    transparent = request.args.get("transparent", "false")

    if not url:
        return "URL is required", 400

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2
    )

    qr.add_data(url)
    qr.make(fit=True)

    # QR image generate
    if transparent == "true":
        img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    else:
        img = qr.make_image(fill_color="black", back_color="white")

    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")


# ---------------- RENDER FIX ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
