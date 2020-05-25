import numpy as np
import matplotlib.pyplot as plt
import pandas
import os
from matplotlib import font_manager as fm, rcParams
from matplotlib import cm

fig = plt.figure(figsize=(7,7))
### Post colaboración Nico Valenzuela Levi
fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(fname="../Montserrat-Regular.ttf")
fname = os.path.split(fpath)[1]

labels = 'Si', 'No', 'Sin data'
sizes = [54.8, 39.4, 5.8]
explode = (0, 0.1, 0) 
greens = cm.get_cmap('Set2')
test= [0.66,0.99,0.33]
colors = greens(test)
fig, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,autopct='%1.1f%%',colors=colors,labeldistance=1.05,
        shadow=False, startangle=252.5)
#252
#90
ax1.axis('equal') 
plt.title(r"Municipalidades con servicio de reciclaje en operación",fontproperties=prop, fontsize=16)
plt.ylabel('345 municipalidades. Chile 2018', fontproperties=prop, fontsize=14, labelpad= -4)
plt.xlabel('(Valenzuela-Levi, 2019)', fontproperties=prop, fontsize=12)
fig = plt.gcf()
fig.set_size_inches(7,7)
plt.savefig("outputNicoValenzuela.png")
plt.show()

