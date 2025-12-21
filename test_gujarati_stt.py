import whisper

model = whisper.load_model("small")   # IMPORTANT: small or medium

result = model.transcribe(
    "live_audio.wav",
    language="gu",              # FORCE Gujarati
    task="transcribe",          # NOT translate
    fp16=False,
    initial_prompt="આ ગુજરાતી ભાષા છે"
)

print("OUTPUT:")
print(result["text"])
