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
    nombreInformesComunas,pathReportesCOVID
    

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
        
    df_consolidado=df_consolidado[['id_region',
                               'nombre_region',
                               'casos_totales',
                               'casos_nuevos',
                               'casos_nuevos_sintomas',
                               'casos_nuevos_nosintomas',
                               'fallecidos_totales',
                               'fallecidos_nuevos',
                               'recuperados_totales',
                               'recuperados_nuevos']]
            
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
    
    print('La consolidación de comunas se hace a partir del submodulo de ivan')

    pathImport=pathInformesComunas
    
    allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
    auxBool=True
    
    primero=True
    
    df=pd.read_csv(pathReportesCOVID)
    
    '''    
    df.columns
    Out[27]: Index(['Fecha',
    'CUT', 'Region', 'Comuna', 'Casos Confirmados'],
    dtype='object')
    '''

    #primero cambiamos al formato como lo teníamos nosotros, para no echar a perder los scripts

    df=df.rename(columns={"Fecha": "fecha",
                          "CUT": "id_comuna",
                          "Region": "nombre_region",
                          "Comuna":"nombre_comuna",
                      "Casos Confirmados": "casos_totales"})    
    
    df['nombre_region']=df.nombre_region.replace('AP',"Arica y Parinacota")
    df['nombre_region']=df.nombre_region.replace('TA',"Tarapaca")
    df['nombre_region']=df.nombre_region.replace('AN',"Antofagasta")
    df['nombre_region']=df.nombre_region.replace('AT',"Atacama")
    df['nombre_region']=df.nombre_region.replace('CO',"Coquimbo")
    df['nombre_region']=df.nombre_region.replace('VS',"Valparaiso")
    df['nombre_region']=df.nombre_region.replace('RM',"Region Metropolitana")
    df['nombre_region']=df.nombre_region.replace('LI',"OHiggins")
    df['nombre_region']=df.nombre_region.replace('ML',"Maule")
    df['nombre_region']=df.nombre_region.replace('NB',"Nuble")
    df['nombre_region']=df.nombre_region.replace('BI',"Biobio")
    df['nombre_region']=df.nombre_region.replace('AR',"Araucania")
    df['nombre_region']=df.nombre_region.replace('LR',"Los Rios")
    df['nombre_region']=df.nombre_region.replace('LL',"Los Lagos")
    df['nombre_region']=df.nombre_region.replace('AI',"Aisen")
    df['nombre_region']=df.nombre_region.replace('MA',"Magallanes y la Antartica Chilena")

    df['id_region']=0
    
    df.loc[df.nombre_region=='Arica y Parinacota','id_region']=15
    df.loc[df.nombre_region=='Tarapaca','id_region']=1
    df.loc[df.nombre_region=='Antofagasta','id_region']=2
    df.loc[df.nombre_region=='Atacama','id_region']=3
    df.loc[df.nombre_region=='Coquimbo','id_region']=4
    df.loc[df.nombre_region=='Valparaiso','id_region']=5
    df.loc[df.nombre_region=='Region Metropolitana','id_region']=13
    df.loc[df.nombre_region=='OHiggins','id_region']=6
    df.loc[df.nombre_region=='Maule','id_region']=7
    df.loc[df.nombre_region=='Nuble','id_region']=16
    df.loc[df.nombre_region=='Biobio','id_region']=8
    df.loc[df.nombre_region=='Araucania','id_region']=9
    df.loc[df.nombre_region=='Los Rios','id_region']=14
    df.loc[df.nombre_region=='Los Lagos','id_region']=10
    df.loc[df.nombre_region=='Aisen','id_region']=11
    df.loc[df.nombre_region=='Magallanes y la Antartica Chilena','id_region']=12
    
    pobla=pd.read_csv('../datos/informes_diarios_comunas/2020-03-30-InformeDiarioComunas-COVID19.csv')

    pobla=pobla[['nombre_comuna','poblacion']]
    
    df=df.merge(df.merge(pobla,left_on='nombre_comuna',right_on='nombre_comuna', sort=False))
    
    df['tasa']=df.casos_totales/df.poblacion*100000

    df=df[['fecha',
           'id_region',
           'nombre_region',
           'id_comuna',
           'nombre_comuna',
           'casos_totales',
           'poblacion',
           'tasa']]
    df.fecha=pd.to_datetime(df["fecha"],format="%d-%m-%Y").dt.strftime('%Y-%m-%d')
    #guardamos el informe consolidado 
    df.to_csv(pathExport+nombreInformeConsolidadoComunas, index=False)
    
    exportColumns=['casos_totales',
                   'tasa']
    for columna in exportColumns:
        pivot= df.pivot_table(index=['id_region', 'nombre_region', 'id_comuna', 'nombre_comuna'],
             columns='fecha',
             values=columna)
        pivot.to_csv(pathExport+nombreInformesComunas+columna+'.CSV')
    
    
    print('Datos por Comuna consolidados!')
    
    return df.fecha[len(df.fecha)-1]
    '''
    
    
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
