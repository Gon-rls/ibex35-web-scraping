# Analisis del IBEX-35

Programa en Python que obtiene en tiempo real los datos de las 35 empresas que componen el indice bursatil IBEX-35, los procesa y genera automaticamente un informe ejecutivo y una hoja de calculo lista para analisis y visualizacion en Excel.

Autor: Gonzalo Rodriganez

---

## Descripcion

Este proyecto automatiza la obtencion y el analisis de los datos del IBEX-35 publicados en la web de CincoDias. A partir de esa informacion, genera de forma automatica:

- Un informe de texto (informe_ibex35.txt) con los datos mas relevantes de la jornada, listo para ser entregado a direccion.
- Una hoja de calculo (ibex35_datos.csv) con todos los datos de las 35 empresas organizados por columnas, que puede abrirse en Excel para filtrar, ordenar y crear graficos.

El objetivo es que la herramienta pueda ejecutarse a diario, sirviendo como un sistema de analisis rapido y automatizado para los directivos de una empresa de inversion, sin necesidad de revisar manualmente los datos del mercado.

---

## Para que sirve

- Ahorra tiempo en la recopilacion manual de datos bursatiles.
- Facilita la toma de decisiones al resumir automaticamente las empresas con mayor subida, mayor bajada, mayor y menor capitalizacion, y la mas atractiva por dividendo.
- Deja los datos preparados en formato tabular para su explotacion en Excel (graficos, filtros, dashboards).
- Puede integrarse en una rutina diaria de analisis financiero interno.

---

## Como funciona

### 1. Obtencion de datos
Se conecta a la web de CincoDias mediante:
- requests: realiza la peticion HTTP a la pagina, igual que un navegador.
- BeautifulSoup: analiza el HTML recibido para localizar la tabla del IBEX-35 (identificada por su clase CSS "bt shortable") y extraer los datos de cada empresa.

### 2. Limpieza y tratamiento de datos
Los datos llegan en formato numerico espanol (1.234,56) y se convierten al formato ingles (1234.56) mediante sustituciones de separadores de miles y decimales. Los valores vacios o con formato inesperado (como el PER o la rentabilidad por dividendo) se controlan con bloques try/except, asignando None cuando no es posible convertir el dato, evitando asi que el programa se detenga por errores.

De cada empresa se extrae:
- Nombre
- Precio actual (ultimo)
- Variacion del dia (%)
- Fecha y hora de la ultima cotizacion
- Maximo y minimo del dia
- Variacion anual
- Volumen de negociacion
- Capitalizacion bursatil
- PER
- Rentabilidad por dividendo

### 3. Calculos
Con los datos ya limpios, se calculan mediante max() y min() (combinadas con funciones lambda):
- Empresa con mayor y menor variacion diaria.
- Empresa con mayor y menor capitalizacion bursatil.
- Empresa mas atractiva por rentabilidad por dividendo (filtrando valores None).
- Media de la variacion diaria y media de la rentabilidad por dividendo del indice.

### 4. Generacion de resultados
- informe_ibex35.txt: informe claro y estructurado, listo para entregar a direccion, con las empresas destacadas del dia.
- ibex35_datos.csv: tabla completa con los 35 valores y sus columnas (Empresa, Ultimo, Var %, Fecha, Hora, Max, Min, Var Anual %, Negociacion, Capitalizacion, PER, Rentabilidad Dividendos), lista para abrir en Excel y generar graficos.

---

## Tecnologias utilizadas

- Python
- requests (peticiones HTTP)
- BeautifulSoup (bs4) (parsing de HTML)
- Modulos estandar para generacion de ficheros .txt y .csv
- Excel (visualizacion y creacion de graficos a partir del .csv)

---

## Posibles mejoras futuras

- Automatizacion de la ejecucion diaria (por ejemplo, mediante tareas programadas).
- Envio automatico del informe por correo electronico.
- Generacion de graficos directamente desde Python.
- Historico de datos para analisis de tendencias a lo largo del tiempo.

---

## Notas

Este proyecto tiene un fin educativo/demostrativo sobre web scraping, tratamiento de datos y generacion automatica de informes en Python.
