
titulo='Exámenes, Contagiados y Letalidad al 22 Mayo'

fontsize=24
fontsizenames=30

import pandas as pd
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import seaborn as sns

fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(size= 20,fname="../Montserrat-Regular.ttf")

fname = os.path.split(fpath)[1]

##Primero Cargamos los Datos de Worldometers
path='test.csv'

df1=pd.read_csv(path,sep=",")

#print(df1.head())
#print(df1.iloc[:,2])
#print(df1.iloc[:,13])
#print(df1.iloc[:,1])

df1['tasa_casos']=df1.iloc[:,2]/(df1.iloc[:,13]/10**5)
df1['tasa_testeo']=df1.iloc[:,11]/(df1.iloc[:,13]/10**5)
df1['tasa_de_positividad']=df1.iloc[:,2]/(df1.iloc[:,11])
df1['tasa_letalidad']=df1.iloc[:,4]/(df1.iloc[:,2])

#print(df1['tasa_testeo'])
#print(df1.head())
#print(df1['tasa_de_positividad'])

### SACAMOS OUTLIERS, OJO CHINA NO TIENE DATOS COMAPRABLES EN ESTA BASE...

df1=df1[df1.Country!="China"]
df1=df1[df1.Country!="Qatar"]
df1=df1[df1.Country!="UAE"]
### Corregir tema de las comas y puntos 

#data['tasa_fallecidos']=df1.fallecidos_totales/(data.pobla/10**6)
#data['tasa_testeo']=df1.pcr_numero/(data.pobla/10**5)
#data['fatalidad']=df1.fallecidos_totales/(data.casos_totales)*100
### ACA ESTEBAN SACO 

### datas 

## Sirve como una forma de normalizar, para tener un valor fundamental.
## Muestra Contagios por cada 100.000 10^5 poblacion
## Muestra PCR por cada 100.000 10^5 poblacion

x="tasa_testeo"
y="tasa_casos"
nombres='Country'
alto=9
ancho=9
prop1 = fm.FontProperties(size= 10,fname="../Montserrat-Regular.ttf")

fig, ax = plt.subplots(figsize=(ancho, alto))
g =sns.scatterplot(x=x, y=y,
                       hue=nombres,
                       size="tasa_letalidad",
                       sizes=(10, 800),
                       data=df1,ax=ax);

for line in df1.index:#range(0,datascatter.shape[0]):
        deltaderecha=0;
        if ((df1['Country'][line]=='India')or(df1['Country'][line]=='Pakistan')or(df1['Country'][line]=='Bangladesh')):
          deltaderecha=469
        if ((df1['Country'][line]=='Chile')):
          deltaderecha=199
        ax.text(df1[x][line]+deltaderecha,
                 df1[y][line]+19,
                 df1['Country'][line],
                 horizontalalignment='center',
                 color='black',
                 fontsize=3,

                 fontproperties=prop1)
                 #weight='semibold')

h,l = ax.get_legend_handles_labels()
bbox_to_anchor_y=0
size_lgd = plt.legend(h[-4:-1], l[-4:-1], loc='lower right',#, borderpad=1.6,# prop={'size': 20},
                         # bbox_to_anchor=(0.5,-0.45), 
                         #markerfirst=False,
                          fancybox=True,# shadow=True,
                          #bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                          bbox_to_anchor=(0.98, 0.05),
                          labelspacing=2,#,borderpad=-4,
                          prop=prop1,
                #frameon=True,
                framealpha=0,#title="popdensity",
                numpoints=1)._legend_box.align='center'#, loc=4)#, numpoints=4)
ax.text(5000, 140, 'Letalidad (en %)', fontproperties=prop,fontsize=18)

plt.xlabel("Exámenes PCR por cada 100.000 habitantes",fontproperties=prop,fontsize=18)
plt.ylabel("Contagios por cada 100.000 habitantes",fontproperties=prop,fontsize=18)
plt.title(titulo,pad=10,fontproperties=prop,fontsize=fontsize)
#plt.xticks([250, 500, 750, 1000,1250, 1500], ['250', '500', '750', '1.000', '1.250', '1.500'])
plt.savefig("PostPCRMundo.png")
plt.show()



