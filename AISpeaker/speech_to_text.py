import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Start")
    audio = r.listen(source) # 마이크로부터 음성 듣기
    

try:
    text = r.recognize_google(audio, language = 'en-US')
    print(text)
except sr.UnknownValueError:
    print("Error")
except sr.RequestError as e:
    print("요청 실패 : {0}".format(e)) # API key error or network error
    