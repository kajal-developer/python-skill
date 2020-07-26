# requires pyaudio and pyspeech
#pip install speechrecognition
#pip install gTTS
#pip install pygame
#while running code will take time as it consist of online services
import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time 
import os
from gtts import gTTS
import pygame
from pygame import mixer

from threadpoolctl import threadpool_info

def speak(audioString):
    global x
    b=audioString
    if len(b)==0:#do nothing
        #w1=Label(root,text="no input!").pack()
        return
    tts=gTTS(text=b,lang='en-us')
    tts.save("voice%s.mp3"%(x))
    #x+=1
    pygame.init()
    pygame.display.set_mode((2,1))
    mixer.music.load("voice%s.mp3"%(x))
    mixer.music.play(0)
    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recognizeSpeech():
    #record audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak...")
        audio=r.listen(source)
        print("heard...waiting for google to recognize audio")
    #speech recognition using google speech recognition
    data=""

    try:
        data=r.recognize_google(audio)
        print("you said :"+data)
    except sr.UnknownValueError:
        print("Google speech recognition could not understand  audio")
    except sr.RequestError as e:
        print("could not request results from google speech recognition service;{0}".format(e))
    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on nitesh, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    else :
        speak(",,,,,,,I did not get what you said !")





x=0
print("Starting Program..")
speak("Hi! Ted, what can I do for you?")
recognizedText = recognizeSpeech() # DO speech recognition
## data = "what time is it"
jarvis(recognizedText) ## Process the text
speak("Turning off the program.")
print("Run complete")


       





    