import numpy as np
import matplotlib.pyplot as plt
import pandas
import os
from matplotlib import font_manager as fm, rcParams
fig = plt.figure(figsize=(7,7))
### Post colaboración Olivia Bordeu y Nacho Oliva.
df = pandas.read_csv("asgdpPunto.csv",sep=";",encoding= 'unicode_escape')
fpath = os.path.join(rcParams["datapath"],"../Montserrat-Regular.ttf")
prop = fm.FontProperties(fname="../Montserrat-Regular.ttf")
fname = os.path.split(fpath)[1]

color_blue = tuple(np.array([38, 53, 134])/255.)
# Make a fake dataset:
country = np.array(df.values[:,0])
FiscalStimulus = np.array(df.values[:,1])
GrossDebt = np.array(df.values[:,3])

height = FiscalStimulus

##PRIMERO ESTIMULO FISCAL SOBRE PIB POR PAIS ########################################################################################
## Recoletado de : https://www.segib.org/covid-19/

bars = country
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height,color=color_blue)

# Create names on the x-axis
plt.xticks(y_pos, bars)



plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Estímulo fiscal económico como (%) del PIB', fontproperties=prop, fontsize=12, labelpad= -4)
plt.xlabel('País', fontproperties=prop, fontsize=12)

plt.title(r"Estímulo fiscal económico COVID19 como porcentaje del PIB",fontproperties=prop, fontsize=12)
 


plt.savefig("outputFiscalStimulus.png")
# Show graphic
plt.show()

##SEGUNDO DEUDA BRUTA SOBRE PIB POR PAIS ############################################################################################
### IMF
fig = plt.figure(figsize=(7,7))
height= GrossDebt

# Create bars
plt.bar(y_pos, height,color=color_blue)
# Create names on the x-axis
plt.xticks(y_pos, bars)


plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Deuda Bruta País como (%) del PIB', fontproperties=prop, fontsize=12, labelpad= -4)
plt.xlabel('País', fontproperties=prop, fontsize=12)

plt.title(r"Deuda Bruta como porcentaje del PIB",fontproperties=prop, fontsize=12)

plt.savefig("outputGrossDebt.png")
# Show graphic

plt.show()

##TERCERO ESTIMULO FISCAL SOBRE PIB POR PAIS G20 ############################################################################################
## BONUS / https://www.statista.com/statistics/1107572/covid-19-value-g20-stimulus-packages-share-gdp/
fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:
country = np.array(df.values[:,0])
FiscalStimulus = np.array(df.values[:,1])

height = FiscalStimulus
bars = country
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height,color=color_blue)
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(rotation=90, fontsize= 10, fontproperties=prop) 
plt.yticks(fontproperties=prop, fontsize= 12)

plt.subplots_adjust(bottom=0.15)
plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Estímulo fiscal económico como (%) del PIB', fontproperties=prop, fontsize=10, labelpad= -4)


plt.title(r"Estímulo fiscal económico COVID19 como porcentaje del PIB G20",fontproperties=prop, fontsize=12)
 
plt.savefig("outputFiscalStimulusG20.png")
# Show graphic
plt.show()


########### NUEVO POST
#1

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:
country = np.array(df.values[:,0])
FiscalStimulus = np.array(df.values[:,1])

height = FiscalStimulus
bars = country
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height,color=color_blue)
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(fontproperties=prop,rotation=48, fontsize= 6) 
plt.yticks(fontproperties=prop, fontsize= 12)


plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Estímulo fiscal económico como (%) del PIB', fontproperties=prop, fontsize=10, labelpad= -4)


plt.title(r"Estímulo fiscal económico COVID19 como porcentaje del PIB G20",fontproperties=prop, fontsize=12)
 
plt.savefig("outputFiscalStimulusG20covid.png")
# Show graphic
plt.show()

plt.close('all')
# Numero 1 COVID
#############################2

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:
country = np.array(df.values[:,0])

country = np.array([r'Japón',r'EE-UU','Australia','Canada','Brasil','Francia','Alemania','Un. Europea', 'Argentina', 'Arabia Saud.', 'Rusia', 'Indonesia', 'China', r'Turquía', 'Italia', 'India', r'México'])
FiscalStimulus = np.array(df.values[:,1])

country = np.append(country, 'Chile')
FiscalStimulus = np.append(FiscalStimulus, 6.7)

arrsort = FiscalStimulus.argsort()
FiscalStimulus1 = FiscalStimulus[arrsort[::-1]]
country1 = country[arrsort[::-1]]

height = np.array(FiscalStimulus1,dtype=float)
bars = country1
y_pos = np.arange(len(bars))


import matplotlib.colors as mcolors
from matplotlib import cm

greens = cm.get_cmap('bwr')

test = (np.arange(18)+4)/18. #1 - (height - 6.7)
#test[2:] = np.arange(16)/ 30. + 0.5

#h2 = height / height.max() 
#h2 = h2 / h2[2]

#test2 = test - test[2] + 0.5

colors = greens(test)
colors[5, :] = np.array([0,0,0,1])

# Create bars
plt.bar(y_pos, height,color=colors)
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(rotation=90, fontsize= 10, fontproperties=prop) 
plt.yticks(fontproperties=prop, fontsize= 12)



