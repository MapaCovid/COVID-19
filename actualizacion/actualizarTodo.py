#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:52:21 2020

@author: esteban
"""

from extraerDatosRegiones import extraerDatosRegiones
from consolidarCSV import consolidarCSV
from gitPullPush import gitPull, gitPush

(actualizacionBool,fechaActualizacion)=extraerDatosRegiones()
if actualizacionBool:
    # la función extraerDatoRegiones devuelve True si extrajo algo
    # devuelve False si ya estábamos actualizados
    print('Tenemos nuevos datos, vamos a consolidar.')
    consolidarCSV()
    gitPull
    mensajeCommit='actualización automática '+fechaActualizacion
    gitPush(mensajeCommit)
    
    
