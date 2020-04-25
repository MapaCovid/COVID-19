#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:56:18 2020

@author: esteban
"""

ultimaFechaCasos='2020-04-25'

import pandas as pd
##Primero Cargamos los Datos de tests PCR del repositorio del MinCultura
path='../../fuentes/MinCiencias/output/producto7/PCR_T.csv'

df1=pd.read_csv(path)
df=df1[df1.index>2].reset_index(drop=True).rename(columns={'Region':'fecha'})
df=pd.melt(df,id_vars='fecha',value_vars=list(df.columns[1:]),var_name='nombre_region', value_name='pcr_numero')
df['id_region']=0

df.loc[df.nombre_region=='Arica y Parinacota','id_region']=15
df.loc[df.nombre_region=='Tarapacá','id_region']=1
df.loc[df.nombre_region=='Antofagasta','id_region']=2
df.loc[df.nombre_region=='Atacama','id_region']=3
df.loc[df.nombre_region=='Coquimbo','id_region']=4
df.loc[df.nombre_region=='Valparaiso','id_region']=5
df.loc[df.nombre_region=='Metropolitana','id_region']=13
df.loc[df.nombre_region=='O’Higgins','id_region']=6
df.loc[df.nombre_region=='Maule','id_region']=7
df.loc[df.nombre_region=='Ñuble','id_region']=16
df.loc[df.nombre_region=='Biobío','id_region']=8
df.loc[df.nombre_region=='Araucanía','id_region']=9
df.loc[df.nombre_region=='Los Ríos','id_region']=14
df.loc[df.nombre_region=='Los Lagos','id_region']=10
df.loc[df.nombre_region=='Aysén','id_region']=11
df.loc[df.nombre_region=='Magallanes','id_region']=12
df.pcr_numero=df.pcr_numero.replace('-',0)
df=df.fillna(0)
df.pcr_numero=df.pcr_numero.astype(int)



pcrsum=df.groupby('nombre_region').sum().reset_index()

pcrsum.loc[pcrsum.nombre_region=='Arica y Parinacota','id_region']=15
pcrsum.loc[pcrsum.nombre_region=='Tarapacá','id_region']=1
pcrsum.loc[pcrsum.nombre_region=='Antofagasta','id_region']=2
pcrsum.loc[pcrsum.nombre_region=='Atacama','id_region']=3
pcrsum.loc[pcrsum.nombre_region=='Coquimbo','id_region']=4
pcrsum.loc[pcrsum.nombre_region=='Valparaiso','id_region']=5
pcrsum.loc[pcrsum.nombre_region=='Metropolitana','id_region']=13
pcrsum.loc[pcrsum.nombre_region=='O’Higgins','id_region']=6
pcrsum.loc[pcrsum.nombre_region=='Maule','id_region']=7
pcrsum.loc[pcrsum.nombre_region=='Ñuble','id_region']=16
pcrsum.loc[pcrsum.nombre_region=='Biobío','id_region']=8
pcrsum.loc[pcrsum.nombre_region=='Araucanía','id_region']=9
pcrsum.loc[pcrsum.nombre_region=='Los Ríos','id_region']=14
pcrsum.loc[pcrsum.nombre_region=='Los Lagos','id_region']=10
pcrsum.loc[pcrsum.nombre_region=='Aysén','id_region']=11
pcrsum.loc[pcrsum.nombre_region=='Magallanes','id_region']=12






############################################################
# Datos confirmados por region
path='../../COVID19_Chile_Regiones-casos_totales.CSV'
casos=pd.read_csv(path)

casos=casos[['nombre_reg',ultimaFechaCasos,'id_reg']]
casos=casos.rename(columns={'nombre_reg':'nombre_region',ultimaFechaCasos:'casos_totales','id_reg':'id_region'})


data=pcrsum.merge(casos, on='id_region')



###############################################################

#Pobla

data=data.rename(columns={'nombre_region_x':'nombre_region'})

pobla1=df1[df1.index==1].reset_index(drop=True).rename(columns={'Region':'poblacion'})
pobla1=pd.melt(pobla1,id_vars='poblacion',value_vars=list(pobla1.columns[1:]),var_name='nombre_region', value_name='pobla')
pobla1=pobla1[['nombre_region','pobla']]

data=data.merge(pobla1, on='nombre_region')
data.pobla=data.pobla.astype(int)






############################################################
# Datos fallecidos por region
path='../../COVID19_Chile_Regiones-fallecidos_totales.CSV'
fallecidos=pd.read_csv(path)

fallecidos=fallecidos[['nombre_reg',ultimaFechaCasos,'id_reg']]
fallecidos=fallecidos.rename(columns={'nombre_reg':'nombre_region',ultimaFechaCasos:'fallecidos_totales','id_reg':'id_region'})


data=data.merge(fallecidos, on='id_region')
data=data.rename(columns={'nombre_region_x':'nombre_region'})
################################################################
data=data[['id_region',
           'nombre_region',
           'casos_totales',
           'fallecidos_totales',
           'pcr_numero',
           'pobla']]

###############################################################
casosTotalesChile=data.casos_totales.sum()
fallecidosTotalesChile=data.fallecidos_totales.sum()
PCRTotalesChile=data.pcr_numero.sum()
poblaTotalesChile=data.pobla.sum()

row_chile = pd.DataFrame([pd.Series([0,
     'Chile',
     casosTotalesChile,
     fallecidosTotalesChile,
     PCRTotalesChile,
     poblaTotalesChile])], index = [15])

row_chile.columns=data.columns

data = pd.concat([data, row_chile])


data['tasa_casos']=data.casos_totales/(data.pobla/10**5)
data['tasa_fallecidos']=data.fallecidos_totales/(data.pobla/10**5)
data['tasa_testeo']=data.pcr_numero/(data.pobla/10**5)
data['mortalidad']=data.fallecidos_totales/(data.casos_totales)


datascatter=data[data.id_region!=12]
x="tasa_testeo"
y="tasa_casos"
nombres='nombre_region'
size='mortalidad'
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
fig, ax = plt.subplots()
g =sns.scatterplot(x=x, y=y,
                   hue=nombres,
                   size=size,
                   sizes=(100, 700),
                   data=datascatter,ax=ax);
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#ax.set_xlim(0,0.010)

#For each point, we add a text inside the bubble
for line in datascatter.index:#range(0,datascatter.shape[0]):
     ax.text(datascatter[x][line], datascatter[y][line], datascatter[nombres][line], horizontalalignment='center', size='medium', color='black', weight='semibold')


plt.show()












# Load libraries
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# Create example dataframe
df = pd.DataFrame({
'x': [1, 1.1, 1.2, 2, 5],
'y': [5, 15, 7, 10, 2],
's': [10000,20000,30000,40000,50000],
'group': ['Stamford','Yale','Harvard','MIT','Cambridge']
})

#Create figure
plt.figure(figsize = (15,10))

# Create scatterplot. alpha controls the opacity and s controls the size.
ax = sns.scatterplot(df.x, df.y, alpha = 0.5,s = df.s)

ax.set_xlim(0,6)
ax.set_ylim(-2, 18)

#For each point, we add a text inside the bubble
for line in range(0,df.shape[0]):
     ax.text(df.x[line], df.y[line], df.group[line], horizontalalignment='center', size='medium', color='black', weight='semibold')
