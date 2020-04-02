## Script para correr 1 vez al día

import pandas
import glob
from datetime import date

pathImport='../../informes_minsal/informes_diarios_CSV/'
pathExport='../../'

allfiles = [i for i in glob.glob((pathImport+'*.{}').format('csv'))]
auxBool=True


for i in allfiles:

    dateString=(i[0:10])
    pd = pandas.read_csv((pathImport+i),",")
    
    pd['Fecha']= date(*map(int,dateString.split('-')))
    with open("consolidado.txt",'a') as f:
        pd.to_csv(f,header=auxBool,sep=",",index=False)
        f.close()
    auxBool=False

pd = pandas.read_csv(i,",")