#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:52:21 2020

@author: esteban
"""

from extraerDatosRegiones import extraerDatosRegiones
from consolidarCSV import consolidarCSVRegiones
from gitPullPush import gitPull, gitPush

(actualizacionBoolRegiones,fechaActualizacionRegiones)=extraerDatosRegiones()
#(actualizacionBoolComunas,fechaActualizacionComunas)=descargadorInformesEPI

#Primero para las Regiones
if actualizacionBoolRegiones:
    # la función extraerDatoRegiones devuelve True si extrajo algo
    # devuelve False si ya estábamos actualizados
    print('Tenemos nuevos datos por Regiones, vamos a consolidar.')
    consolidarCSVRegiones()
    gitPull
    mensajeCommit='auto-update Regiones'+fechaActualizacionRegiones
    gitPush(mensajeCommit)
