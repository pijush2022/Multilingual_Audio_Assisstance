from setuptools import find_packages, setup

setup(
    name="AI Assistant for Multilingual Support 🌐",
    version="0.1",
    author="Pijush",
    author_email="pijushpl2023@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)