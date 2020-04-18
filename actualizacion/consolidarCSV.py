#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Script para correr cuando haya actualización de los informes diarios en CSV

import pandas as pd
import glob
import numpy as np
from variables import pathInformesRegiones,\
    pathInformesComunas,\
    pathExport,\
    nombreInformeConsolidadoRegiones,\
    nombreInformesRegiones,\
    nombreInformeConsolidadoComunas,\
    nombreInformesComunas
    

def consolidarCSVRegiones():
    
     ##Primero consolidamos los regionales
    
    pathImport=pathInformesRegiones
    allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
    auxBool=True
    
    primero=True
    
    
    for i in allfiles:
    
        dateString=(i.replace(pathImport,'')[0:10])
        df = pd.read_csv((i),",")
        #filas=df.shape[0]
        
        #primero hacemos una columna de puros zeros
        fecha = pd.DataFrame(np.zeros((len(df), 1)))
        #para simplemente luego tener una columna con la fecha
        
        
        fecha['fecha']=dateString
        #=date(*map(int,dateString.split('-')))
    
        #juntamos los dos dataframes
        df_con_fecha=pd.concat([fecha['fecha'],df],axis=1)
        
        if primero:
            #Creamos el consolidado usando la fecha mas antigua
            df_consolidado=df_con_fecha.copy()
            
        else:
            #para todo el resto los unimos abajo
            df_consolidado=df_consolidado.append(df_con_fecha)
            
        primero=False
    
    ### guardamos el archivo
        
    df_consolidado=df_consolidado[['fecha', 'id_reg', 'nombre_reg', 'casos_nuevos', 'casos_totales',
       'fallecidos_nuevos', 'fallecidos_totales', 'recuperados_nuevos',
       'recuperados_totales']]
            
    df_consolidado.to_csv(pathExport+nombreInformeConsolidadoRegiones, index=False)
    
    ##########
    # Ahora que tenemos el consolidado por Regiones, las vamos a pivotear para sacar
    # informes para cada uno de los datos.
    
    
    
    ##casos_nuevos
    exportColumns=['casos_nuevos',
                   'casos_totales',
                   'fallecidos_nuevos',
                   'fallecidos_totales',
                   'recuperados_nuevos',
                   'recuperados_totales']
    for columna in exportColumns:
        pivot_casos_totales= df_consolidado.pivot_table(index=['id_reg','nombre_reg'],
             columns='fecha',
             values=columna)
        pivot_casos_totales.to_csv(pathExport+nombreInformesRegiones+columna+'.CSV')
    
    
    
    
    print('Datos Regionales consolidados!')


def consolidarCSVComunas():
    
    print('Falta todavía programar bien la consolidación de CSV Comunas')

'''
    ##Ahora consolidamos los Comunales
    
    pathImport=pathInformesComunas
    
    allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
    auxBool=True
    
    primero=True
    
    
    for i in allfiles:
    
        dateString=(i.replace(pathImport,'')[0:10])
        df = pd.read_csv((i),",")
        #filas=df.shape[0]
        
        #primero hacemos una columna de puros zeros
        fecha = pd.DataFrame(np.zeros((len(df), 1)))
        #para simplemente luego tener una columna con la fecha
        
        
        fecha['fecha']=dateString
        #=date(*map(int,dateString.split('-')))
    
        #juntamos los dos dataframes
        df=pd.concat([fecha['fecha'],df],axis=1)
        
        
        ### Los datos por Comuna tienen que ser arreglados.
        #   Primero, a partir de la columna de tasa y la de población, hay que
        #   reconstruir los datos de los casos (porque sólo informan cuando hay más
        # de 4 casos)
        
        df['casos_totales']=df.casos_totales.replace('-',0)
        df['tasa']=df.tasa.replace('-',0)
        
        
        df['casos_totales']=df.casos_totales.fillna(0)
        df['tasa']=df.tasa.fillna(0)
        
        df['casos_totales']=df.casos_totales.astype(int)


        df['tasa']=df.tasa.astype(float)
        
        df['poblacion']=df.poblacion.fillna(0)
        
        
        ##Ahora corregimos los datos de los casos totales.
        ##EXEPTO PARA LAS "Por determinar"
        df.loc[df.nombre_comuna!='Por determinar','casos_totales']=\
            (df[df.nombre_comuna!='Por determinar'].tasa\
              *df[df.nombre_comuna!='Por determinar'].poblacion/100000)\
                .round(0).astype(int)
        
        if primero:
            #Creamos el consolidado usando la fecha mas antigua
            df_consolidado=df.copy()
            
        else:
            #para todo el resto los unimos abajo
            df_consolidado=df_consolidado.append(df)
            
        primero=False
    
    
    ### guardamos el archivo
            
    df_consolidado.to_csv(pathExport+nombreInformeConsolidadoComunas, index=False)
    
    df_consolidado['id_comuna']=df_consolidado.id_comuna.fillna(0)
    
    ##casos_nuevos
    exportColumns=['casos_totales',
                   'tasa']
    for columna in exportColumns:
        pivot= df_consolidado.pivot_table(index=['id_region', 'nombre_region', 'id_comuna', 'nombre_comuna'],
             columns='fecha',
             values=columna)
        pivot.to_csv(pathExport+nombreInformesComunas+columna+'.CSV')
    
    
    print('Datos por Comuna consolidados!')

'''
