import pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import datetime
from scipy.ndimage.interpolation import shift

df = pandas.read_csv("Global_Mobility_Report (2).csv",sep=",",encoding= 'utf-8')
#SUBCONJUNTO A USAR CHILE 
df = df.loc[df['country_region'].str.match('Chile') == True]
regiones = df['sub_region_1'].unique()
#TOMAR LAS FECHAS DISPONIBLES PARA TRABAJARLAS
fecha= df['date'].unique()
valores= []
aux=0

#MODIFICAR LAS FECHAS, A FORMATO '%d-%m-%y MAS ADAPTABLE A FORMATO IG
newdates=[]
for date in fecha:
	ndate={}
	ndate=str(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%y'))
	print(ndate)
	newdates.append(ndate)
print(newdates)
print("revision fecha")
print(newdates[27])
for i in regiones:
	values={}
	#Reviso para cada region y saco los valores del arreglo
	linea = df.loc[df['sub_region_1'].str.match(str(i)) == True]
	#ACA HAY VARIAS OPCIONES INTERESANTES PARA VER
	#transit_stations_percent_change_from_baseline
	#grocery_and_pharmacy_percent_change_from_baseline
	#parks_percent_change_from_baseline
	#workplaces_percent_change_from_baseline
	#residential_percent_change_from_baseline
	values=linea['retail_and_recreation_percent_change_from_baseline']
	valores.append(values)
	#print(valores)
print(valores)

#16 regiones
antofa = np.array(valores[1])
araucania = np.array(valores[2])
arica = np.array(valores[3])
atacama = np.array(valores[4])
aysen = np.array(valores[5])
biobio = np.array(valores[6])
coquimbo = np.array(valores[7])
loslagos = np.array(valores[8])
losrios = np.array(valores[9])
magallanes = np.array(valores[10])
maule = np.array(valores[11])
nuble = np.array(valores[12])
ohi = np.array(valores[13])
rm = np.array(valores[14])
tarapaca = np.array(valores[15])
valparaiso = np.array(valores[16])

#ex funcion : moving_average(array, numero_de_periodos)
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

ant7 = moving_average(antofa,7)
#print("este archivo tiene tantos # "+str(len(ant5)))
arauc7 = moving_average(araucania,7)
valpo7 = moving_average(valparaiso,7)
rm7 = moving_average(rm,7)
maga7 = moving_average(magallanes,7)
mau7 = moving_average(maule,7)
nuble7 = moving_average(nuble,7)
ohi7 = moving_average(ohi,7)

### SHIFT
#shift(ant7,)
ant7=shift(ant7,6)
arauc7=shift(arauc7,6)
valpo7=shift(valpo7,6)
rm7=shift(rm7,6)
maga7=shift(maga7,6)
mau7=shift(mau7,6)
nuble7=shift(nuble7,6)
ohi7=shift(ohi7,6)

#print(len(ant7))
#print(len(antofa))


#### FORMATO YACHAY
fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(fname="../Montserrat-Regular.ttf")
fname = os.path.split(fpath)[1]

#ploteo de figura y líneas
fig = plt.figure(figsize=(7,7))
plt.axhline(y=0, color='gray', linestyle='-')
#plt.plot(antofa,color = 'darkblue', lw=2)

plt.plot(rm7,color = 'darkblue', lw=2)
plt.plot(ant7,color = 'lavender', lw=2)
plt.plot(arauc7,color = 'royalblue', lw=2)
plt.plot(valpo7,color = 'cornflowerblue', lw=2)
plt.plot(maga7,color = 'lightsteelblue', lw=2)
plt.plot(mau7,color = 'slategrey', lw=2)
plt.plot(nuble7,color = 'forestgreen', lw=2)
plt.plot(ohi7,color = 'mediumaquamarine', lw=2)
plt.axvline(x=27, color = 'gray', linestyle = '--', linewidth = 2)
plt.text(28, 5, r'Cierre de escuelas 13/03', fontproperties=prop, fontsize=10, color = 'gray')
plt.axvline(x=33, color = 'gray', linestyle = '--', linewidth = 2)
plt.text(34, 1.5, r'Se declara Estado de Emergencia 19/03', fontproperties=prop, fontsize=10, color = 'gray')
#plt.plot(arica,color = 'darkblue', lw=2)
#plt.plot(atacama,color = 'darkgreen', lw=2)
#plt.plot(aysen,color = 'darkgreen', lw=2)
#plt.plot(biobio,color = 'darkgreen', lw=2)
#plt.plot(coquimbo,color = 'darkgreen', lw=2)
#plt.plot(loslagos,color = 'darkgreen', lw=2)
#plt.plot(losrios,color = 'darkgreen', lw=2)
#plt.plot(magallanes,color = 'darkgreen', lw=2)
#plt.plot(maule,color = 'darkgreen', lw=2)
#plt.plot(nuble,color = 'darkgreen', lw=2)
#plt.plot(ohi,color = 'darkgreen', lw=2)
#plt.plot(rm,color = 'darkgreen', lw=2)
#plt.plot(tarapaca,color = 'darkgreen', lw=2)
#plt.plot(valparaiso,color = 'darkgreen', lw=2)
#plt.plot(rm,marker='o',color = 'darkgreen', lw=2)
#plt.plot(araucania,marker='o',color = 'darkgreen', lw=2)
pop_a = mpatches.Patch(color='darkblue', label='RM')
pop_b = mpatches.Patch(color='lavender', label='Antofagasta')
pop_c = mpatches.Patch(color='royalblue', label='Araucanía')
pop_d = mpatches.Patch(color='cornflowerblue', label='Valparaíso')
pop_e = mpatches.Patch(color='lightsteelblue', label='Magallanes')
pop_f = mpatches.Patch(color='slategrey', label='Maule')
pop_g = mpatches.Patch(color='forestgreen', label='Ñuble')
pop_h = mpatches.Patch(color='mediumaquamarine', label='O´Higgins')

plt.xticks([0,12,24,36,48,60,72,84], [newdates[0],newdates[12],newdates[24],newdates[36],newdates[48],newdates[60],newdates[72],newdates[84]], fontproperties=prop)

plt.title(r'Reducción Movilidad (Comercio y Recreación), media móvil 7 días - Google', fontsize=16, fontproperties=prop)
plt.xlabel(r'Fecha', fontsize=14, fontproperties=prop)
plt.ylabel(r'Variación en (%) relativa a línea base entre 6 de Enero y 3 de Febrero', fontsize=16, fontproperties=prop)

###GLOSA y ETIQUETAS
plt.legend(handles=[pop_a,pop_b,pop_c,pop_d,pop_e,pop_f,pop_g,pop_h], prop = prop)
#Comercio y Recreación
#Parques
#Lugar de Trabajo
#Estaciones de Transporte
plt.savefig("outMOBILITYcomercio.png")
plt.show()