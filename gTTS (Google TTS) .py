'''
# TTS

- 참고 사이트

    https://pypi.org/project/gTTS/

    https://pypi.org/project/SpeechRecognition/

- Installation

    pip install gTTS

'''
from gtts import gTTS   
from playsound import playsound

def TTS(Text, Language):
    tts = gTTS(text=Text, lang=Language)
    tts.save("TTS.mp3")
    playsound("TTS.mp3")   

TTS("안녕하세요",'ko')