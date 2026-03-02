import whisper
import requests
from PreProcessing import reduce_noise
import os
import jiwer
from ground_truth import GROUND_TRUTH_TEXT

# Load Whisper model ONCE
model = whisper.load_model("large-v3")


def normalize_text(text: str) -> str:
    transform = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemovePunctuation(),
        jiwer.Strip(),
        jiwer.RemoveMultipleSpaces()
    ])
    return transform(text)


def calculate_wer(truth: str, hypothesis: str) -> float:
    truth_clean = normalize_text(truth)
    hypothesis_clean = normalize_text(hypothesis)
    return jiwer.wer(truth_clean, hypothesis_clean)


def transcribe_gujarati(input_audio_path: str):

    # 🔹 OPTIONAL: disable preprocessing if harming quality
    clean_audio = input_audio_path
    # reduce_noise(input_audio_path, "clean_audio.wav")
    # clean_audio = "clean_audio.wav"

    print("🎙 Transcribing with Whisper...")

    result = model.transcribe(
        clean_audio,
        language="gu",
        task="transcribe",
        fp16=False,
        temperature=0.0,
        beam_size=5,
        best_of=5,
        condition_on_previous_text=False
    )


    print("Audio file exists:", os.path.exists(input_audio_path))
    print("Audio file size:", os.path.getsize(input_audio_path))

    whisper_text = result["text"].strip()
    print("Whisper Output:", whisper_text)

    # 🔹 Calculate WER ONLY on Whisper output
    whisper_wer = calculate_wer(GROUND_TRUTH_TEXT, whisper_text)
    print(f"Whisper WER: {whisper_wer:.2%}")

    # 🔹 Send to Smruti for readability improvement
    corrected_text = whisper_text

    try:
        print("📡 Sending to Smruti API...")
        print("Sentence sent to Smruti:", whisper_text)

        response = requests.post(
            "https://vrund1346-smruti-gujarati-grammar-checker.hf.space/correct",
            json={"sentence": whisper_text},
            headers={"Content-Type": "application/json"},
            timeout=20
        )

        print("Smruti Status Code:", response.status_code)
        print("Smruti Raw Response:", response.text)

        if response.status_code == 200:
            data = response.json()
            corrected_text = data.get("corrected_text", whisper_text)
            print("Smruti Output:", corrected_text)

        else:
            print("Smruti API error:", response.status_code)

    except Exception as e:
        print("Smruti API failed:", e)

    return whisper_text, corrected_text, whisper_wer