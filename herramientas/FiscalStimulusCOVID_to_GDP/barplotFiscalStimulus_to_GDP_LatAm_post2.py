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


#############################2

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008.csv",sep=";",encoding= 'unicode_escape')
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


plt.title(r"Estímulo fiscal económico Crisis 2008 como porcentaje del PIB G20",fontproperties=prop, fontsize=12)
 
plt.savefig("outputFiscalStimulusG20Lehman.png")
# Show graphic
plt.show()

#############################3 BONUS DIFERENCIA

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008_diff.csv",sep=";",encoding= 'unicode_escape')
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

plt.ylabel('Diferencia Estímulo como (%) PIB 2008 v/s 2020', fontproperties=prop, fontsize=12, labelpad= -4)
#plt.xlabel('País', fontproperties=prop, fontsize=12)

plt.title(r"Diferencia de Estímulo fiscal económico como (%) del PIB 2008 v/s 2020",fontproperties=prop, fontsize=12)

plt.savefig("outputDIFFCOVIDLEHMAN.png")
# Show graphic
plt.show()

############################4 BONUS

fig = plt.figure(figsize=(7,7))
df = pandas.read_csv("g20_2008_debt.csv",sep=";",encoding= 'unicode_escape')
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

plt.ylabel('Deuda Bruta País como (%) del PIB', fontproperties=prop, fontsize=12, labelpad= -4)
#plt.xlabel('País', fontproperties=prop, fontsize=12)

plt.title(r"Deuda Bruta como porcentaje del PIB G20",fontproperties=prop, fontsize=12)

plt.savefig("outputGrossDebt_g20.png")
# Show graphic
plt.show()
