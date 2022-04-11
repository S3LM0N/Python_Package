'''
# KoNLPy (Okt)

- 참고 사이트

    https://datascienceschool.net/03%20machine%20learning/03.01.02%20KoNLPy%20%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%B2%98%EB%A6%AC%20%ED%8C%A8%ED%82%A4%EC%A7%80.html

    https://github.com/open-korean-text/open-korean-text

- Installation

    pip install SpeechRecognition

    pip install pyaudio

'''
from konlpy.tag import Okt

def Analysis(Text):
    Text_Km = '"{}"'.format(Text)
    okt = Okt()
    Input_Text_Normalize = okt.normalize(Text_Km)
    Input_Text_Pos_Array = okt.pos(Input_Text_Normalize)
    Input_Text_Pos_Array_Lenth = len(Input_Text_Pos_Array)

    Analysis_Verb_List = []
    Analysis_Noun_List = []
    Analysis_Adjective_List = []

    while(Input_Text_Pos_Array_Lenth > 0):
        Input_Text_Pos_Array_Lenth = Input_Text_Pos_Array_Lenth - 1
        
        if (Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][1] == "Verb") :
            Analysis_Verb_List.append(Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][0])
        if (Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][1] == "Noun") :
            Analysis_Noun_List.append(Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][0])
        if (Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][1] == "Adjective") :
            Analysis_Adjective_List.append(Input_Text_Pos_Array[Input_Text_Pos_Array_Lenth][0])

    
    Analysis_Output = [Input_Text_Normalize, Input_Text_Pos_Array, Analysis_Verb_List, Analysis_Noun_List, Analysis_Adjective_List, len(Input_Text_Pos_Array)]

    return Analysis_Output
'''
    * RETURN
   Analysis_Output [0] - 정규화된 문장
   Analysis_Output [1] - 정렬되지 않은 요소들
   Analysis_Output [2] - 동사 리스트
   Analysis_Output [3] - 명사 리스트
   Analysis_Output [4] - 형용사 리스트
   Analysis_Output [5] - 요소 개수
'''