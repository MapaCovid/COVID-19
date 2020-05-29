import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

import os
from matplotlib import font_manager as fm, rcParams

fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(size= 16,fname="../Montserrat-Regular.ttf")
fname = os.path.split(fpath)[1]




#ZOOM 12 1 AÑO
#ZOOM 121 10 AÑOS
numero = 121 #int(input("Escribe 12 para zoom, 121 para 10 años"))
if numero == 121:
	df = pandas.read_csv("desempleoSerieCompleta.csv",sep=";",encoding= 'unicode_escape')
else:
	df = pandas.read_csv("desempleoChile.csv",sep=";",encoding= 'unicode_escape')
#df = pandas.read_csv("desempleoChile.csv",sep=";",encoding= 'unicode_escape')



color_blue = tuple(np.array([38, 53, 134])/255.)
color_red = tuple(np.array([226, 69, 6])/255.)

pop_a = mpatches.Patch(color=color_blue, label='Total país')
pop_b = mpatches.Patch(color=color_red, label='Hombre')
pop_c = mpatches.Patch(color='darkgreen', label='Mujer')

trimestre = np.array(df.values[:,1])#[-200:]
pais = np.array(df.values[:,2])#[-200:]
mujeres = np.array(df.values[:,3])#[-200:]
hombres = np.array(df.values[:,4])#[-200:]
#print(len(trimestre))

fig = plt.figure(figsize=(8,8))

if numero == 121:
	plt.axvline(x=3, color = 'gray', linestyle = '--', linewidth = 2)
	plt.text(4, 5, r'Piñera 2010', fontproperties=prop, fontsize=12, color = 'gray')
	plt.text(52, 5, r'Bachelet 2014', fontproperties=prop, fontsize=12, color = 'gray')
	plt.text(101, 5, r'Piñera 2018', fontproperties=prop, fontsize=12, color = 'gray')
	plt.axvline(x=51, color='gray', linestyle = '--', linewidth = 2)
	plt.axvline(x=100, color='gray', linestyle = '--', linewidth = 2)

if numero == 121:
	plt.plot(mujeres,color = 'darkgreen', lw=2)
	plt.plot(pais, color = color_blue, lw=2)
	plt.plot(hombres, color = color_red, lw=2)
	

if numero == 12:
	plt.plot(mujeres,marker='o',color = 'darkgreen', lw=2)
	plt.plot(pais,  marker='o', color = color_blue, lw=2)
	plt.plot(hombres,marker='o', color = color_red, lw=2)
	

#CRITERIO PUEDEN SER TRES PUNTOS, DEPENDIENDO SI SE TOMA MARZO AL INICIO DEL TRIMESTRE MOVIL O AL FINAL, ESTIMO MAS ADECUADO AL FINAL PORQUE LA TASA DESEMPLEO TIENE LATENCIA
#3 PIÑERA
#51  BACHELET
#100 PIÑERA


#CASO ZOOM
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], trimestre, fontsize=4)
if numero == 121:
	plt.xticks([0,11,22,33,44,55,66,77,88,99,110,121], [trimestre[0],trimestre[11],trimestre[22],trimestre[33],trimestre[44],trimestre[55],trimestre[66],trimestre[77],trimestre[88],trimestre[99],trimestre[110],trimestre[120]], fontproperties=prop)

if numero == 12:
	plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], trimestre, fontsize=4, fontproperties=prop)

plt.xlabel(r'Trimestre', fontsize=14, fontproperties=prop)
plt.ylabel(r'Tasa de desempleo (%)', fontsize=14, fontproperties=prop)

if numero == 121:
	plt.title(r'Desempleo Trimestral móvil Chile 2010 - 2020', fontsize=14, fontproperties=prop)

if numero == 12:
	plt.title(r'Desempleo Trimestral móvil Chile 2019 - 2020', fontsize=14, fontproperties=prop)

plt.xticks(rotation=52,fontsize=11)
plt.yticks(fontsize=12, fontproperties=prop)
plt.legend(handles=[pop_a,pop_b,pop_c], prop = prop)
#ESTE DA LIMITE A EJE X
if numero == 121:
	plt.xlim(-1, 122)

if numero == 12:
	plt.xlim(-1, 13)

#plt.legend(fontsize=14)
plt.savefig("outputChile2-"+str(numero)+"-.png")
plt.show(block=False)
