#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:23:57 2020

@author: esteban
"""


ultimaFechaCasos='2020-05-20'
titulo='Letalidad por Región al 20 de Mayo'
fatalidad='Letalidad [%]'




data_size=fatalidad
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


############################################################
# Datos confirmados por region
path='../../COVID19_Chile_Regiones-casos_totales.CSV'
casos=pd.read_csv(path)

casos=casos[['nombre_region',ultimaFechaCasos,'id_region']]
casos=casos.rename(columns={'nombre_reg':'nombre_region',ultimaFechaCasos:'casos_totales','id_reg':'id_region'})



############################################################
# Datos fallecidos por region
path='../../COVID19_Chile_Regiones-fallecidos_totales.CSV'
fallecidos=pd.read_csv(path)

fallecidos=fallecidos[['nombre_region',ultimaFechaCasos,'id_region']]
fallecidos=fallecidos.rename(columns={'nombre_region':'nombre_region',ultimaFechaCasos:'fallecidos_totales','id_region':'id_region'})


data=casos.merge(fallecidos, on='id_region')
data=data.rename(columns={'nombre_region_x':'nombre_region'})
################################################################
data=data[['id_region',
           'nombre_region',
           'casos_totales',
           'fallecidos_totales']]

###############################################################
casosTotalesChile=data.casos_totales.sum()
fallecidosTotalesChile=data.fallecidos_totales.sum()



row_chile = pd.DataFrame([pd.Series([0,
     'Chile',
     casosTotalesChile,
     fallecidosTotalesChile])], index = [len(data)])

row_chile.columns=data.columns

data = pd.concat([data, row_chile])

data['fatalidad']=data.fallecidos_totales/(data.casos_totales)*100
data.nombre_region=data.nombre_region.replace('Metropolitana','RM')


data=data.rename(columns={'fatalidad':fatalidad})






data.nombre_region=data.nombre_region.replace('Arica y Parinacota','Arica y P.')
data.nombre_region=data.nombre_region.replace('Arica y Parinacota','Arica y P.')
fata=data[['nombre_region',fatalidad]].sort_values(by=[fatalidad],ascending=False)
sns.set(font_scale=2)
sns.set_style("white")#,)  
alto=8
ancho=9
fig = plt.figure()
fig, ax = plt.subplots(figsize=(ancho, alto))
g= sns.barplot(x="nombre_region",
                 y=fatalidad,
                 data=fata,
                 palette="Reds_r",
                 ax=ax)
i=0
for p in g.patches:
    height = p.get_height()
    g.text(p.get_x()+p.get_width()/2., height + 0.1,
        fata[fatalidad].round(1).values[i],ha="center",
        fontproperties=prop,fontsize=17)
    i+=1
plt.xticks( ha='right', rotation=45,fontproperties=prop,fontsize=20)
g.axhline(1.1,linewidth=4, color='black')
plt.ylabel("Letalidad [%]",fontproperties=prop,fontsize=fontsize)
plt.xlabel("",fontproperties=prop,fontsize=fontsize)
plt.title(titulo,pad=35,fontproperties=prop,fontsize=fontsize)
margen=0.03
#gs1.tight_layout(fig, rect=[0+margen, 0, 1, 0.8])
#plt.tight_layout(rect=[0+margen, 0+margen, 0.5, 1-margen])
sns.despine()
plt.show()

