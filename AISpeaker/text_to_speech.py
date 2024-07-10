from gtts import gTTS
from playsound import playsound

# English
# text = 'Can I help you?'
file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)


# playsound(file_name) #mp3 file 재생

# Korean
# text = '파이썬을 배우면 이런것도 할 수 있어요'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name)

# Long sentence(파일에서 불러오기)
with open('sample.txt','r') as f:
    text = f.read()
    
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)


playsound(file_name) #mp3 file 재생