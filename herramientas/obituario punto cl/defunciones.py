from bs4 import BeautifulSoup
import pandas
import datetime
import requests

#COMENTARIOS DEL TRABAJO, SE HACE UN REPLACE
#
								#
#
                                        #

#
                                    #

## LOGICA DE EXTRACCION, LOOK FOR :
# col-lg-12  , DIV CLASS
# H6 ID  _condolencia_   ...TEXT
# A CLASS search-link    ...TEXT

counter=0
quotes=[]

### https://obituario.cl/?page=870
while True:
    URL= "https://obituario.cl/?page="+str(counter)
    counter=counter+1
    r = requests.get(URL, verify=False)
    soup = BeautifulSoup(r.content, from_encoding="utf-8")
    contenido = soup.findAll("div", {"class": "search-result"})
    #if contenido == []:
    if contenido == []:
        break
    for row in contenido:
        quote = {}
        #print(str(row).split(" |")[0].split("<h6>")[1])
        quote['FechaDefuncion'] = str(row).split(" |")[0].split("<h6>")[1].replace("\r","").replace("\n","").replace("\t","")
        #print(row.find("a", attrs={'class': 'search-link'}).text)
        quote['Nombre'] = row.find("a", attrs={'class': 'search-link'}).text.replace("\r","").replace("\n","").replace("\t","").replace("                                        ","").replace("                                    ","")
        quote['Texto'] = (str(row).split("</p>")[0].split("<p>")[1]).replace("\r","").replace("\n","").replace("\t","")
        #print(quote['Texto'])
        #quote['Date'] = str(datetime.datetime.today().strftime('%d-%m-%Y'))
        #quote['Hora'] = str(datetime.datetime.today().strftime("%H:%M:%S"))
        quotes.append(quote)

pd = pandas.DataFrame(quotes)
pd.to_csv("Obituario-"+str(datetime.datetime.today().strftime('%d-%m-%Y'))+".csv", mode='a', header=False)
