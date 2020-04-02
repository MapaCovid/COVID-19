## Este script no es necesario usarlo después del 01 de Abril de 2020 

"""
Se realiza este script para construir las columnas "casos_nuevos" y 
"fallecidos_nuevos", sólo para los informes diarios previos (e incluído) al 
01 de Abril. Esto porque el minsal antes del 25 de marzo no indicaba los 
"casos nuevos", sino que solo los casos totales. Lo mismo para los fallecidos, 
y hasta el 01 de Abril no se estaban calculando los nuevos fallecidos al 
importar los datos.

La gracia es que a partir de ahora (desde el 02 de abril en adelante), al 
generar el informe diario en CSV se calculen automáticamente los 
fallecidos_nuevos sin tener que arreglar después 
los informes (los casos_nuevos ahora los está publicando directamtne el minsal.)
"""