import whisper
import os

print("Current directory:", os.getcwd())

model = whisper.load_model("base")

result = model.transcribe(
    "live_audio.wav",
    language="gu",
    fp16=False
)

print("Gujarati Text:")
print(result["text"])
