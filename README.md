# El Repositorio COVID-19 Chile
# Ahora los datos regionales actualizados automáticamente!
En este repositorio se encuentran se encuentran todos los datos disponibles relativos al COVID-19 en Chile, así como también las fuentes utilizadas (informes del minsal, colegio médico, etc...)
Para cada comuna y región, y para cada día: nuevos casos, casos totales, nuevos fallecidos, fallecidos totales, nuevos recuperados, recuperados totales. Estamos trabajando para incluír la información demográfica y medidas (fechas de las cuarentenas, cordones sanitarios y otros eventos que puedan permitir hacer análisis de las medidas tomadas por la autoridad.

## ¡Necesitamos ayuda! - ¿Cómo puedo aportar?
Hay mucha información todavía que se puede incluír en este repositorio. Y muchas formas de analizar la información y sacar observaciones o conclusiones. ¡Para eso necesitamos ayuda!

Los temas en los cuales estamos trabajando los estamos poniendo en Issues
https://github.com/YachayData/COVID-19/issues
Puedes comentar libremente!

Puedes desde ya clonar este git y proponer cambios! Pero no tienes que saber programar para ayudar, basta con tener nuevas ideas, aportar con nuevas fuentes, saber leer informes y transcribirlos en un GoogleDocs / Google Drive o un Excel.

Si tienes dudas cómo aportar, métete al grupo de Whatsapp https://chat.whatsapp.com/CUBbQK40HTTBmFoLszaG5S
También puedes escribirnos en:
* Instagram instagram.com/yachay.data
* Twitter https://twitter.com/YachayD
* Facebook https://www.facebook.com/yachay.data/


## ¿Cómo se estrucura la información?

### La información consolidada:
* Consolidado_COVID19_Chile_Regiones.CSV Series de Tiempos por Regiones con:
	* fecha: formato YYYY-MM-DD
	* id_reg: ID de la Región (número de la región, siguiendo metodología antigua)
	* nombre_region: Nombre de la Región, sin tildes ni Ñ
	* casos_nuevos: Número de nuevos casos confirmados del día
	* casos_totales: Casos confirmados acumulados a la fecha
	* fallecidos_nuevos: Número de fallecidos del día
	* fallecidos_totales: Fallecidos acumulados a la fecha
	* recuperados_nuevos: (Por ahora no lo estamos usando)
	* recuperados_totales: (Por ahora no lo estamos usando)

* Consolidado_COVID19_Chile_Comunas.CSV. Series de Tiempos por Comunas con:
	* fecha: formato YYYY-MM-DD
	* id_reg: ID de la Región (número de la región, siguiendo metodología antigua)
	* nombre_region: Nombre de la Región, sin tildes ni Ñ
	* id_comuna:
	* nombre_comuna:
	* casos_nuevos: Número de nuevos casos confirmados del día
	* casos_totales: Casos confirmados acumulados a la fecha
	
Si te interesa sólo un dato, puedes encontrar la matriz pivoteada para ese dato específico, indexada por región/comuna y fecha, donde los datos (ej. casos totales) se encontrarán en una columna por cada fecha. 


### Fuentes y Herramientas

* * /Herramientas  - Estarán los scripts creados para analizar los datos, o para construir las Series de Tiempos a partir de los informes CSV que están en /informes_minsal
* /informes_minsal - Informes del Ministerio de Salud, tanto en PDF como en CSV


	

