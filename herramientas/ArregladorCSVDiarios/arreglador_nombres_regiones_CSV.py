## Este script no es necesario usarlo despu√©s del 01 de Abril de 2020 

"""
Hoy 03 de Abril tenemos el problema de que tenemos distintos formatos para los nombres de las Regiones
A partir de ahora este es el formato:
    * CON espacio entre las palabras
    * OHiggins se escribe sin apÛstrofe
    * Nuble se escribe sin —
    * Magallanes queda asÌ no m·s
    
Arica y Parinacota
Tarapaca
Antofagasta
Atacama
Coquimbo
Valparaiso
Metropolitana
OHiggins
Maule
Nuble
Biobio
Araucania
Los Rios
Los Lagos
Aysen
Magallanes

"""

import numpy as np
import pandas as pd
import datetime
from datetime import timedelta, date

#Directorio de los informes diarios en CSV que queremos arreglar
path='../../informes_minsal/informes_diarios_Region_CSV/'
formato_archivo='-InformeDiarioRegion-COVID19.csv'

###
##Queremos arreglar desde el 02 de Marzo al 01 de Abril
## Para pasar fecha a datetime
## datetime = pd.to_datetime('2020-03-01')
## Para pasar datetime a fecha en string
## fecha string datetime.strftime('%Y-%m-%d')


#definimos primero una funci√≥n para tener un rango de todas las fechas entre medio
#es un rango inverso pues va de la fecha m√°s reciente a la menos reciente
def rango_fechas_inverso(start_date, end_date):
    for n in range(int ((fecha_final - fecha_inicial).days)):
        yield fecha_final - timedelta(n)


fecha_inicial=pd.to_datetime('2020-03-01')
fecha_final=pd.to_datetime('2020-04-06')
        
for fecha in rango_fechas_inverso(fecha_inicial-timedelta(1), fecha_final):
    #Fecha Hoy en string: fecha.strftime("%Y-%m-%d")
    #Fecha Ayer en string: (fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    #Abrimos el CSV de Hoy
    stringHoy=fecha.strftime("%Y-%m-%d")
    stringAyer=(fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    informeHoy = pd.read_csv(path+stringHoy+formato_archivo)
    informeHoy = informeHoy.replace('LosRios','Los Rios')
    informeHoy = informeHoy.replace('Ohiggins','OHiggins')
    informeHoy = informeHoy.replace('LosLagos','Los Lagos')
    informeHoy = informeHoy.replace('Vaparaiso','Valparaiso')
    
    informeHoy.to_csv(path+stringHoy+formato_archivo, index=False)
    