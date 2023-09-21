from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit

Listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_cmd():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print('Running command')

    except:
        pass
    return command


def run_alexa():
    command = take_cmd()
    print('Running command')

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing...' + song)
        pywhatkit.playonly(song)


run_alexa()
