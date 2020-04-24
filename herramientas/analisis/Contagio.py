import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

data = [1, 3, 4, 5, 7, 11, 13, 17, 23, 33, 43, 61, 75, 156, 201, 238, 342, 434, 537, 632, 746, 923, 1142, 1306, 1610, 
1909, 2139, 2449, 2738, 3031, 3404, 3737, 4161, 4471, 4815, 5116, 5546, 5972, 6501, 6927, 7213, 7525, 7917, 8273, 8807, 
9252, 9730, 10088, 10507, 10832, 11296]

# función de Gompertz
import datetime
numdays = len(data)

base = datetime.datetime.today()
date = [base - datetime.timedelta(days=x) for x in range(numdays)]



def f(x,a,b,c):
    return a*np.exp(-b*np.exp(-c*x))

# derivada de función de Gompertz 

def der_f(x,a,b,c):
    return a*b*c*np.exp(-(b*np.exp(-c*x) + c*x))

x = [float(i) for i in range(len(data))]
y = [float(i) for i in data]

# data optima para regresión y ajuste 


color_blue = tuple(np.array([70, 78, 254])/255.)
color_red = tuple(np.array([226, 69, 6])/255.)

fl_x = np.array(range(3,len(data)), dtype = np.longdouble)
fl_y = np.array(data[3:], dtype = np.longdouble)

popt, pcov = curve_fit(f, fl_x, fl_y, maxfev = 9999999)

# gráfico integrado (rango modelado + proyección)

d_proy = 70 # días de proyección
date_proy = [base + datetime.timedelta(days=x) for x in range(d_proy)]



"""
fig = plt.figure(figsize=(8,7))


t = np.linspace(0, len(data)-1, num = len(data)*5)

plt.plot([0,len(data)-1+d_proy,],[popt[0],popt[0]],'--', color=color_blue)
plt.plot([len(data)-1,len(data)-1],[0,popt[0]],'--.',color='gray')

plt.plot(t,f(t,*popt), 'r', label = 'Fit Modelado')
#plt.plot(t,der_f(t,*popt),'b', label = 'Contagio diario (rango modelado)')

t_proy = np.linspace(len(data)-1, len(data)-1+d_proy, num = d_proy*5)

plt.plot(t_proy,f(t_proy,*popt), 'r--', label = 'Fit Proyectado')
#plt.plot(t_proy,der_f(t_proy,*popt),'b--', label = 'Contagio diario (rango proyectado)')

plt.ylim(-500,20000)

plt.plot(x,y,'k^', label = 'Casos Totales')
ticks = np.array([10,30,50,70,90, 110])
plt.xticks(ticks, ['13/3', '2/4', '22/4', '12/5', '1/6','21/6'], fontsize=12)
plt.yticks([0, 5000, 10000, 15000, 20000],['0', '5,000', '10,000', '15,000', '20,000'], fontsize=12)
plt.title('Modelo de contagio Gompertz COVID-19 Chile', fontsize=14)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Casos Totales Confirmados', fontsize=14)
#plt.legend(loc = 'best', fontsize = 'x-small')
plt.grid(linestyle = '--')
plt.legend(fontsize=14)
# Hoy = 50

plt.show(block=False)
"""

fig = plt.figure(figsize=(8,7))


t = np.linspace(0, len(data)-1, num = len(data)*5)

plt.plot([0,len(data)-1+d_proy,],[popt[0],popt[0]],'--', color=color_blue)
plt.plot([len(data)-1,len(data)-1],[0,550],'--.',color='gray')

plt.plot(t,der_f(t,*popt), 'r', label = 'Fit Modelado')

t_proy = np.linspace(len(data)-1, len(data)-1+d_proy, num = d_proy*5)


plt.plot(t_proy,der_f(t_proy,*popt), 'r--', label = 'Fit Proyectado')
plt.ylim(-50,600)

plt.plot(x[1:],np.diff(y),'k^', label = 'Casos Diaros')
ticks = np.array([10,30,50,70,90, 110])
plt.xticks(ticks, ['13/3', '2/4', '22/4', '12/5', '1/6','21/6'], fontsize=12)
plt.yticks(fontsize=12)
plt.title('Modelo de contagio Gompertz COVID-19 Chile', fontsize=14)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Casos Confirmados Diarios', fontsize=14)
plt.legend(fontsize=14)
plt.grid(linestyle = '--')
plt.show(block=False)

