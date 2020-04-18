#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:29:44 2020

@author: esteban
"""
from subprocess import Popen, PIPE
import subprocess
import shlex
import requests
import os
from os import walk
from variables import urlCifrasOficiales, pathInformesEPI, pathReportesCOVID
import numpy as np

#urlCifrasOficiales='https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/'
def descargadorInformesEPI():
    #Esta función debería descargar los informes EPI disponibles en
    # https://www.gob.cl/coronavirus/cifrasoficiales/
    # Y dejarlos en /fuentes/informes_departamento_epidimiologia/
    # con el formato "2020-04-15-INFORME_EPI_COVID19.pdf"
    
    # (Para eso, primero tiene que ver si hay un nuevo informe)
    
    
    response = subprocess.check_output(shlex.split('curl --request GET '+urlCifrasOficiales))
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
            
            
   
        
    #Los informes EPI se dejan en  pathInformesEPI   
    #Primero vemos todos archivos que están en la carpeta
    informes_epi_descargados = []
    for (dirpath, dirnames, filenames) in walk(pathInformesEPI):
        informes_epi_descargados.extend(filenames)
        break
    
    #Vamos a capturar sólo los nombres de los archivos:
    nombres_informes_epi=[]
    for urlInforme in url_informe_epi:
        nombres_informes_epi.append(urlInforme.split('/')[-1]);
    urlpath=urlInforme.replace(urlInforme.split('/')[-1],'')
        
    ##Tomamos sólo los que faltan por descargar:
    informes_a_descargar=list(set(nombres_informes_epi)-set(informes_epi_descargados))
    

#    
    from os import popen
    os.chdir(pathInformesEPI)    
    for informe in informes_a_descargar:
        url=urlpath+informe
        os.system('/usr/local/bin/wget '+url)
#        args = ['/usr/local/bin/wget %s', '-r', '-l 1', '-p', '-P %s' % pathInformesEPI, url]
#        output = popen(' '.join(args))

#        args = ['/usr/local/bin/wget', '-r', '-l', '1', '-p', '-P', pathInformesEPI, url]
#        output = Popen(args, stdout=PIPE)



    # Si descarga un nuevo informe, debería devolver (True, "YYY-MM-DD")
    # Si no descarga nada nuevo, es importante que emita (False,""), 
    # Para no correr los procesos de consolidación de Comunas
    
    
   
    
    # Por ahora, lo estamos haciendo a mano. Necesitamos programar aquí!
    return (True,"2020-04-18");
        
