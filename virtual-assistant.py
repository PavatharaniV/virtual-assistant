import speech_recognition as sp
import pyttsx3 as t
import datetime 
import pywhatkit
import wikipedia as wi


listner = sp.Recognizer()
engine = t.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmnd():
    try:
        with sp.Microphone() as mic:
            print("listening.....")
            voice = listner.listen(mic)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'hey assistant' in command:
                print(command) 
    except:
        pass
    return command

def assistant():
    command = take_cmnd()
    print(command)
    if 'play' in command:
        output = command.replace('play','')
        talk('playing '+output)
        pywhatkit.playonyt(output)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %P')
        talk('Current time is '+time)
    elif 'what is' in command:
        res = command.replace('what is','')
        info = wi.summary(res,1)
        talk(info)
    elif 'who is' in command:
        res = command.replace('who is','')
        info = wi.summary(res,1)
        talk(info)
    else:
        talk('Please repeat')

while True:
    assistant()
