#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:19:28 2020

@author: esteban
"""

import numpy as np
import pandas as pd
import datetime
from datetime import timedelta, date

## Primero abro los datos consolidados por comuna

path='../../'
nombre_archivo='COVID19_Chile_Comunas.CSV'

df = pd.read_csv(path+nombre_archivo)

# Queremos ver en cuánto han aumentado los casos totales
pivot= df.pivot_table(index='nombre_comuna',
         columns='fecha',
         values='casos_totales')
(((pivot['2020-04-01']-pivot['2020-03-30'])/pivot['2020-03-30'])*100).max()

pivot['2020-04-01']-pivot['2020-03-30']
pivot['cambio_porcentual']=(((pivot['2020-04-01']-pivot['2020-03-30'])/pivot['2020-03-30'])*100).replace(np.inf,0)


pivot.sort_values(by='cambio_porcentual')
