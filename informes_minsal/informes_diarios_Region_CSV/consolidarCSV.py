## Este script no es necesario usarlo después del 02 de Abril de 2020 

"""
Se realiza este script para construir las columnas "casos_nuevos" y 
"fallecidos_nuevos", sólo para los informes diarios previos (e incluído) al 
02 de Abril. Esto porque el minsal antes del 25 de marzo no indicaba los 
"casos nuevos", sino que solo los casos totales. Lo mismo para los fallecidos, 
y hasta el 02 de Abril no se estaban calculando los nuevos fallecidos al 
importar los datos.

La gracia es que a partir de ahora, al generar el informe diario en CSV se 
calculen automáticamente los nuevos_fallecidos sin tener que arreglar después 
los informes.
"""

import pandas
import glob
from datetime import date

allfiles = [i for i in glob.glob('*.{}'.format('csv'))]
auxBool=True
for i in allfiles:

    dateString=(i[0:10])
    pd = pandas.read_csv(i,",")
    pd['Fecha']= date(*map(int,dateString.split('-')))
    with open("consolidado.txt",'a') as f:
        pd.to_csv(f,header=auxBool,sep=",",index=False)
        f.close()
    auxBool=False

pd = pandas.read_csv(i,",")