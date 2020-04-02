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