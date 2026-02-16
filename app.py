from flask import Flask, request, jsonify
from transcribe_gujarati import transcribe_gujarati
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Gujarati Speech-to-Text API is running"

@app.route("/transcribe", methods=["POST"])
def transcribe():
    print("➡️ Request received")
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio = request.files["file"]
    input_path = "input.wav"
    audio.save(input_path)

    try:
        text = transcribe_gujarati(input_path)
    finally:
        if os.path.exists(input_path):
            os.remove(input_path)

    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

