# ¿Cómo se estrucura la información disponible?
## ¿Cómo se obtiene la información?
- **Extracción:** Primero, la información se extrae a la carpeta `/datos` de las fuentes disponibles en `/fuentes`. 
- **Consolidación:** A partir de los datos en CSV disponibles en la carpeta `/datos` , estos se consolidan en la carpeta raíz `/`

## ¿Qué archivos se crean y cuál es su formato?
Identificamos dos tipos de manera de mostrar los datos
### 1. Archivos de Datos Consolidados
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
	
### 2. Archivos de Datos específicos
 	COVID19_Chile_Comunas-casos_totales.CSV
	COVID19_Chile_Comunas-tasa.CSV
	COVID19_Chile_Regiones-casos_nuevos.CSV
	COVID19_Chile_Regiones-casos_totales.CSV
	COVID19_Chile_Regiones-fallecidos_nuevos.CSV
	COVID19_Chile_Regiones-fallecidos_totales.CSV
	COVID19_Chile_Regiones-recuperados_nuevos.CSV
	COVID19_Chile_Regiones-recuperados_totales.CSV
