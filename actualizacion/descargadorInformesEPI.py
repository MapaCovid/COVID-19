#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:29:44 2020

@author: esteban
"""

def descargadorInformesEPI():
    #Esta función debería descargar los informes EPI disponibles en
    # https://www.gob.cl/coronavirus/cifrasoficiales/
    # Y dejarlos en /fuentes/informes_departamento_epidimiologia/
    # con el formato "2020-04-15-INFORME_EPI_COVID19.pdf"
    
    # (Para eso, primero tiene que ver si hay un nuevo informe)
    # Si descarga un nuevo informe, debería devolver (True, "YYY-MM-DD")
    # Si no descarga nada nuevo, es importante que emita (False,""), 
    # Para no correr los procesos de consolidación de Comunas
   
    
    # Por ahora, lo estamos haciendo a mano. Necesitamos programar aquí!
    return (True,"2020-04-15");

#Pero aquí voy a colocar todo lo que estaba en el notebook y que hay que
# poner aquí con cuidado
    

import subprocess
import shlex
import requests

response = subprocess.check_output(shlex.split('curl --request GET https://www.gob.cl/coronavirus/cifrasoficiales/'))

#print(response)
url_reporte = []
url_informe_epi = []
for line in response.decode().splitlines():
    if "Reporte_Covid19.pdf" in line:
        url = line.strip().split('https://')[1].split("\"")[0]
        
        url_reporte.append(url)
        
    #El informe a veces está en minúsculas    
    elif "INFORME_EP" in line:
        
        test = line.strip()
        test = test.split('https://')[1].split("\"")[0]
        url_informe_epi.append(test)
    elif "Informe_EPI" in line:
        
        test = line.strip()
        test = test.split('https://')[1].split("\"")[0]
        url_informe_epi.append(test)
        
for url in set(url_informe_epi):
    subprocess.check_output(shlex.split("wget "+ url))
    
    
#Renombrar para armar estandarizacion a la ultima fecha 10-04-2020
import os
os.rename(r'INFORME_EPI_COVID19_20200401v2.pdf',r'INFORME_EPI_COVID19_20200401.pdf')
os.rename(r'Informe_EPI_03_04_2020.pdf',r'INFORME_EPI_COVID19_03042020.pdf')