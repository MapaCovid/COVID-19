import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Fit polinomial y exponencial de la cantidad de casos confirmados en Chile según Johns Hopkins

name = "../../datos/datos_johns_hopkins/time_series_covid19_confirmed_global.csv"


# Importar los datos 

df = pd.read_csv(name)


# Seleccionar los datos de Chile
dch = df[df['Country/Region'] == 'Chile']

# Seleccionar la serie de tiempo 
ch = np.array(dch.values[0, 4:], dtype=float)



# Modificar un error en la base de datos:
ch[57] = 342

# Obtener los días
dia = (df.columns)

# Agregar un dato faltante para el día de hoy si necesario
#ch = np.append(ch, 3000) 
#dia = np.append(dia, '4/1/20')


t = np.arange(ch.shape[0]) + 1
dia = np.array(dia, dtype=np.str)

# elegir los días a partir del primer caso: ch positivo (chp)
chp = ch[ch >= 1] 
diap = dia[-chp.shape[0]:]
tp = np.arange(chp.shape[0]) + 1


# Regresiones
log_tp = np.log(tp)
log_t = np.log(t)
log_y_chile = np.log(ch)
log_y_chilep = np.log(chp)

# Fit exponencial al día de hoy
curve_fit = np.polyfit(tp, log_y_chilep, 1)

# Fit polinomial al día de hoy
curve_poly = np.polyfit(log_tp[-10:], log_y_chilep[-10:], 1)

# valores t de train + predict:
t1 = np.arange(tp[-1] + 11)

# valores t de predict:
t2 = np.arange(11) + tp[-1]  + 1

# Predicciones:
y = np.exp(curve_fit[1]) * np.exp(curve_fit[0]*t1)
ypoly = t1 ** curve_poly[0] * np.exp(curve_poly[1]) 


# Plot
fig = plt.figure(figsize=(9,8))

plt.plot(t1, np.log10(ypoly), label=r'Predicción polinomial hoy: $\sim x^{ %f}$' %curve_poly[0],  color='blue', linewidth=2)
plt.plot(t1, np.log10(y), '--',label=r'Predicción exponencial hoy: $\sim e^{%f x}$' %curve_fit[0], color='orange', linewidth=2)
plt.plot(tp, np.log10(chp),'o', color='k', label='Casos Reales')
plt.legend(fontsize=14)
#plt.xticks([2,7, 12,17,22, 27, 32, 37,42], ['5/3', '10/3', '15/3', '20/3', '25/3', '30/3','5/4','10/4, 15' ], fontsize=14)
plt.yticks([0, 1, 2, 3, 4, 5], [1, 10, 20, 100 ,1000 , 10000, 100000], fontsize =14)
plt.xlabel(r'Días desde el primer Caso', fontsize=14)
plt.ylabel(r'Casos (Escala logarítmica)', fontsize=14)

plt.show()

# Error cuadrado medio:

erre = np.sum((y[:chp.shape[0]]- chp)**2) /chp.shape[0]
errp = np.sum((ypoly[:chp.shape[0]]- chp)**2) /chp.shape[0]
