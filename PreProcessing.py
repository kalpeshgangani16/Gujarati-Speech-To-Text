import librosa
import noisereduce as nr
import soundfile as sf


def reduce_noise(input_audio, output_audio):
    print("🧹 Preprocessing audio...")


    # Load audio
    y, sr = librosa.load(input_audio, sr=None)


    # Take first 1 sec as noise reference
    noise_sample = y[:int(sr * 1.0)]


    # Reduce noise
    reduced_audio = nr.reduce_noise(
        y=y,
        sr=sr,
        y_noise=noise_sample,
        stationary=False
    )


    # Save cleaned audio
    sf.write(output_audio, reduced_audio, sr)


    print("✅ Clean audio saved as", output_audio)


