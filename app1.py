import streamlit as st
from gtts import gTTS
import io

def generate_audio(text):
    # Generate audio from text
    tts = gTTS(text)
    with io.BytesIO() as audio_file:
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file.read()

def main():
    st.title("ReadItV1")

    uploaded_file = st.file_uploader("Choose a file", type=["txt"])

    if uploaded_file is not None:
        # Read file content
        stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
        text_content = stringio.read()

        # Display file content
        st.text_area("File Content", text_content, height=300)

        if st.button("Read Aloud"):
            # Generate audio from text
            audio_data = generate_audio(text_content)

            # Display audio player
            st.audio(audio_data, format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
