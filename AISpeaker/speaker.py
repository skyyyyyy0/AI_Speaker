import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (listen)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = 'en-US')
        print('[User] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError as e:
        print("요청 실패 : {0}".format(e)) # API key error or network error

# Answer
def answer(input_text):
    answer_text = ''
    if 'Hi' in input_text:
        answer_text = 'Hi. Nice to meet you.'
    elif 'Weather' in input_text:
        answer_text = 'The weather is sunny. The degree is 90.'
    elif 'Thank' in input_text: 
        answer_text = 'You\'re welcome'
    elif 'End' in input_text:
        answer_text = 'See you later'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = 'Could you speak again?'
    speak(answer_text)

# 컴퓨터가 소리내어 읽기(TTS)
def speak(text):
    print("[AI speaking] " + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='en-US')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()


speak("How can I help you?")
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)