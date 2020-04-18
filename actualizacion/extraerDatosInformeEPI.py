#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:36:49 2020

@author: esteban
"""



#def extraerDatosInformeEPI(templateJSON,informeEPI,pathInformesComunas):
def extraerDatosInformeEPI():    
    templateJSON="./templatesJSON/2020-04-15-INFORME_EPI_COVID19.tabula-template.json"
    informeEPI="../fuentes/informes_departamento_epidimiologia/2020-04-15-INFORME_EPI_COVID19.pdf"
    pathInformesComunas='../datos/informes_diarios_comunas/'
    # Esta función toma como argumentos el templateJSON para
    # Extraer la info desde el archivo PDF en path_archivo
    # Y dejarla en pathInformesComunas
    print('Todavía falta programar la extracción correctamente')
    
'''    
    
    #Documento adaptado de https://github.com/Stepp1 y https://github.com/estebaniglesias 
#por https://github.com/DiazSalinas
    
    import subprocess
    import shlex
    import requests
    
    #Requiere del paquete tabula-py
    #pip install tabula-py 
    
    import tabula
    
    df = tabula.read_pdf_with_template(informeEPI, templateJSON)

    
    comunas={}
    for idx, dff in enumerate(df):
        key = 'tabla_' + str(idx + 1)
        comunas[key]=dff
        comunas[key].rename(columns=lambda x: x.replace(',', '.'), inplace=True)
        comunas[key].iloc[:,-1] = comunas[key].iloc[:,-1].str.replace(',', '.')
 
    
    #Hay que dejar todo en un csv en pathInformesComunas
    # Formato por definir
        
'''