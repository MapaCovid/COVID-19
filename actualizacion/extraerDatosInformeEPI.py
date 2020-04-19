#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tabula
import csv
import pandas as pd
"""
Created on Fri Apr 17 19:36:49 2020

@author: esteban
"""



#def extraerDatosInformeEPI(templateJSON,informeEPI,pathInformesComunas):
def extraerDatosInformeEPI(fecha):    
    templateJSON="./templatesJSON/Informe-Epidemiologico-17_04_2020.tabula-template"
    informeEPI="../fuentes/informes_departamento_epidimiologia/Informe-Epidemiologico-17_04_2020.pdf"
    pathInformesComunas='../datos/informes_diarios_comunas/'

    to_csv(informeEPI, templateJSON)
    format_comunas(fecha)
    
   
def to_csv(informeEPI,templateJSON):
    df = tabula.read_pdf_with_template(informeEPI,templateJSON,encoding='utf-8')
    comunas = dict()
    file_name = "informeEPI.csv"
    create_headers(file_name)
    for idx, dff in enumerate(df):
        key = 'tabla_' + str(idx + 1)
        comunas[key]=dff
        comunas[key].to_csv(file_name, mode='a', header=True, index=False, encoding="utf-8",float_format='%g')

def create_headers(file):
    #header = ["fecha","id_region","nombre_region","id_comuna","nombre_comuna","poblacion,casos_totales","tasa\n"]
    # Columnas de el csv del informe
    numero_reportes = ['SE{0}'.format(x) for x in range(9,16 + 1)]
    header = ['nombre_comuna', 'poblacion', 'confirmados', 'incidencias', 'actuales', 'incidencia_actual', 'activos', 
    'incidencia_activos'] + numero_reportes + ['key']
    with open(file, 'w', newline='', encoding='utf-8') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(header)

def format_comunas(date):
    df = pd.read_csv("informeEPI.csv")
    df['fecha'] = date
    # Datos que no se tienen en este formato
    df['id_region'] = ''
    df['nombre_region'] = ''
    df['id_comuna'] = ''
    # Ojo se esta escribiendo en la misma carpeta por mientras
    df.to_csv('csv_final.csv', mode='w', header=True, index=False, 
    columns=['fecha', 'id_region','nombre_region', 'id_comuna' ,'nombre_comuna',
     'poblacion', 'confirmados', 'incidencias'], encoding="utf-8",float_format='%g')    

# Aca poner instrucciones
if __name__ =="__main__":
    extraerDatosInformeEPI('17-04-2020')
        
