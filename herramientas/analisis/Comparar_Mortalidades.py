import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#df = pd.read_csv("ts_recov.csv")

name = "../../datos/datos_johns_hopkins/time_series_covid19_confirmed_global.csv"

df = pd.read_csv(name)

# get indices
#### Attention france 
#ifrance = (( df[['Country/Region']] == 'Brazil').values).argmax()
#ichile = ( df[['Country/Region']] == 'Chile').values.argmax()
#iitaly = ( df[['Country/Region']] == 'Italy').values.argmax()
#ispain = ( df[['Country/Region']] == 'Spain').values.argmax()
#
#chile = df.iloc[ichile]
#france = df.iloc[ifrance]
#italy = df.iloc[iitaly]
#spain = df.iloc[ispain]


dfr = df[df['Country/Region'] == 'France']
dfr = dfr[dfr['Province/State'].isnull()]

dch = df[df['Country/Region'] == 'Chile']
dus = df[df['Country/Region'] == 'US']
dbr = df[df['Country/Region'] == 'Brazil']
dit = df[df['Country/Region'] == 'Italy']
dsp = df[df['Country/Region'] == 'Spain']

frd = np.array(dfr.values[0, 4:], dtype=float)
chd = np.array(dch.values[0, 4:], dtype=float)
usd = np.array(dus.values[0, 4:], dtype=float)

brd = np.array(dbr.values[0, 4:], dtype=float)
itd = np.array(dit.values[0, 4:], dtype=float)

spd = np.array(dsp.values[0, 4:], dtype=float)


name = "../../datos/datos_johns_hopkins/time_series_covid19_deaths_global.csv"

Ddf = pd.read_csv(name)

# get indices
#### Attention france 
#ifrance = (( df[['Country/Region']] == 'Brazil').values).argmax()
#ichile = ( df[['Country/Region']] == 'Chile').values.argmax()
#iitaly = ( df[['Country/Region']] == 'Italy').values.argmax()
#ispain = ( df[['Country/Region']] == 'Spain').values.argmax()
#
#chile = df.iloc[ichile]
#france = df.iloc[ifrance]
#italy = df.iloc[iitaly]
#spain = df.iloc[ispain]


Ddfr = Ddf[Ddf['Country/Region'] == 'France']
Ddfr = Ddfr[Ddfr['Province/State'].isnull()]

Ddch = Ddf[Ddf['Country/Region'] == 'Chile']
Ddus = Ddf[Ddf['Country/Region'] == 'US']
Ddbr = Ddf[Ddf['Country/Region'] == 'Brazil']
Ddit = Ddf[Ddf['Country/Region'] == 'Italy']
Ddsp = Ddf[Ddf['Country/Region'] == 'Spain']

Dfrd = np.array(Ddfr.values[0, 4:], dtype=float)
Dchd = np.array(Ddch.values[0, 4:], dtype=float)
Dusd = np.array(Ddus.values[0, 4:], dtype=float)

Dbrd = np.array(Ddbr.values[0, 4:], dtype=float)
Ditd = np.array(Ddit.values[0, 4:], dtype=float)

Dspd = np.array(Ddsp.values[0, 4:], dtype=float)




#frd[-1] = 12210
#itd[-1] = 18279
#brd[-1] = 941
#chd[-1] = 57
#spd[-1] = 15238
#usd[-1] = 16444

frd /= 66.99 
itd /= 60.46 
brd /= 46.66
chd /= 18.05
spd /= 46.66
usd /= 327.2


Dfrd /= 66.99 
Ditd /= 60.46 
Dbrd /= 46.66
Dchd /= 18.05
Dspd /= 46.66
Dusd /= 327.2


pfrd = frd[frd >= 1]
pitd = itd[itd >= 1]
pbrd = brd[brd >= 1]
pchd = chd[chd >= 1]
pspd = spd[spd >= 1]
pusd = usd[usd >= 1]

pDfrd = Dfrd[frd >= 1]
pDitd = Ditd[itd >= 1]
pDbrd = Dbrd[brd >= 1]
pDchd = Dchd[chd >= 1]
pDspd = Dspd[spd >= 1]
pDusd = Dusd[usd >= 1]


ppfrd = pfrd[pDfrd >= .1]
ppitd = pitd[pDitd >= .1]
ppbrd = pbrd[pDbrd >= .1]
ppchd = pchd[pDchd >= .1]
ppspd = pspd[pDspd >= .1]
ppusd = pusd[pDusd >= .1]

ppDfrd = pDfrd[pDfrd >= .1]
ppDitd = pDitd[pDitd >= .1]
ppDbrd = pDbrd[pDbrd >= .1]
ppDchd = pDchd[pDchd >= .1]
ppDspd = pDspd[pDspd >= .1]
ppDusd = pDusd[pDusd >= .1]

N = 40
points = np.arange(40) / 40  * 3.8
t = 10 ** points
tt = t  / 10.
plt.plot(np.log10(t), np.log10(tt),':', color ='gray')

tt = t  / 100.
plt.plot(np.log10(t), np.log10(tt),':', color ='gray')

tt = t  / 100. * 6.3
plt.plot(np.log10(t), np.log10(tt),'--', color ='gray')
plt.text(1.2,.7, r'10%' , fontsize=18, color = 'gray')
plt.text(3.4,2, r'6.3%', fontsize=18, color = 'gray')
plt.text(3,.7, r'1%' , fontsize=18, color = 'gray')
plt.scatter(np.log10(ppfrd), np.log10(ppDfrd), label = 'Francia', color ='C9')
plt.scatter(np.log10(ppusd), np.log10(ppDusd), label = 'US', color ='green')
plt.scatter(np.log10(ppspd), np.log10(ppDspd), label = r'España', color ='orange')
plt.scatter(np.log10(ppbrd), np.log10(ppDbrd), label = 'Brasil', color ='blue')
plt.scatter(np.log10(ppchd), np.log10(ppDchd), label = 'Chile', color ='k')

plt.text(1.2,-1.8, r'.. : Tasa de Mortalidad en %' , fontsize=18, color = 'gray')
plt.text(1.2,-2.1, r'-- : "" Mundial (6.3%)' , fontsize=18, color = 'gray')
plt.title(r'Evolución de las Muertes vs. Número de Casos (loglog)', fontsize=14)
plt.xticks([0, 1,2,3],[1, 10 , 100 , 1000], fontsize=14)
plt.yticks([-1,0,1,2], [0.1,1,10,100], fontsize=14)


plt.xlabel(r'Casos por millón de habitantes (log)', fontsize=14)
plt.ylabel(r'Muertes por millón de habitantes (log)', fontsize=14)


plt.legend(fontsize=14)
plt.show(block=False)
