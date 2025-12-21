import streamlit as st
import whisper

model = whisper.load_model("base")

st.title("Gujarati Speech-to-Text")

audio_file = st.file_uploader("Upload Gujarati Audio")

if audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    result = model.transcribe("temp.wav", language="gu")
    st.write(result["text"])
