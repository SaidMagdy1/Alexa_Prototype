#our features 
import datetime
from bs4 import BeautifulSoup
import requests
import pywhatkit
import wikipedia
import pyjokes
from googletrans import Translator, constants

LANG="ar"
wikipedia.set_lang(LANG) 
header={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
  }
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%A %d/%m/%Y")


def google_it(command):
    command=command.replace("اليكسا"," ")
    command=command.replace("ابحثي عن"," ")
    command=command.replace("عندي سؤال", " ")
    command=command.strip()
    print(command)
    url="https://www.google.com/search?q="+command
    it=requests.get(url,headers=header)

    soup=BeautifulSoup(it.content,'lxml')
     
    response=soup.find('div',class_="HwtpBd gsrt PZPZlf kTOYnf")
    if response:
        return response.text
    else:
        return ("عذرا لم أفهمك")

def ask_about(command):
    command = command.replace("كلميني عن", "")
    command = command.replace("من هو", "")  
    command = command.replace("من هي", "")       
    command = command.replace("اليكسا", "")  
    command=command.strip()  
    print(command)
    response = wikipedia.summary(command,1)
    if response:
        return response
    else:
        return ("عذرا لم أفهمك")


def on_YouTube(command):
    command = command.replace("اليكسا", "") 
    command = command.replace("اغنيه", "")
    command = command.replace("موسيقى", "")  
    command = command.replace("سوره", "")       
    command = command.replace("صوره" , "")  
    command = command.replace("فيديو" , "")       
    command = command.replace("على يوتيوب" , "") 
    command = command.replace("افتحي" , "")       
    command = command.replace("شغلي" , "") 
    command=command.strip()  
    response="حاضر ها هي" + command       
    pywhatkit.playonyt(command)
    return response