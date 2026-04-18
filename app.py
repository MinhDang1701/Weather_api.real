from flask import Flask, jsonify, request
from flask_cors import CORS
import urllib.request
import json

app = Flask(__name__)
CORS(app)

API_KEY = "9a10d08fdd33490a891141504260304"

@app.route("/weather")
def weather():
    try:
        # 📍 Lấy GPS từ mobile
        lat = request.args.get("lat")
        lon = request.args.get("lon")

        if not lat or not lon:
            return jsonify({
                "error": "Missing lat/lon"
            }), 400

        # 🌤️ Gọi API REAL-TIME
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&lang=vi"

        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read())

        # 🔥 TRẢ NGUYÊN FORMAT (KHÔNG ĐỤNG GÌ)
        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)