#Auth :  said magdy 
#This is a current working prototype.

#*****************************************************************
#*** I will enhance it every day, adding features periodically ***
#*****************************************************************

from gtts import gTTS
import os
import playsound
import speech_recognition as sr
from alexa_features import *      #our own features

LANG="ar"

#here we play the speach from the user 
def Alexa_Speak(text,language=LANG):
    tts=gTTS(text=text,lang=language)
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3",True)
    os.remove("Speech.mp3")


#here make alexa listen to user
def Alexa_Listen():
    """
    Listens for speech input, recognizes the command, and returns the recognized text.
    
    Returns:
        str: The recognized speech command, or an empty string if an error occurs.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("KeyWords You can use : [ ما هو , ما هي , ابحثي عن , كلميني عن , من هو , شغلي , افتحي ]")
            print("Listening...")
            audio = recognizer.listen(source)
            
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language=LANG)
        print(f"Recognized command: {command}")
        return command
    
    except sr.UnknownValueError:
        Alexa_Speak("عذرا لم أفهمك")  
        return ""
    
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""



def Run_Alexa():
    finish=True
    while finish:
        command=Alexa_Listen()
        if ("شكرا" in command) | ("باي" in command) | ("مع السلامه" in command) | ("سلام" in command):
            finish=False
        elif ("الساعه" in command) | ("الوقت" in command):
            Alexa_Speak(".الساعة الان."+get_time())
        elif "تاريخ" in command:
            Alexa_Speak(".تاريخ اليوم هو."+get_date())
        elif ("ما هو" in command) | ("ما هي" in command)| ("عندي سؤال" in command) | ("ابحثي عن" in command):
            Alexa_Speak(google_it(command))
        elif ("من هو" in command) | ("من هي" in command)| ("كلميني عن" in command):
           Alexa_Speak(ask_about(command))
        elif ("اغنيه" in command) | ("موسيقى"  in command) | ("سوره" in command) | ("صوره" in command) | ("فيديو" in command) | ("على يوتيوب" in command) | ("افتحي" in command) | ("شغلي" in command):
            Alexa_Speak(on_YouTube(command)) 
            
       
    Alexa_Speak("مع السلامة")

Run_Alexa()

