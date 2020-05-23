import pandas as pd
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import seaborn as sns
import locale
# Set to German locale to get comma decimal separater
import numpy as np

locale.setlocale(locale.LC_NUMERIC, "es_ES")
plt.rcdefaults()
# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True


titulo='Exámenes, Contagiados y Letalidad al 22 Mayo'

fontsize=24
fontsizenames=30



fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(size= 20,fname="../Montserrat-Regular.ttf")

fname = os.path.split(fpath)[1]

##Primero Cargamos los Datos de Worldometers
path='test.csv'

df1=pd.read_csv(path,sep=",")

pais = np.array(['USA', 'Brasil', 'Rusia',r'España', 'UK','Italia', 'Francia', 'Alemania', r'Turquía', r'Irán', 'India', r'Perú', 'China', r'Canadá', 'A. Saudita', r'México', 'Chile', r'Bélgica', r'Pakistán', r'Países Bajos','Qatar', 'Ecuador', 'Bielorrusia', 'Suecia', 'Suiza', 'Singapur', r'Bangladesh', 'Portugal', 'UAE', 'Irlanda'])
df1['Pais'] = pais

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
prop1 = fm.FontProperties(size= 11,fname="../Montserrat-Regular.ttf")
prop2 = fm.FontProperties(size= 14,weight='bold',fname="../Montserrat-Regular.ttf")

fig, ax = plt.subplots(figsize=(ancho, alto))
g =sns.scatterplot(x=x, y=y,
                       hue=nombres,
                       size="tasa_letalidad",
                       sizes=(10, 800),
                       data=df1,ax=ax);

for line in df1.index:#range(0,datascatter.shape[0]):
        delta_ejex=0;
        delta_ejey=0
        if ((df1['Pais'][line]=='Pakistán')or(df1['Pais'][line]=='Bangladesh')):
          delta_ejex=669
          delta_ejey=-15
        if ((df1['Pais'][line]=='India')):
          delta_ejey=-25
          delta_ejex=439
        if ((df1['Pais'][line]=='Bangladesh')):
          delta_ejey=-23
        if ((df1['Pais'][line]=='Chile')):
          delta_ejex=199
          delta_ejey=-15
        if ((df1['Pais'][line]=='Suecia')or(df1['Pais'][line]=='Suiza')or(df1['Pais'][line]=='Portugal')):
          delta_ejex=-77
          delta_ejey=-3
        if ((df1['Pais'][line]=='España')or(df1['Pais'][line]=='Alemania')):
          delta_ejey=-3
        if ((df1['Pais'][line]=='Canada')):
          delta_ejex=-50
        if ((df1['Pais'][line]=='Chile')):
          ax.text(df1[x][line]+delta_ejex,
                 df1[y][line]+19+delta_ejey,
                 df1['Pais'][line],
                 horizontalalignment='center',
                 color='black',
                 fontsize=10,
                 weight='semibold',
                 fontproperties=prop2)
        elif((df1['Pais'][line]!='Chile')):
          ax.text(df1[x][line]+delta_ejex,
                 df1[y][line]+19+delta_ejey,
                 df1['Pais'][line],
                 horizontalalignment='center',
                 color='black',
                 fontsize=6,

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



plt.xticks(fontproperties = prop, fontsize= 12)
plt.yticks(fontproperties = prop, fontsize = 12)
plt.savefig("PostPCRMundo.png")
plt.show()



