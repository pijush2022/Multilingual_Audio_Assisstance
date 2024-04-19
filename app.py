import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("AI Assistant for Multilingual Support 🌐")
    
    if st.button("Feel free to inquire about anything"):
        with st.spinner("Listening..."):
            text=voice_input()
            response=llm_model_object(text)
            text_to_speech(response)
            
            
            audio_file=open("sepp.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="sepp.mp3",
                               mime="audio/mp3")
            
if __name__=='__main__':
    main()