plt.subplots_adjust(bottom=0.15)

plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Estímulo fiscal económico como (%) del PIB', fontproperties=prop, fontsize=12, labelpad=0)
plt.xlim(-.75, 17.75)

plt.title(r"Estímulo fiscal económico COVID-19 como porcentaje del PIB G20",fontproperties=prop, fontsize=12)
 
plt.savefig("outputFiscalStimulusG20Lehman0.png")
# Show graphic
plt.show()

"""
plt.close()


# Numero 1
#############################2

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:
country = np.array(df.values[:,0])

country = np.array([r'Japón',r'EE-UU','Australia','Canada','Brasil','Francia','Alemania','Un. Europea', 'Argentina', 'Arabia Saud.', 'Rusia', 'Indonesia', 'China', r'Turquía', 'Italia', 'India', r'México'])
FiscalStimulus = np.array(df.values[:,1])

country = np.append(country, 'Chile')
FiscalStimulus = np.append(FiscalStimulus, 2.8)

arrsort = FiscalStimulus.argsort()
FiscalStimulus1 = FiscalStimulus[arrsort[::-1]]
country1 = country[arrsort[::-1]]

height = np.array(FiscalStimulus1,dtype=float)
bars = country1
y_pos = np.arange(len(bars))


import matplotlib.colors as mcolors
from matplotlib import cm

greens = cm.get_cmap('bwr')

test = (np.arange(18)+1)/18. #1 - (height - 6.7)
#test[2:] = np.arange(16)/ 30. + 0.5

#h2 = height / height.max() 
#h2 = h2 / h2[2]

#test2 = test - test[2] + 0.5

colors = greens(test)
colors[8, :] = np.array([0,0,0,1])

# Create bars
plt.bar(y_pos, height,color=colors)
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(rotation=90, fontsize= 10, fontproperties=prop) 
plt.yticks(fontproperties=prop, fontsize= 12)



plt.subplots_adjust(bottom=0.15)

plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Estímulo fiscal económico como (%) del PIB', fontproperties=prop, fontsize=12, labelpad=0)
plt.xlim(-.75, 17.75)

plt.title(r"Estímulo fiscal económico Crisis 2008 como porcentaje del PIB G20",fontproperties=prop, fontsize=12)
 
plt.savefig("outputFiscalStimulusG20Lehman.png")
# Show graphic
plt.show()


plt.close()


# Numero 2
#############################3 BONUS DIFERENCIA

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008_diff.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:
#country = np.array(df.values[:,0])
FiscalStimulus = np.array(df.values[:,1])

height = FiscalStimulus
height = np.append(height, 3.9)

arrsort = height.argsort()
FiscalStimulus2 = height[arrsort[::-1]]
country2 = country[arrsort[::-1]]


bars = country2
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos[:11], FiscalStimulus2[:11],color='g')
plt.bar(y_pos[11:], FiscalStimulus2[11:],color='r')
plt.bar(y_pos[6], FiscalStimulus2[6],color='k')
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(rotation=90, fontsize= 10, fontproperties=prop) 
plt.yticks(fontproperties=prop, fontsize= 12)

plt.subplots_adjust(bottom=0.15)
plt.xlim(-.75, 17.75)
plt.ylim(-9, 19.75)

plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Diferencia Estímulo como (%) PIB 2008 v/s 2020', fontproperties=prop, fontsize=12, labelpad= 0)
#plt.xlabel('País', fontproperties=prop, fontsize=12)

#plt.title(r"Diferencia de Estímulo fiscal económico como (%) del PIB 2008 v/s 2020",fontproperties=prop, fontsize=12)
plt.title(r"COVID v/s 2008 Estímulo Fiscal como % del PIB",fontproperties=prop, fontsize=12)
plt.savefig("outputDIFFCOVIDLEHMAN.png")
# Show graphic
plt.show()
plt.close()

############################4 BONUS

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008_debt.csv",sep=";",encoding= 'unicode_escape')
# Make a fake dataset:


FiscalStimulus = np.array(df.values[:,1])


height = FiscalStimulus
height = np.append(height, 27.9)

arrsort = height.argsort()
height3 = height[arrsort[::-1]]
country3 = country[arrsort[::-1]]


bars = country3
y_pos = np.arange(len(bars))



greens = cm.get_cmap('Oranges')

# Create bars
plt.bar(y_pos, height3,color=greens(1-np.arange(18)/18.))
plt.bar(y_pos[-3], height3[-3],color='k')
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(rotation=90, fontsize= 10, fontproperties=prop) 
plt.yticks(fontproperties=prop, fontsize= 12)


plt.subplots_adjust(bottom=0.15)
plt.xlim(-.75, 17.75)

plt.title('This is a special font: {}'.format(fname), fontproperties=prop)

plt.ylabel('Deuda Bruta País como (%) del PIB', fontproperties=prop, fontsize=12, labelpad= 0)
#plt.xlabel('País', fontproperties=prop, fontsize=12)

plt.title(r"Deuda Bruta como porcentaje del PIB G20",fontproperties=prop, fontsize=12)

plt.savefig("outputGrossDebt_g20.png")
# Show graphic
plt.show()

"""