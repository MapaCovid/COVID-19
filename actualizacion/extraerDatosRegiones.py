#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script se ha realizado gracias al aporte de https://github.com/jcrucesdeveloper
Y las posteriores contribuciones de https://github.com/estebaniglesias
"""
#función que entrega el día del útlimo informe Regional disponible en el minsal
from fechaHoy import getDay
from variables import pathInformesRegiones, formatoArchivoRegiones, urlInformesRegionesMinsal
path = pathInformesRegiones
formato_archivo = formatoArchivoRegiones

import requests
import re
from bs4 import BeautifulSoup
import os.path
import pandas as pd


def extraerDatosRegiones():
    #Si actualiza devuelve True
    #Si no actualiza devuelve False

    ## Al toque vamos a ver si la info actualizada es la última o no
    #en particular vamos a ver si la fecha de la pag ya está en nuestro CSV
    print('Veamos qué fecha tiene el minsal')
    fechaHoyString = getDay()
    print('El minsal tiene fecha de: ' + fechaHoyString)

    if os.path.isfile(path + fechaHoyString + formato_archivo):
        print(
            'No hay actualización, los por Comuna datos ya estaban actualizados'
        )
        return (False, '')
        ##Los datos del sitio web ya están en CSV's
    else:
        #Los datos no están. Vamos a sacarlos.
        print('Son datos nuevos, asi que los vamos a extraer')




        ########SCRAPPING EN LA PAGINA DEL MINSAL CON PANDAS########
        #Para usar pd.read_html se necesita usar directamente el string de la url, 
        # por lo que no funciona si se importa desde otro script con un request
        url = 'https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/'
        #Extraemos la tabla de internet
        tables = pd.read_html(url)
        df = tables[0]
        df = df.drop([0,18,19])

        #Preparamos los nombres de las columnas en el formato ya establecido y limpiamos la tabla
        header = [
            'nombre_region',
            'casos_totales', 
            'casos_nuevos', 
            'casos_nuevos_sintomas',
            'casos_nuevos_nosintomas',
            'Casos nuevos sin notificar',
            'Casos activos confirmados',
            'fallecidos_totales',
            'recuperados_totales']
        df = df[1:]
        df.columns = header
        #Eliminamos las columnas que no nos sirven
        df = df.drop(columns = ['Casos nuevos sin notificar', 'Casos activos confirmados'])
        #Agregamos el id de las regiones
        id_region = [15,1,2,3,4,5,13,6,7,16,8,9,14,10,11,12]
        df.insert(0, 'id_region', id_region, True)
        #Pa revisar
        #print(df)




        ########PREPARAMOS EL INFORME DE HOY########
        #Hacemos una copia
        informeHoy = df
        
        #convertimos a enteros los datos que nos interesan
        informeHoy.casos_totales = informeHoy.casos_totales.str.replace('.','').astype(int)
        informeHoy.casos_nuevos = informeHoy.casos_nuevos.str.replace('.','').astype(int)
        informeHoy.fallecidos_totales = informeHoy.fallecidos_totales.str.replace('.','').astype(int)

        #Fecha segun pagina
        #extraemos los fallecidos de ayer
        from datetime import timedelta
        fechaHoy = pd.to_datetime(fechaHoyString)
        #le resto un día y tengo objeto fecha de ayer
        fechaAyer = fechaHoy - timedelta(1)
        fechaAyerString = fechaAyer.strftime("%Y-%m-%d")



        #ABRIMOS EL INFORME DE AYER PARA HACER CALCULOS
        try:
            #Tratamos de abrir el informe de ayer
            informeAyer = pd.read_csv(path + fechaAyerString + formato_archivo)

            #Del informe de ayer, sacamos los fallecidos y calculamos los fallecidos nuevos de hoy
            informeAyer = informeAyer.rename(columns={'fallecidos_totales': 'fallecidos_totales_old'})
            informeAyer = informeAyer[['id_region', 'fallecidos_totales_old']]
            informeHoy = pd.merge(informeHoy, informeAyer, on='id_region')
            informeHoy['fallecidos_nuevos'] = informeHoy.fallecidos_totales - informeHoy.fallecidos_totales_old

            #Hacemos el mismo procedimiento para los recuperados
            informeAyer = informeAyer.rename(columns={'recuperados_totales': 'recuperados_totales_old'})
            informeAyer = informeAyer[['id_region', 'recuperados_totales_old']]
            informeHoy = pd.merge(informeHoy, informeAyer, on='id_region')
            informeHoy['recuperados_nuevos'] = informeHoyrecuperados_totales - informeHoy.recuperados_totales_old

            #Damos formato al informe de hoy, seleccionando solo las columnas necesarias
            informeHoy = informeHoy[[
                'id_region', 
                'nombre_region', 
                'casos_totales', 
                'casos_nuevos',
                'casos_nuevos_sintomas', 
                'casos_nuevos_nosintomas',
                'fallecidos_totales', 
                'fallecidos_nuevos', 
                'recuperados_totales',
                'recuperados_nuevos'
            ]]
        
        except:
            #Si no se encontró un informe anterior, simplemente se llenan con cero (es lo que se me ocurre por ahora)
            informeHoy['fallecidos_nuevos'] = 0
            informeHoy['recuperados_nuevos'] = 0
            informeHoy = informeHoy[[
                'id_region', 
                'nombre_region', 
                'casos_totales', 
                'casos_nuevos',
                'casos_nuevos_sintomas', 
                'casos_nuevos_nosintomas',
                'fallecidos_totales', 
                'fallecidos_nuevos', 
                'recuperados_totales',
                'recuperados_nuevos'
            ]]
            pass



        ########GUARDAMOS EL INFORME DE HOY########
        #ya estamos listos para guardarlos.
        # usamos fechaHoyString
        # no queremos que guarde el index 0, 1, 2  index=False

        informeHoy.to_csv(path + fechaHoyString + formato_archivo, index=False)
        print('Hemos finalizado')
        print('Casos totales en Chile al ' + fechaHoyString + ' :' +
              informeHoy.casos_totales.sum().astype(str))
        return (True, fechaHoyString)