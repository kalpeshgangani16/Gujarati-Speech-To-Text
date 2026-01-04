import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from scipy.signal import resample

# BEST mic (WASAPI)
sd.default.device = 9

record_fs = 48000   # Mic supported rate
target_fs = 16000   # Whisper required rate
seconds = 8

print("🎙️ Speak clearly in Gujarati (full sentences)...")

audio = sd.rec(
    int(seconds * record_fs),
    samplerate=record_fs,
    channels=1,
    dtype="int16"
)
sd.wait()

# Convert to float for resampling
audio_float = audio.astype(np.float32)

# Resample to 16kHz
num_samples = int(len(audio_float) * target_fs / record_fs)
audio_16k = resample(audio_float, num_samples)

# Convert back to int16
audio_16k = audio_16k.astype(np.int16)

write("live_audio.wav", target_fs, audio_16k)

print("✅ Audio recorded at 48kHz and saved as 16kHz (live_audio.wav)")
