#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:52:21 2020

@author: esteban
"""

from extraerDatosRegiones import extraerDatosRegiones
from consolidarCSV import consolidarCSVRegiones, consolidarCSVComunas
from gitPullPush import gitPull, gitPush
from descargadorInformesEPI import descargadorInformesEPI
from extraerDatosInformeEPI import extraerDatosInformeEPI

(actualizacionBoolRegiones,fechaActualizacionRegiones)=extraerDatosRegiones()
(actualizacionBoolComunas,fechaActualizacionComunas)=descargadorInformesEPI

#Primero para las Regiones
if actualizacionBoolRegiones:
    # la función extraerDatoRegiones devuelve True si extrajo algo
    # devuelve False si ya estábamos actualizados
    print('Tenemos nuevos datos por Regiones, vamos a consolidar.')
    consolidarCSVRegiones()
    gitPull
    mensajeCommit='auto-update Regiones'+fechaActualizacionRegiones
    gitPush(mensajeCommit)
    
if actualizacionBoolComunas:
    print('Tenemos nuevos datos por Comunas')
    
    print('Primero vamos a extraer los datos de los PDFs')
    extraerDatosInformeEPI()
    consolidarCSVComunas()
    git pull
    mensajeCommit='auto-update Informe EPI'+fechaActualizacionComunas
    gitPush(mensajeCommit)
    
    
    
