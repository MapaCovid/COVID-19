# El Repositorio COVID-19 Chile
**¿Qué?:** Somos un grupo de voluntarios. Queremos ser la plataforma de mayor cantidad de datos y herramientas de análisis de datos relativas al COVID-19 en Chile.

**¿Para qué?:** Para tener los recursos necesarios para poder mostrar claramente lo que está pasando, y poder correr modelos matemáticos y epidimiológicos. Todo con el objetivo de frenar el avance del coronavirus en Chile.

**¿Cómo puedo aportar?:** No necesitas ningún conocimiento previo, sólo motivación! Lee más abajo

# Los Datos
## ¿Qué datos tienen actualmente?
- Datos a nivel **regional y nacional**:
	- [Consolidado_COVID19_Chile_Regiones.CSV](https://github.com/YachayData/COVID-19/blob/master/Consolidado_COVID19_Chile_Regiones.CSV) - Por cada día desde el 02 de Marzo: casos nuevos y totales, fallecidos nuevos y totales. Para nivel país, recuperados nuevos y recuperados totales.
- Datos a nivel **comunal**:
	- [Consolidado_COVID19_Chile_Comunas.CSV](https://github.com/YachayData/COVID-19/blob/master/Consolidado_COVID19_Chile_Comunas.CSV) - Por cada día desde el 02 de Marzo: casos nuevos y totales.

Además, tenemos diversos formatos útiles para distintas aplicaciones. Para más información, [sobre cómo se estructuran los datos disponibles, revisa la documentación aquí ](https://github.com/YachayData/COVID-19/blob/master/SobreLosDatos.md)

## ¿Qué nueva información queremos incluír?
Hay mucha más información disponible que nos gustaría incluír. A continuación, encontrarás una lista de la nueva información a incluír, con sus enlaces a los hilos de discusión.

- [Datos de camas UCI](https://github.com/jorgeperezrojas/covid19-data/blob/master/csv/pacientes_en_uci.csv)
- [Datos de cuarentena por comuna y por fecha](https://github.com/YachayData/COVID-19/issues/3)
- [Número de tests realizados por fecha](https://github.com/YachayData/COVID-19/issues/2)
- [Contaminación](https://github.com/YachayData/COVID-19/issues/8)
- [Información demográfica]()

# ¿Cómo puedo aportar?
Esta es una plataforma para que todas y todos puedan aportar! **Sin importar 


Para algunas, hemos logrado automatizar el proceso de extracción de estos datos. Pero es algo que requiere trabajo hacer. Para otro tipo de información, todavía se tienen que extraer "a mano", y para otros, todavía necesitamos ayuda para encontrar las fuentes. Para todo eso, **se necesita tu ayuda!**. 


Estamos trabajando para incluír la información demográfica y medidas (fechas de las cuarentenas, cordones sanitarios y otros eventos que puedan permitir hacer análisis de las medidas tomadas por la autoridad.

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


	

