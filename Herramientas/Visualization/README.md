# Dashboard

Este dashboard está programado usando el framework Dash de Plotly. La referencia a la mayoría de sus componentes
puede ser encontrada en la documentación oficial de plotly.

Sobre los datos

- Para la carga de datos se asume que el directorio relativo de los datos es /informes_minsal/informes_diarios_Region_CSV
y /informes_minsal/informes_diarios_Comuna_CSV. Con esos mismos nombres.

- Para la lectura de los datos se asume que cada archivo .csv en esa carpeta posee archivos cuyo nombre inicia con la
fecha en el formato YYYY-MM-DD.

## Uso:

Para lanzar la aplicación simplemente dirígete a esta carpeta e instala los paquetes necesarios.

````
pip install -r requirements.txt
````

Luego, para iniciar la aplicación ejecuta desde la consola.
````
python main.py
````
Ya podras utilizarla desde tu navegador visitando localhost en el puerto que se indicará en la consola.

Esta herramienta sigue en desarrollo.