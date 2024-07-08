#our features 
import datetime
from bs4 import BeautifulSoup
import requests

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%A %d/%m/%Y")

def google_it(command):
    command=command.replace("اليكسا"," ")
    #command=command.replace("ما هو"," ")
    command=command.replace("ابحثي عن"," ")
    command=command.strip()
    #url="https://www.google.com/search?q="+command
    url = "https://www.google.com/search?q=%D9%85%D8%A7+%D9%87%D9%88+%D8%B7%D9%88%D9%84+%D8%B1%D9%88%D9%86%D8%A7%D9%84%D8%AF%D9%88&rlz=1C1ASVC_arEG948EG949&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyDwgFEC4YJxjHARjqAhjRAzIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkyMzk3ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8"
    it=requests.get(url)

    soup=BeautifulSoup(it.content,'html.parser')

    height_element = soup.find("div", {"class": "Z0LcW"})
    if height_element:
        height = height_element.text
        print(f"Cristiano Ronaldo's height: {height}")
    else:
        print(soup.find("body").text)

        
    #response=soup.find("body").text
    # response=soup.find("div",class_="GyAeWb").text
    # print(response)