import requests
import re
from bs4 import BeautifulSoup

def hello():
    print("hello")

def monthTextToNumber(monthText):

        if monthText == "enero":
            return "01"
        elif monthText == "febrero":
            return "02"
        elif monthText == "marzo":
            return "03"
        elif monthText == "abril":
            return "04"
        elif monthText == "mayo":
            return "05"
        elif monthText == "junio":
            return "06"
        elif monthText == "julio":
            return "07"
        elif monthText == "agosto":
            return "08"
        elif monthText == "septiembre":
            return "09"
        elif monthText == "octubre":
            return "10"
        elif monthText == "noviembre":
            return "11"
        elif monthText == "diciembre":
            return "12"
        else: 
            return "ERROR-EMAIL-FORMAT"
        
def getCurrentDay(day):
    if(int(day) < 10):
        return "0"+str(day)
    else: 
        return str(day)
    
    
def getDay():
    page = requests.get("https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('div',class_="contenido")[0]   
    currentDayPage = list(table.children)[3]
    currentDate = re.search(r'^\*[A-Za-z\s]*(\d+)\s*\w*\s(\w*)\s*\w*\s*(\d*)',currentDayPage.get_text())
    currentMonth = monthTextToNumber(currentDate.group(2))
    currentDay = getCurrentDay(currentDate.group(1))
    today = currentDate.group(3) + "-" +currentMonth +"-" + currentDay
    return today

       