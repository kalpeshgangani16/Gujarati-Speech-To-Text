import whisper

# Load model
model = whisper.load_model("large-v3")

# Transcribe + translate to English
# result = model.transcribe(
#     "live_audio.wav",
#     task="translate",   # 🔥 THIS converts Gujarati → English
#     fp16=False,
#     temperature=0.0
# )
result = model.transcribe(
    "live_audio.wav",
    language="gu",
    task="transcribe",
    fp16=False,
    temperature=0.0,
    no_speech_threshold=0.6,
    logprob_threshold=-1.0,
    condition_on_previous_text=False,
    initial_prompt="આ સ્પષ્ટ અને શુદ્ધ ગુજરાતી ભાષા છે."
)

# result = model.transcribe(
#     "gujarati_voice.wav",
#     language="gu",
#     task="transcribe",
#     fp16=False
# )


english_text = result["text"]

# Print on screen
print("English Text:")
print(english_text)

# Write English text into file
with open("output_gujarati.txt", "w", encoding="utf-8") as f:
    f.write(english_text)

print("\n✅ English text saved to output_english.txt")
