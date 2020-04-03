## Script para correr 1 vez al día

import pandas as pd
import glob
from datetime import date
import numpy as np


##Primero consolidamos los regionales

pathImport='../../informes_minsal/informes_diarios_Region_CSV/'
pathExport='../../'

allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
auxBool=True

primero=True


for i in allfiles:

    dateString=(i.replace(pathImport,'')[0:10])
    df = pd.read_csv((pathImport+i),",")
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
        
df_consolidado.to_csv(pathExport+'Consolidado_COVID19_Chile_Regiones.CSV', index=False)


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
    pivot_casos_totales.to_csv(pathExport+'COVID19_Chile_Regiones-'+columna+'.CSV')








##Ahora consolidamos los Comunales

pathImport='../../informes_minsal/informes_diarios_Comuna_CSV/'
pathExport='../../'

allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
auxBool=True

primero=True


for i in allfiles:

    dateString=(i.replace(pathImport,'')[0:10])
    df = pd.read_csv((pathImport+i),",")
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
    df['casos_totales']=df.casos_totales.fillna(0)
    df['casos_totales']=df.casos_totales.astype(int)
    df['tasa']=df.tasa.fillna(0)
    df['tasa']=df.tasa.astype(float)
    df['poblacion']=df.poblacion.fillna(0)
    
    ##Ahora corregimos los datos de los casos totales.
    df['casos_totales']=(df.tasa*df.poblacion/100000).round(0).astype(int)
    
    if primero:
        #Creamos el consolidado usando la fecha mas antigua
        df_consolidado=df.copy()
        
        print('primero')
    else:
        #para todo el resto los unimos abajo
        df_consolidado=df_consolidado.append(df)
        
    primero=False

### guardamos el archivo
        
df_consolidado.to_csv(pathExport+'Consolidado_COVID19_Chile_Comunas.CSV', index=False)



##casos_nuevos
exportColumns=['casos_totales',
               'tasa']
for columna in exportColumns:
    pivot_casos_totales= df_consolidado.pivot_table(index=['id_region', 'nombre_region', 'id_comuna', 'nombre_comuna'],
         columns='fecha',
         values=columna)
    pivot_casos_totales.to_csv(pathExport+'COVID19_Chile_Comunas-'+columna+'.CSV')






