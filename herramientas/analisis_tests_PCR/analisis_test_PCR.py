#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:56:18 2020

@author: esteban
"""

ultimaFechaCasos='2020-05-09'
titulo='Exámenes, Contagiados y Letalidad al 09 Mayo'
fatalidad='Letalidad (en %)'
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
pcrsum.loc[pcrsum.nombre_region=='Valparaíso','id_region']=5
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

casos=casos[['nombre_region',ultimaFechaCasos,'id_region']]
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

fallecidos=fallecidos[['nombre_region',ultimaFechaCasos,'id_region']]
fallecidos=fallecidos.rename(columns={'nombre_region':'nombre_region',ultimaFechaCasos:'fallecidos_totales','id_region':'id_region'})


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
     poblaTotalesChile])], index = [len(data)])

row_chile.columns=data.columns

data = pd.concat([data, row_chile])


data['tasa_casos']=data.casos_totales/(data.pobla/10**5)
data['tasa_fallecidos']=data.fallecidos_totales/(data.pobla/10**6)
data['tasa_testeo']=data.pcr_numero/(data.pobla/10**5)
data['fatalidad']=data.fallecidos_totales/(data.casos_totales)*100
data.nombre_region=data.nombre_region.replace('Metropolitana','RM')


data=data.rename(columns={'fatalidad':fatalidad})
data_sin_Magallanes=data[data.id_region!=12]
datas=[[data,0],
       [data_sin_Magallanes,0]
       ]

import locale
# Set to German locale to get comma decimal separater
locale.setlocale(locale.LC_NUMERIC, "de_DE")

plt.rcdefaults()

# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True

i = 0
for [datascatter,bbox_to_anchor_y] in datas:
    
    
    x="tasa_testeo"
    y="tasa_casos"
    nombres='nombre_region'
    size=data_size

    sns.set(font_scale=2)
    sns.set_style("white")#,)
    
    alto=9
    ancho=9
    fig = plt.figure()
    #import matplotlib.gridspec as gridspec
    #fig=plt.figure(figsize=(ancho, alto))
    #gs1 = gridspec.GridSpec(1, 1)
    #ax = fig.add_subplot(gs1[0])
    
    fig, ax = plt.subplots(figsize=(ancho, alto))
    #fig, ax = plt.subplots()
    g =sns.scatterplot(x=x, y=y,
                       hue=nombres,
                       size=size,
                       sizes=(400, 1000),
                       data=datascatter,ax=ax);
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #ax.set_xlim(0,0.010)
    
    #For each point, we add a text inside the bubble
    
    if i == 0:
      more = 10
    else: 
      more = 0

    for line in datascatter.index:#range(0,datascatter.shape[0]):
        delta=0;
        if ((datascatter[nombres][line]=='Los Ríos')or
        (datascatter[nombres][line]=='Araucanía')):
            delta=8;
        if (datascatter[nombres][line]=='Arica y Parinacota'):
            delta=-18;
        if ((datascatter[nombres][line]=='Coquimbo') or
            datascatter[nombres][line]=='Arica y Parinacota'):
            delta=-18;
        ax.text(datascatter[x][line],
                 datascatter[y][line]+7+delta+more,
                 datascatter[nombres][line],
                 horizontalalignment='center',
                 size='small',
                 color='black',
                 fontsize=fontsizenames,
                 fontproperties=prop)
                 #weight='semibold')
    
    
    h,l = ax.get_legend_handles_labels()
    size_lgd = plt.legend(h[-4:-1], l[-4:-1], loc='lower right',#, borderpad=1.6,# prop={'size': 20},
                         # bbox_to_anchor=(0.5,-0.45), 
                         #markerfirst=False,
                          fancybox=True,# shadow=True,
                          #bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                          bbox_to_anchor=(1.04, bbox_to_anchor_y),
                          labelspacing=0.8,#,borderpad=-4,
                          prop=prop,
                #frameon=True,
                framealpha=0,#title="popdensity",
                numpoints=1)._legend_box.align='center'#, loc=4)#, numpoints=4)
    if i == 0:
        ax.text(1320, 110, 'Letalidad (en %)', fontproperties=prop)
    else:
      ax.text(1320, 54.75, 'Letalidad (en %)', fontproperties=prop)
#    leg = plt.get_legend()
#    leg._legend_box.align = "left"
#    tit=leg.get_title()
    #tit.set_horizontalalignment('left')#_legend_box.align='left'
    plt.xlabel("Exámenes PCR por cada 100.000 habitantes",fontproperties=prop,fontsize=fontsize)
    plt.ylabel("Contagios por cada 100.000 habitantes",fontproperties=prop,fontsize=fontsize)
    plt.xticks([250, 500, 750, 1000,1250, 1500], ['250', '500', '750', '1.000', '1.250', '1.500'])

    plt.title(titulo,pad=35,fontproperties=prop,fontsize=fontsize)
    margen=0.03
    #gs1.tight_layout(fig, rect=[0+margen, 0, 1, 0.8])
    #plt.tight_layout(rect=[0+margen, 0+margen, 0.5, 1-margen])
    sns.despine()
    #plt.savefig('%i.png' %i)
    i += 1

#plt.show(block=False)    