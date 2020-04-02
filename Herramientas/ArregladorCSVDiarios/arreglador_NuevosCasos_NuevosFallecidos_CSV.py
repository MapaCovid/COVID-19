## Este script no es necesario usarlo después del 01 de Abril de 2020 

"""
Se realiza este script para construir las columnas "casos_nuevos" y 
"fallecidos_nuevos", sólo para los informes diarios previos (e incluído) al 
01 de Abril. Esto porque el minsal antes del 25 de marzo no indicaba los 
"casos nuevos", sino que solo los casos totales. Lo mismo para los fallecidos, 
y hasta el 01 de Abril no se estaban calculando los nuevos fallecidos al 
importar los datos.

La gracia es que a partir de ahora (desde el 02 de abril en adelante), al 
generar el informe diario en CSV se calculen automáticamente los 
fallecidos_nuevos sin tener que arreglar después 
los informes (los casos_nuevos ahora los está publicando directamtne el minsal.)
"""

import numpy as np
import pandas as pd
import datetime
from datetime import timedelta, date

#Directorio de los informes diarios en CSV que queremos arreglar
path='../../informes_minsal/informes_diarios_CSV/'
formato_archivo='-InformeDiarioRegion-COVID19.csv'

###
##Queremos arreglar desde el 02 de Marzo al 01 de Abril
## Para pasar fecha a datetime
## datetime = pd.to_datetime('2020-03-01')
## Para pasar datetime a fecha en string
## fecha string datetime.strftime('%Y-%m-%d')


#definimos primero una función para tener un rango de todas las fechas entre medio
#es un rango inverso pues va de la fecha más reciente a la menos reciente
def rango_fechas_inverso(start_date, end_date):
    for n in range(int ((fecha_final - fecha_inicial).days)):
        yield fecha_final - timedelta(n)


fecha_inicial=pd.to_datetime('2020-03-02')
fecha_final=pd.to_datetime('2020-04-01')
        
for fecha in rango_fechas_inverso(fecha_inicial-timedelta(1), fecha_final):
    #Fecha Hoy en string: fecha.strftime("%Y-%m-%d")
    #Fecha Ayer en string: (fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    #Abrimos el CSV de Hoy
    stringHoy=fecha.strftime("%Y-%m-%d")
    stringAyer=(fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    informeHoy = pd.read_csv(path+stringHoy+formato_archivo)
    informeAyer= pd.read_csv(path+stringAyer+formato_archivo)
    
    informeHoy['casos_nuevos']=(informeHoy.casos_totales-informeAyer.casos_totales)
    informeHoy['fallecidos_nuevos']=(informeHoy.fallecidos_totales-informeAyer.fallecidos_totales)
    
    #actualizamos el CSV de Hoy
    informeHoy.to_csv(path+stringHoy+formato_archivo)
    