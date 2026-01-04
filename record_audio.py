import sounddevice as sd
import soundfile as sf

FILENAME = "live_audio.wav"
SAMPLERATE = 16000   # good for speech + Whisper
SECONDS = 10         # change recording length as needed

print("🎙️ Recording... speak now!")
audio = sd.rec(int(SECONDS * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
sd.wait()

sf.write(FILENAME, audio, SAMPLERATE)

print(f"✅ Saved recording as {FILENAME}")
