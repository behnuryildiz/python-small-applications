from gtts import gTTS
import os

text = input ("Type the text that you want to revert to the MP3 format:\n")
language = "en"  #for English: en || Turkish: tr || German: de || Spanish: es

speech = gTTS(text= text, lang= language, slow= False)
speech.save("./fromWrite_toSpeech/revertedText.mp3")
os.system("start ./fromWrite_toSpeech/revertedText.mp3")