#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:21:38 2020

@author: esteban
"""

#Primero vamos a rescatar los datos desde IVAN
path='../../datos/COVID19_Chile/covid19_chile.csv'

import pandas as pd

df=pd.read_csv(path)

'''

df.columns
Out[8]: 
Index(['Fecha', 'Region', 'Nuevo Confirmado', 'Nuevo Muerte',
       'Nuevo Recuperado', 'Acum Confirmado', 'Acum Muerte',
       'Acum Recuperado'],
      dtype='object')

'''
#vamos a tomar las estadísticas nacionales. sumamos todas las regiones para cada día
df=df.groupby('Fecha').sum()

#las fechas conviene mejor tratarlas como datetime

df.index=pd.to_datetime(df.index,format='%d-%m-%Y')
df=df.sort_index()
a_row=[0,0,0,0,0,0]
row_df = pd.DataFrame([a_row], index = [pd.to_datetime('2020-03-02')], columns=df.columns)
df = pd.concat([row_df, df])

b_row=[358,7,303,10088,133,4338]
row_df = pd.DataFrame([b_row], index = [pd.to_datetime('2020-04-19')], columns=df.columns)
df = pd.concat([df, row_df])



#una vista rápida

df[['Nuevo Confirmado','Nuevo Recuperado']].plot()

#primero veamos si lo que dijo es cierto, juntemos por semanas
#S1 02/03 - 08/03
#S2 09/03 - 15/03
#S3 16/03 -22/03
#S5 .... me da paja seguir copiando, voy a hacer un ciclo for con módulo 7


# Piñera mostró 3 datos:
# Contagiados activos acumulados (barras azules)
# Contagiados nuevos (curva roja)
# Recuperados nuevos (curva verde)

#Construimos contagiados activos
df['Confirmado Activo']=df['Acum Confirmado']-df['Acum Recuperado']

piñeraDatos=[[],[],[]]
mod=0
i=1
sum0=0
sum1=0
sum2=0
while (i<len(df)+1):
    sum0+=df.loc[df.index[i-1],'Confirmado Activo']
    sum1+=df.loc[df.index[i-1],'Nuevo Confirmado']
    sum2+=df.loc[df.index[i-1],'Nuevo Recuperado']
    
    if ((i%7==0)and(i>0)):
        piñeraDatos[0].append(df.loc[df.index[i-1],'Confirmado Activo'])
        piñeraDatos[1].append(sum1)
        piñeraDatos[2].append(sum2)
        
        sum0=0
        sum1=0
        sum2=0
        print(i)
  #  if ((i%7==4)and(i>43)):
  #      print(i)
  #      piñeraDatos[0].append(df.loc[df.index[i],'Confirmado Activo'])
  #      piñeraDatos[1].append(sum1)
  #      piñeraDatos[2].append(sum2)
        
  #      sum0=0
  #      sum1=0
  #      sum2=0
      #  print(i)
    i+=1
    #print(i)

piñeraDatos={
    'casos_activos':piñeraDatos[0],
    'casos_nuevos':piñeraDatos[1],
    'recuperados_nuevos':piñeraDatos[2]}
    
piñeradf=pd.DataFrame(piñeraDatos) 



ax1=piñeradf.casos_activos.plot.bar()
ax1.set_ylim((0,7000))
ax2=piñeradf[['casos_nuevos','recuperados_nuevos']].plot()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, len(df))
y1=df['Nuevo Confirmado'].values

p1 = np.poly1d(np.polyfit(x, y1, 5))

t = np.linspace(0, 1, len(df)*10)
plt.plot(x, y1, 'o', t, p1(t), '-')
plt.show()


