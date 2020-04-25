![Update Submodules](https://github.com/YachayData/COVID-19/workflows/Update%20Submodules/badge.svg)![Actualizar Comunas](https://github.com/YachayData/COVID-19/workflows/Actualizar%20Comunas/badge.svg) ![Actualizar Regiones](https://github.com/YachayData/COVID-19/workflows/Actualizar%20Regiones/badge.svg)
# El Repositorio COVID-19 Chile
**¿Qué?:** Somos un grupo de voluntarios. Queremos ser la plataforma de mayor cantidad de datos y herramientas de análisis de datos relativas al COVID-19 en Chile.

**¿Para qué?:** Para tener los recursos necesarios para poder mostrar claramente lo que está pasando, y poder correr modelos matemáticos y epidimiológicos. Todo con el objetivo de frenar el avance del coronavirus en Chile.

**¿Cómo puedo aportar?:** No necesitas ningún conocimiento previo, sólo motivación! Pero si sabes programar o quieres correr modelos, bienvenido eres también! **Existen  muchas formas de aportar** Lee más abajo en la sección [¿Cómo puedo aportar?](#cómo-puedo-aportar)

# Los Datos
## ¿Qué datos tienen actualmente?
- Datos a nivel **regional y nacional**:
	- [Consolidado_COVID19_Chile_Regiones.CSV](https://github.com/YachayData/COVID-19/blob/master/Consolidado_COVID19_Chile_Regiones.CSV) - Por cada día desde el 02 de Marzo: casos nuevos y totales, fallecidos nuevos y totales. Para nivel país, recuperados nuevos y recuperados totales.
- Datos a nivel **comunal**:
	- [Consolidado_COVID19_Chile_Comunas.CSV](https://github.com/YachayData/COVID-19/blob/master/Consolidado_COVID19_Chile_Comunas.CSV) - Por cada día desde el 02 de Marzo: casos nuevos y totales.

Además, tenemos diversos formatos útiles para distintas aplicaciones. Para más información, [sobre cómo se estructuran los datos disponibles, revisa la documentación aquí ](https://github.com/YachayData/COVID-19/blob/master/SobreLosDatos.md)

## ¿Qué nueva información queremos incluír?
Hay mucha más información disponible que nos gustaría incluír. A continuación, encontrarás una lista de la nueva información a incluír, con sus enlaces a los hilos de discusión.

- [Datos de camas UCI](https://github.com/YachayData/COVID-19/issues/11)
- [Datos de cuarentena por comuna y por fecha](https://github.com/YachayData/COVID-19/issues/3)
- [Número de tests realizados por fecha](https://github.com/YachayData/COVID-19/issues/2)
- [Contaminación](https://github.com/YachayData/COVID-19/issues/8)
- Información demográfica.
- Fechas y lugares de medidas como cuarentenas.

# ¿Cómo puedo aportar?
Esta es una plataforma para que todas y todos puedan aportar!
Para mejor coordinación [únete a nuestro grupo de Whatsapp aquí](https://chat.whatsapp.com/CUBbQK40HTTBmFoLszaG5S)

No necesitas saber programar para poder aportar. Algunas formas de ayudar son:

- **Aportando ideas** de nuevos datos para incluír o análisis para realizar: Para esto, **crea un nuevo tema** en la [Sección de Issues](https://github.com/YachayData/COVID-19/issues). O si no, simplemente coméntala en el grupo de Whatsapp.

- **Buscando fuentes** de los nuevos datos a incluír. Si tienes ideas de dónde se podrían obtener los datos, coméntalo en la [sección correspondiénte](https://github.com/YachayData/COVID-19/issues)!

- **Programando** la automatización de la extracción de los datos. O ya sea **manteniendo** los códigos ya escritos.  Para esto, por favor [revisa la documentación sobre la extracción de datos en /actualizacion](https://github.com/YachayData/COVID-19/tree/master/actualizacion)

- **Creando nuevas herramientas de análisis**. A partir de los datos se pueden observar muchísimas cosas! Para eso, revisa la [documentación en la sección de herramientas de análisis /herramientas](https://github.com/YachayData/COVID-19/tree/master/herramientas).

- **Creando nuevas herramientas de visualización de los datos** Par eso, revisa la [sección de Herramientas de Visualización más abajo en este documento](#herramientas-de-visualización)

# Fuentes
Todas las fuentes utilizadas en este repositorio están **indicadas y respaldadas** en la carpeta `/fuentes`. Luego, los datos son transcritos a la carpeta `/datos`. Para más información sobre las fuentes, [revisa la documentación de sobre las fuentes](https://github.com/YachayData/COVID-19/tree/master/fuentes). 

# Herramientas de visualización
Los datos son más fáciles de comprender si uno los visualiza! A continuación una lista de las herramientas de visualización Web que utilizan los datos de este repositorio:

- [www.mapacovid.cl](www.mapacovid.cl): Mapa de Visualización creado por [YachayData](https://github.com/YachayData/) usando el código de [Yi Liu](https://github.com/stevenliuyi/covid19/)
- [Dashboard de Rudy](https://github.com/YachayData/COVID-19/tree/master/herramientas/Visualization): Panel de visualización de datos desarrollado por [Rudy](https://github.com/rudyn2)

Si creas la tuya, no dudes en subirla a este repositorio en la carpeta `/herramientas/visualizacion` haciendo un pull request. O si tienes otro repositorio, crea un Issue avisando para que la incorporemos a esta lista!

# Análisis de Datos.
Para la mayoría de los análisis, hay que mezclar distintos tipos de información, hacer cálculos, correr modelos. Este repositorio no se limita a los datos, si no que también incorpora herramientas de análisis de datos Open Source. Estas se encuentran en la carpeta `/herramientas`. Para más información visita la [documentación en la sección de herramientas de análisis en la carpeta /herramientas](https://github.com/YachayData/COVID-19/tree/master/herramientas).
	

