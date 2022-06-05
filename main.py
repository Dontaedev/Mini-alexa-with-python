from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

####     PYTHON TEXT TO SPEECH SET UP ######

Listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


####   THE ENTRY, WAIT UNTIL YOU SEE LISTENING THE SAY YOUR COMMAND ########  

def take_command():
    try:
            
        with sr.Microphone() as source:
            talk("what can i do for you today")
            print("listening...")
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")
                print(command)
  
    except:
          pass
         

    return command

#### TO PLAY A SONG ON YOUTUBE SAY ALEXA (PLAY) *SONG NAME* ######
#  REMEMBER TO SAY THE WORD PLAY BEFORE THE SONG NAME SO ALEXA KNOWS WHAT YOU ARE TALKING

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    

######    ASK ALEXA WHAT TIME IS IT ########

    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M")
        print(time)
        talk("the current time is ", + time)


#####            ASK ALEXA ABOUT A PERSON BY ASKING WHO IS *PERSON*  ###########

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


#####       ASK ALEXA TO TELL YOU A JOKE BY SAYING TELL ME A JOKE   #########


    elif "joke" in command:
        talk(pyjokes.get_joke())


####           TELL ALEXA GOOD MORNING    ########


    elif "good morning" in command:
        talk("Good morning, hope you are doing well today")


#####     DONT'T TRY TO ROAST ALEXA LOL  #########
    elif "you're ugly" in command:
        talk("thanks, i try my best to look like you today")


#####     TELL ALEXA THAT YOU ARE SAD  #####

    elif "sad" in command:
        talk("cheer up, bettter and happier times is coming")
   
##       IF ALEXA DIDN'T GET WHAT YOU SAID  ######## 
    else:
        talk("sorry, i don't understand could you repeat")
        return run_alexa

    


run_alexa()


def launch_app(path_of_app):
    try:
        subprocess.call([path_of_app])
        return True
    except Exception as e:
        print(e)
        return False