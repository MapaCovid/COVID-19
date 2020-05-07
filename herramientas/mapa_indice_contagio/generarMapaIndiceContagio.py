#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:13:28 2020

@author: esteban
"""

from mapaIndiceContagio import mapaIndiceContagio

fechaAAnalizar='2020-05-04'
lista_indices=['riesgo_activos',
               'var%1periodo',
               'riesgo_activos_variacion']

mapaIndiceContagio(fechaAAnalizar,
                   lista_indices)
