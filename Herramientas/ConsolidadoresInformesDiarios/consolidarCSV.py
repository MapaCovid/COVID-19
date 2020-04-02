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
        
        print('primero')
    else:
        #para todo el resto los unimos abajo
        print('segundo')
        df_consolidado=df_consolidado.append(df_con_fecha)
        
    primero=False

### guardamos el archivo
        
df_consolidado.to_csv(pathExport+'COVID19_Chile_Region.CSV', index=False)
