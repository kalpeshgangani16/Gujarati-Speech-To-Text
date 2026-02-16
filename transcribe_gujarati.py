import whisper
from PreProcessing import reduce_noise
import os
import jiwer
from ground_truth import GROUND_TRUTH_TEXT

# Load model ONCE
model = whisper.load_model("large-v3")


def calculate_wer(truth: str, hypothesis: str) -> float:
    truth = truth.strip()
    hypothesis = hypothesis.strip()
    return jiwer.wer(truth, hypothesis)


def transcribe_gujarati(input_audio_path: str) -> str:
    clean_audio = "clean_audio.wav"

    reduce_noise(input_audio_path, clean_audio)

    result = model.transcribe(
        clean_audio,
        language="gu",
        task="transcribe",
        fp16=False,
        temperature=0.2,
        no_speech_threshold=0.6,
        logprob_threshold=-1.0,
        condition_on_previous_text=False
    )

    predicted_text = result["text"]

    if os.path.exists(clean_audio):
        os.remove(clean_audio)

    wer = calculate_wer(GROUND_TRUTH_TEXT, predicted_text)

    print(f"Transcription WER: {wer:.2%}")

    return predicted_text
