from faster_whisper import WhisperModel
import os

model = WhisperModel("small")

audio_folder = "../Indian_Languages_Audio_Dataset/Gujarati/wav"

out = open("labels.csv", "w", encoding="utf-8")
out.write("path,text\n")

for file in os.listdir(audio_folder):
    if file.endswith(".wav"):
        path = os.path.join(audio_folder, file)
        segments, _ = model.transcribe(path, language="gu")

        text = " ".join([s.text for s in segments]).strip()
        out.write(f"{path},{text}\n")
        print(file, "->", text)

out.close()
print("Gujarati labels.csv created")
