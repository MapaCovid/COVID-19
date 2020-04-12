# ¿Cómo se estrucura la información?
## La información consolidada.
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
