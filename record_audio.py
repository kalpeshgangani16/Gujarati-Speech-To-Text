import sounddevice as sd
sd.default.device = 1   # <-- IMPORTANT (your mic)
from scipy.io.wavfile import write

fs = 16000        # Sample rate (Whisper needs 16kHz)
seconds = 5       # Recording duration

print("🎙️ Speak Gujarati now...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("live_audio.wav", fs, audio)
print("✅ Audio saved as live_audio.wav")
