## Script para correr 1 vez al día

import pandas as pd
import glob
from datetime import date
import numpy as np

pathImport='../../informes_minsal/informes_diarios_CSV/'
pathExport='../../'

allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
auxBool=True


for i in allfiles:

    dateString=(i.replace(pathImport,'')[0:10])
    df = pd.read_csv((pathImport+i),",")
    #filas=df.shape[0]
    
    #primero hacemos una columna de puros zeros
    fecha = pd.DataFrame(np.zeros((len(df), 1)))
    #para simplemente luego tener una columna con la fecha
    
    
    fecha['fecha']=date(*map(int,dateString.split('-')))

    #juntamos los dos dataframes
    df_con_fecha=pd.concat([fecha['fecha'],df],axis=1)
    
    
    with open("consolidado.txt",'a') as f:
        df_con_fecha.to_csv(f,header=auxBool,sep=",",index=False)
        f.close()
    auxBool=False
