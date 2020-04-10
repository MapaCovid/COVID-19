#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script se ha realizado gracias al aporte de https://github.com/jcrucesdeveloper
Y las posteriores contribuciones de https://github.com/estebaniglesias
"""
#función que entrega el día del útlimo informe Regional disponible en el minsal
from fechaHoy import getDay
from  variables import pathInformesRegiones, formatoArchivoRegiones, urlInformesRegionesMinsal
path=pathInformesRegiones
formato_archivo=formatoArchivoRegiones

import requests
import re
from bs4 import BeautifulSoup
import os.path

def extraerDatosRegiones():
    #Si actualiza devuelve True
    #Si no actualiza devuelve False
        
    
    ## Al toque vamos a ver si la info actualizada es la última o no
    #en particular vamos a ver si la fecha de la pag ya está en nuestro CSV
    print('Veamos qué fecha tiene el minsal')
    fechaHoyString=getDay()
    print('El minsal tiene fecha de: '+fechaHoyString)
    

    
    if os.path.isfile(path+fechaHoyString+formato_archivo):
        print('No hay actualización, los por Comuna datos ya estaban actualizados')
        return (False,'')
        ##Los datos del sitio web ya están en CSV's
    else:
        #Los datos no están. Vamos a sacarlos.
        print('Son datos nuevos, asi que los vamos a extraer')
        
        page = requests.get(urlInformesRegionesMinsal)
        #Funcion para crear el formato correcto. Sacar tildes y las ñ's
        def normalizeText(text):
            newText = ''
            for char in text:
                if(char == 'á'):
                    newText+='a'
                elif char == 'é':
                    newText+='e'
                elif char == 'í':
                    newText+='i'
                elif char == 'ó':
                    newText+='o'
                elif char == 'ú':
                    newText+='u'
                elif char == 'Ñ':
                    newText+= 'N'
                elif char == "’":
                    newText+= " "
                else:
                     newText+=char
            return newText
        # Dict para saber la id de las regiones
        thisRegionDic = {
            "Arica y Parinacota":15,
            "Tarapaca":1,
            "Antofagasta": 2,
            "Atacama":3,
            "Coquimbo": 4,
            "Valparaiso" : 5,
            "Metropolitana": 13,
            "O Higgins": 6,
            "Maule": 7,
            "Nuble": 16,
            "Biobio":8,
            "Araucania": 9,
            "Los Rios": 14,
            "Los Lagos":10,
            "Aysen": 11,
            "Magallanes":12
        }
        
        
        soup = BeautifulSoup(page.content, 'html.parser')
        
        table = soup.find_all('div',class_="contenido")[0]
        currentTable = list(table.children)[1]
        currentTbody = list(currentTable.children)[1]
        
        #New data es la matriz que guardara todo
        #Por ahora quedará así porque estas son las columnas que tiene el minsal
        columnas=["id_reg","nombre_reg","casos_nuevos","casos_totales","porcentaje","fallecidos_totales"]
        #lo escribo así porque después usaremos las columnas
        newData = [columnas]
        #print(currentTbody)
        # Bucle pricipal que navega a través del sitio e utlizar regex para buscar la info que nos corresponde
        valueTest = 0
       # print('largo del tbody children')
       # print(len(list(currentTbody.children)))
        for currentTr in list(currentTbody.children):
            #print('tr')
            #print(currentTr)
            #Se salta los primeros cinco que son vacios y los impares continene info de las regiones
            if valueTest > 5 and valueTest % 2 != 0:
         #       print('loop 2')
                #print(currentTr) 
                stringTr = str(currentTr)
                arrayTags = stringTr.split("\n")
                #La nueva region que vamos a agregarle la info
                newRegion = []
                
                
                for regString in arrayTags:    
          #          print('loop 3')
                    #Encuentra <>()<> subgrupos de un tag así
                    pattern = re.search(r'<[\w\s=":%;-]*>([A-Za-z0-9_éá’íÑ\.\s]*)%?<.*',regString)
                    if pattern is not None:
           #             print('loop 4')                        
                        #Normalizamos el texto utilizando la funcion de arriba
                        newValue = normalizeText(pattern.group(1))
                        #print('..................')
                        #print(newValue)
                        #Si no tiene valor salimos
                        if(newValue == ""):
                            break
                        else:        
                            #Si existe la region en nuestro dic, utilizamos el id y le hacemos un append a la region
                            if(newValue in thisRegionDic):
                                newRegion.append(thisRegionDic[newValue])
                            #Le hacemos un append del valor que sacamos
                            newRegion.append(newValue)
                    #Sacamos solo los que tienen valores, y ya tenemos todas las regiones
                
                if(len(newRegion) != 0):
                    #Esta linea elminina un espacio que se grababa de más
                    #Esto se saca el 10 de Abril del 2020 porque el Minsal sacó el espacio que se grababa de más
                    #newRegion[4] = newRegion[4][0]
                    
                    newData.append(newRegion)
                valueTest +=1
            
        import pandas as pd
        
        informeHoy= pd.DataFrame(newData, columns=columnas)
        
        #tenemos un pandas, pero la primera fila la tenemos que sacar
        informeHoy=informeHoy[informeHoy.index>0]
        #pero para también usar el informe de ayer, tenemos que tener los mismos indices
        #asi que vamos a reindexar sin cambiar el orden de lo demás
        informeHoy=informeHoy.reset_index(drop=True)
        
        #Lo que sigue con pandas es relativamente simple
        #Primero sacamos el espacio en O Higgins
        informeHoy=informeHoy.replace('O Higgins', 'OHiggins')
        #le sacamos los puntos
        informeHoy=informeHoy.replace('\.','',regex=True)
        #convertimos a enteros los datos que nos interesan
        informeHoy.casos_nuevos=informeHoy.casos_nuevos.astype(int)
        informeHoy.casos_totales=informeHoy.casos_totales.astype(int)
        #print(informeHoy.casos_totales)
        informeHoy.fallecidos_totales=informeHoy.fallecidos_totales.astype(int)
        
        #Fecha segun pagina 
        #extraemos los fallecidos de ayer
        
        from datetime import timedelta
        fechaHoy=pd.to_datetime(fechaHoyString)
        #le resto un día y tengo objeto fecha de ayer
        fechaAyer=fechaHoy-timedelta(1)
        fechaAyerString=fechaAyer.strftime("%Y-%m-%d")
        fechaAyerString
        
        #path='../informes_minsal/informes_diarios_Region_CSV/'
        #formato_archivo='-InformeDiarioRegion-COVID19.csv'
        informeAyer= pd.read_csv(path+fechaAyerString+formato_archivo)
        
        informeHoy['fallecidos_nuevos']=informeHoy.fallecidos_totales-informeAyer.fallecidos_totales
        
        #seleccionamos las columnas según el formato
        informeHoy['recuperados_nuevos']=0
        informeHoy['recuperados_totales']= 0
        informeHoy=informeHoy[['id_reg', 'nombre_reg', 'casos_nuevos', 'casos_totales','fallecidos_nuevos', 'fallecidos_totales','recuperados_nuevos','recuperados_totales']]
        
        #ya estamos listos para guardarlos.
        # usamos fechaHoyString
        # no queremos que guarde el index 0, 1, 2  index=False
        informeHoy.to_csv(path+fechaHoyString+formato_archivo,  index=False)
        print('Hemos finalizado')
        print('Casos totales en Chile al '+fechaHoyString+' :'+informeHoy.casos_totales.sum().astype(str))
        return (True,fechaHoyString)
            
