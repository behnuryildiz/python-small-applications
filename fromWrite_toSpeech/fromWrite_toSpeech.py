from gtts import gTTS
import os

#test = "deneme yazisini buraya yaz" veya
text = input ("MP3 formatinda dönüstürmek istedigin texti buraya yazar misin ?\n")

language = "tr"

speech = gTTS(text= text, lang= language, slow= False)

speech.save("text.mp3")

os.system("start text.mp3")