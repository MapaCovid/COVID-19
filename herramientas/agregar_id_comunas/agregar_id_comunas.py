#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:55:42 2020
@author: esteban
"""

# Este script necesita que instales 
# conda install geopandas
#conda install -c conda-forge descartes


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

#reload(sys)
#sys.setdefaultencoding('utf8')


## Primero necesitamos cargar los polígonos de las comunas.
# poligonos descargados desde https://www.bcn.cl/siit/mapas_vectoriales/index_html
shp_path = "../../fuentes/geometrias_comunas/comunas.shp"
comunasChile = gp.read_file(shp_path)

## Luego cargamos los datos del COVID19
datos_path="../../datos/informes_diarios_comunas/2020-04-10-InformeDiarioComunas-COVID19.csv"
datosComunas = pd.read_csv(datos_path)


'''
comunasChile.columns =  
Index(['objectid', 'shape_leng', 'dis_elec', 'cir_sena', 'cod_comuna',
       'codregion', 'st_area_sh', 'st_length_', 'Region', 'Comuna',
       'Provincia', 'geometry'],
      dtype='object')
'''
## Necesitamos que las columnas tengan el mismo nombre:
comunasChile['nombre_comuna']=comunasChile.Comuna
############################################################

df=datosComunas.merge(comunasChile, on='nombre_comuna')
 '''
df.columns=
Index(['id_region', 'nombre_region', 'id_comuna', 'nombre_comuna', 'poblacion',
       'casos_totales', 'tasa', 'objectid', 'shape_leng', 'dis_elec',
       'cir_sena', 'cod_comuna', 'codregion', 'st_area_sh', 'st_length_',
       'Region', 'Comuna', 'Provincia', 'geometry'],
      dtype='object')
 '''
 



comunasChile.columns
comunasChile[['cod_comuna','Comuna']]


hola=datosComunas.merge(comunasChile, on='nombre_comuna')

map_dataRM.merge(datosComunasRM, on='NOMBRE')

### Cargar la capa con polígonos en JSON
#comunasRM = "comunas13.json"
#map_dataRM = gpd.read_file(comunasRM)
#map_dataRM.head()
#map_dataChile.columns
#Out[9]: Index([u'ID', u'NOMBRE', u'geometry'], dtype='object')

#sns.set(style="whitegrid", palette="pastel", color_codes=True)
#sns.mpl.rc("figure", figsize=(10,6))

#poligonos descargados desde https://www.bcn.cl/siit/mapas_vectoriales/index_html


#sf = shp.Reader(shp_path)
#len(sf.shapes())
#sf.records()[1]





##Aquí ya tenemos un geopandas, asi que podemos importar la info para
#también tenerla en pandas
#map_dataChile[['NOMBRE']].to_csv('NombresComunas.csv', index=False)



#ahora hay que hacer un merge entre map_dataChile y datosComunasRM 
#vamos a hacer un Atrribute Join en pandas

map_dataRM_conEstadisticas = map_dataRM.merge(datosComunasRM, on='NOMBRE')

map_STGO=map_dataRM_conEstadisticas[map_dataRM_conEstadisticas.EN_GRAN_SANTIAGO==1]
#seleccionar solo santiago

#map_STGO.loc['CASOS_MULT_POBLACION_DIV_SUPERFICIE']=map_STGO['CASOS_MULT_POBLACION_DIV_SUPERFICIE'].replace(0, np.nan)

#ahora le voy a appendear la info

map_STGO.loc[:,'CASOS_MULT_POBLACION_DIV_SUPERFICIE']=map_STGO['CASOS_MULT_POBLACION_DIV_SUPERFICIE'].replace(0, np.nan)


# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(30, 30))
 
# Control del título y los ejes
ax.set_title(u'Comunas del Gran Santiago por Índice de Riesgo de Contagio', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': 'black'})
                       
                       # Control del título y los ejes

#ax.set_xlabel('Longitud')
#ax.set_ylabel('Latitud')
plt.axis('off')
#ax.legend(fontsize=1000)


# Añadir la leyenda separada del mapa
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.2)
#map_STGO[(map_STGO.NOMBRE!='Santiago')&(map_STGO.NOMBRE!='Providencia')&(map_STGO.NOMBRE!='Ñuñoa')&(map_STGO.NOMBRE!='Las Condes')] 
# Mostrar el mapa finalizado
map_STGO.plot(column='CASOS_MULT_POBLACION_DIV_SUPERFICIE',
         cmap='Reds', ax=ax,
                                legend=True,
                                legend_kwds={'label': "Riesgo de Contagio",},
                                cax=cax, zorder=5,
                                missing_kwds={"color": "lightgrey",
                                              "edgecolor": "black",
                                              "hatch": "///"#,
                                              #"label": "Missing values",
                                              })








plt.rcParams['font.size'] = 7


map_STGO[(map_STGO.NOMBRE!='Santiago')&&(map_STGOOMBRE!='Providencia')&&(map_STGO.NOMBRE!='Nunoa')]


