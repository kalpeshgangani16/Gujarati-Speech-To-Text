from flask import Flask, request, jsonify
from transcribe_gujarati  import transcribe_gujarati   # ✅ make sure filename is transcribe.py
import os

app = Flask(__name__)

UPLOAD_FILE = "input.wav"


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Gujarati Speech-to-Text API is running"
    })


@app.route("/transcribe", methods=["POST"])
def transcribe():
    print("➡️ Request received")

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio = request.files["file"]
    audio.save(UPLOAD_FILE)

    print("Saved file size:", os.path.getsize(UPLOAD_FILE))

    try:
        whisper_text, corrected_text, whisper_wer = transcribe_gujarati(UPLOAD_FILE)

        response = {
            "success": True,
            "whisper_text": whisper_text,
            "corrected_text": corrected_text,
            "whisper_wer": round(whisper_wer, 4)
        }

    except Exception as e:
        response = {
            "success": False,
            "error": str(e)
        }

    finally:
        if os.path.exists(UPLOAD_FILE):
            os.remove(UPLOAD_FILE)

    return jsonify(response)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )