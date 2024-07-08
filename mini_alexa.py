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
    #os.system("S.mp3")
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
            print("Listening...")
            audio = recognizer.listen(source)
            
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language=LANG)
        print(f"Recognized command: {command}")
        return command
    
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# listener=sr.Recognizer()
# def Alexa_Listen():
#     try:
#         with sr.Microphone() as mic:
#             speech=listener.listen(mic)
#             command=listener.recognize_google_cloud(speech,language=LANG)
#             print(command)
#             #Alexa_Speak(command)
#             return command
#     except:
#         Alexa_Speak("عذرا لم أفهمك")  
#         return;  

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
           
    Alexa_Speak("مع السلامة")

Run_Alexa()
#Alexa_Speak(".تاريخ اليوم هو."+get_date())
#Alexa_Listen()
#google_it("اليكسا ما هو طول رونالدو")