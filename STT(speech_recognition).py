'''
# STT

- 참고 사이트

    https://ai-creator.tistory.com/59

    https://pypi.org/project/SpeechRecognition/

- Installation

    pip install SpeechRecognition

    pip install pyaudio

'''

import speech_recognition as sr
def STT(Language):
    # 음성이 인식될 때까지 반복
    while(True): 
        # 녹음중...
        Record = sr.Recognizer()
        with sr.Microphone() as source:
            Audio = Record.listen(source)
        # 소리를 텍스트로 변환 시도
        try:
            Input_Text = Record.recognize_google(Audio, language=Language)
            return Input_Text
        
        except sr.UnknownValueError: continue
            # 음성 인식 오류 (빈 음성)
        except sr.RequestError: continue
            # 구글서버와 통신 오류

STT('ko-KR')