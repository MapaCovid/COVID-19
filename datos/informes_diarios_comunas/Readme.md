# Estructura de estos datos:

A continuación se presentan los datos transcritos de los [Informes EPIDIMIOLÓGICOS entregados por el MINSAL]() en el formato **EXACTO** que se entrega. Esto quiere decir que para las comunas en que existen menos de 4 casos, se infrorma '-', tal cual lo hace el minsal. El cálculo usando la tasa se realiza después.

Para las comunas no identificadas se usa el `id_region` y `nombre_region` correspondiente, pero se usa como comuna el nombre ""

- Nombre del archivo: **YYYY-MM-DD-InformeDiarioComunas-COVID19.csv**, donde YYY-MM-DD es la fecha del informe
- Estructura de los datos:
```
 id_region
nombre_region
id_comuna
nombre_comuna
poblacion
casos totales
tasa
```
