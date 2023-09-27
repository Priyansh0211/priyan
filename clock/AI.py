import os
from platformdirs import sys 
import pyttsx3
import speech_recognition as sr 
import webbrowser
def speak(text):
    engine = pyttsx3.init()
    voices = engine.setProperty('voices')
    engine.setProperty('voices',voices[2])
    engine.setProperty('rate',160)
    engine.say(text)
    engine.runAndWait()

t = Translator()
r = sr.Recognizer()
speak("हेलो मेरा नाम अजय है.बताइया में आपकी क्या मदद कर सकता हूं")
while True:
      with sr.Microphone() as sources:
          speak("आपकी आवाज सुनी जा रही है")
          print("Listening your voice.....")
          audio = r.listen(source)
    try:
       command = r.recognize_google(audio,language='hi-IN')
       speak("आपने कहा:" + command)
       translated = t.translate(command,dest='en')
       if "youtube" in translated.lower():
               speak("youtube.com खोला जा रहा है")
               print("opening youtube.com...")
               webbrowser.open("https://www.youtube.com/")
       elif"whatsapp" in translated.lower():
               speak("व्हाट्सएप खोला जा रहा है")
               print("opening whatsapp...")
               webbrowser.open("https://whatsapp.com")
       elif"close" in translated.lower():
               speak("प्रोग्राम बंद किया जा रहा है")
               print("stopping program....")
               sys.exit()\
      except sr.UnknownValueError:
               speak("मैं आपकी आवाज समझ नहीं पा रहा हूं। कृपया दोबारा बोलें")
               print("Unrecognized Voice. say that again please.")         
