import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#df = pd.read_csv("ts_recov.csv")

# Importar los datos
name = "../../datos_johns_hopkins/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

df = pd.read_csv(name)

# Obtener datos de los paises que elegimos: 

dfr = df[df['Country/Region'] == 'France']
dfr = dfr[dfr['Province/State'].isnull()]

dch = df[df['Country/Region'] == 'Chile']
dus = df[df['Country/Region'] == 'US']
dbr = df[df['Country/Region'] == 'Brazil']
dit = df[df['Country/Region'] == 'Italy']
dsp = df[df['Country/Region'] == 'Spain']


# Modificar los datos erroneos de la base de datos
fr = np.array(dfr.values[0, 4:], dtype=float)
fr[50] = 2876
fr[52] = 4499
fr[53] = 5423
ch = np.array(dch.values[0, 4:], dtype=float)
ch[57] = 342
fr[50] = 2876

us = np.array(dus.values[0, 4:], dtype=float)
br = np.array(dbr.values[0, 4:], dtype=float)
br[51] = 98
it = np.array(dit.values[0, 4:], dtype=float)
it[50] = 15113

sp = np.array(dsp.values[0, 4:], dtype=float)
sp[50] = 3146


# Dividir por la población (millones)

fr /= 66.99 
it /= 60.46 
br /= 46.66
ch /= 18.05
sp /= 46.66
us /= 327.2


# Restringir a partir del caso 1

fr = fr[fr >= 1]
it = it[it >= 1]
br = br[br >= 1]
ch = ch[ch >= 1]
sp = sp[sp >= 1]
us = us[us >= 1]


# Plot 
fig = plt.figure(figsize=(8,8))

ti = np.arange(11)
plt.plot(ti, np.log10(2 ** ti), '--', color='gray')
ti = np.arange(20)
plt.plot(ti, np.log10(2 ** (ti/2.)), '--', color='gray')
ti = np.arange(30)
plt.plot(ti, np.log10(2 ** (ti/4.)), '--', color='gray')
ti = np.arange(30)
plt.plot(ti, np.log10(2 ** (ti/7.)), '--', color='gray')


plt.plot(np.log10(fr),'-o',linewidth=1, label = 'Francia', color ='C9')
plt.plot(np.log10(us),'-o',linewidth=2, label = 'US', color ='b')
plt.plot(np.log10(it),'-o',linewidth=1, label = 'Italia', color ='g')
plt.plot(np.log10(sp),'-o',linewidth=1, label = r'España', color ='orange')

plt.plot(np.log10(br),'-o',linewidth=2, label = 'Brasil', color ='r')
plt.plot(np.log10(ch),'-o',linewidth=2, label = 'Chile', color ='k')
plt.yticks([0, 1,2,3], ['1', '10', '100', '1000'], fontsize=12)
plt.xticks([0, 10, 20, 30], fontsize=14)

plt.xlabel(r'Días desde que se alcanza un caso por millón de habitantes', fontsize=14)
plt.ylabel(r'Casos confirmados por millón de habitantes', fontsize=14)
plt.legend(fontsize=14)

plt.legend(fontsize=14)


plt.show(block=False)
