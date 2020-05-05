## Este script no es necesario usarlo despuÃ©s del 01 de Abril de 2020 

"""
Se realiza este script para reconstruir los informes diarios por Regiones
Entre el 29 de Abril y 04 Mayo (por cambio de formato no logramos generarlo)


Luego se arregla formato para todos los informes anteriores
"""

import numpy as np
import pandas as pd
import datetime
from datetime import timedelta, date

#Directorio de los informes diarios en CSV que queremos arreglar
path_informes='../../datos/informes_diarios_regiones/'
formato_archivo='-InformeDiarioRegiones-COVID19.csv'


path_informes_WM='../../fuentes/White-Mask/Database/csv/Dataset diarios/'
formato_archivo_WM='Casos_COVID-19_Chile_'

###
##Queremos recuperar desde el 29 de Abril al 04 mayo
## Para pasar fecha a datetime
## datetime = pd.to_datetime('2020-03-01')
## Para pasar datetime a fecha en string
## fecha string datetime.strftime('%Y-%m-%d')


#definimos primero una funciÃ³n para tener un rango de todas las fechas entre medio
#es un rango inverso pues va de la fecha mÃ¡s reciente a la menos reciente
def rango_fechas_inverso(fecha_inicial, fecha_final):
    for n in range(int ((fecha_final - fecha_inicial).days)):
        yield fecha_final - timedelta(n)

def rango_fechas(fecha_inicial, fecha_final):
    for n in range(int ((fecha_final - fecha_inicial).days)):
        yield fecha_inicial + timedelta(n)

fecha_inicial=pd.to_datetime('2020-04-29')
fecha_final=pd.to_datetime('2020-05-04')
        
for fecha in rango_fechas(fecha_inicial, fecha_final+ timedelta(1)):
    print(fecha)
    #Fecha Hoy en string: fecha.strftime("%Y-%m-%d")
    #Fecha Ayer en string: (fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    #Abrimos el CSV de Hoy
    stringHoy=fecha.strftime("%Y-%m-%d")
    stringAyer=(fecha-timedelta(1)).strftime("%Y-%m-%d")
    
    #Hoy desde White Mask
    informeHoy = pd.read_csv(path_informes_WM+formato_archivo_WM+stringHoy+'.csv')
    
    #Ayer desde lo nuestro
    informeAyer= pd.read_csv(path_informes+stringAyer+formato_archivo)
    
    
    informeHoy=informeHoy.rename(columns={'Región':'nombre_region',
                              'Casos nuevos con síntomas':'casos_nuevos_sintomas',
                              'Casos nuevos sin síntomas*':'casos_nuevos_nosintomas',
                              'Casos nuevos sin síntomas':'casos_nuevos_nosintomas',     
                              'Casos totales acumulados':'casos_totales',
                              'Fallecidos':'fallecidos_totales'})
    
    informeHoy['casos_nuevos']=(informeHoy.casos_totales-informeAyer.casos_totales)
    informeHoy['fallecidos_nuevos']=(informeHoy.fallecidos_totales-informeAyer.fallecidos_totales)
    
    informeHoy['id_region']=0

    informeHoy.loc[informeHoy.nombre_region=='Arica y Parinacota','id_region']=15
    informeHoy.loc[informeHoy.nombre_region=='Tarapacá','id_region']=1
    informeHoy.loc[informeHoy.nombre_region=='Antofagasta','id_region']=2
    informeHoy.loc[informeHoy.nombre_region=='Atacama','id_region']=3
    informeHoy.loc[informeHoy.nombre_region=='Coquimbo','id_region']=4
    informeHoy.loc[informeHoy.nombre_region=='Valparaíso','id_region']=5
    informeHoy.loc[informeHoy.nombre_region=='Metropolitana','id_region']=13
    informeHoy.loc[informeHoy.nombre_region=='O’Higgins','id_region']=6
    informeHoy.loc[informeHoy.nombre_region=='Maule','id_region']=7
    informeHoy.loc[informeHoy.nombre_region=='Ñuble','id_region']=16
    informeHoy.loc[informeHoy.nombre_region=='Biobío','id_region']=8
    informeHoy.loc[informeHoy.nombre_region=='Araucanía','id_region']=9
    informeHoy.loc[informeHoy.nombre_region=='Los Ríos','id_region']=14
    informeHoy.loc[informeHoy.nombre_region=='Los Lagos','id_region']=10
    informeHoy.loc[informeHoy.nombre_region=='Aysén','id_region']=11
    informeHoy.loc[informeHoy.nombre_region=='Magallanes','id_region']=12
    
    informeHoy['recuperados_nuevos']=0
    informeHoy['recuperados_totales']= 0
    
    informeHoy=informeHoy[['id_region',
                       'nombre_region',
                       'casos_totales',
                       'casos_nuevos',
                       'casos_nuevos_sintomas',
                       'casos_nuevos_nosintomas',
                       'fallecidos_totales',
                       'fallecidos_nuevos',
                       'recuperados_totales',
                       'recuperados_nuevos']]
    
    informeHoy.to_csv(path_informes+stringHoy+formato_archivo, index=False)
    
#Arreglo formato anterior:
fecha_inicial=pd.to_datetime('2020-03-03')
fecha_final=pd.to_datetime('2020-05-04')
        
for fecha in rango_fechas(fecha_inicial, fecha_final+ timedelta(1)):
    print(fecha)
    stringHoy=fecha.strftime("%Y-%m-%d")
    informeHoy = pd.read_csv(path_informes+stringHoy+formato_archivo)
    
    informeHoy=informeHoy.rename(columns={'id_reg':'id_region',
                               'nombre_reg':'nombre_region'})
    
    
    informeHoy.loc[informeHoy.id_region==15,'nombre_region']='Arica y Parinacota'
    informeHoy.loc[informeHoy.id_region==1,'nombre_region']='Tarapacá'
    informeHoy.loc[informeHoy.id_region==2,'nombre_region']='Antofagasta'
    informeHoy.loc[informeHoy.id_region==3,'nombre_region']='Atacama'
    informeHoy.loc[informeHoy.id_region==4,'nombre_region']='Coquimbo'
    informeHoy.loc[informeHoy.id_region==5,'nombre_region']='Valparaiso'
    informeHoy.loc[informeHoy.id_region==13,'nombre_region']='Metropolitana'
    informeHoy.loc[informeHoy.id_region==6,'nombre_region']='O’Higgins'
    informeHoy.loc[informeHoy.id_region==7,'nombre_region']='Maule'
    informeHoy.loc[informeHoy.id_region==16,'nombre_region']='Ñuble'
    informeHoy.loc[informeHoy.id_region==8,'nombre_region']='Biobío'
    informeHoy.loc[informeHoy.id_region==9,'nombre_region']='Araucanía'
    informeHoy.loc[informeHoy.id_region==14,'nombre_region']='Los Ríos'
    informeHoy.loc[informeHoy.id_region==10,'nombre_region']='Los Lagos'
    informeHoy.loc[informeHoy.id_region==11,'nombre_region']='Aysén'
    informeHoy.loc[informeHoy.id_region==12,'nombre_region']='Magallanes'
    
    
    informeHoy.to_csv(path_informes+stringHoy+formato_archivo, index=False)