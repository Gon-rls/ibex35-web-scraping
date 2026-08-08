# ibex35-web-scraping
Web scraping en Python para obtener datos del IBEX 35 y generar informes y archivos CSV automáticamente.

# Web Scraping y Análisis del IBEX 35

Este proyecto consiste en extraer información de las empresas del IBEX 35 utilizando Python y analizar posteriormente los datos obtenidos. Para acceder a la página web utilizo `requests` y `BeautifulSoup`, con los que localizo la tabla que contiene la información de las empresas y recorro sus filas para obtener los diferentes valores.

Durante la extracción se limpian y convierten los datos numéricos teniendo en cuenta el formato utilizado en la página web. Se obtienen datos como el último valor, la variación diaria y anual, fecha y hora, valores máximo y mínimo, negociación, capitalización, PER y rentabilidad por dividendos. Toda esta información se almacena en una lista para poder trabajar posteriormente con ella.

Una vez recopilados los datos, el programa realiza diferentes cálculos utilizando `max()` y `min()`. De esta forma se identifican las empresas con mayor subida y mayor bajada diaria, las que tienen mayor y menor capitalización y la empresa con mayor rentabilidad por dividendos. También se calculan las medias de la variación diaria y de la rentabilidad por dividendos.

Finalmente, se genera un informe en formato TXT con los principales resultados y un archivo CSV con todos los datos extraídos. Estos datos se importan posteriormente a **Excel**, donde se organizan y visualizan mediante tablas y gráficos para facilitar su análisis.

El proyecto me ha permitido practicar web scraping, limpieza y procesamiento de datos, manejo de listas, análisis de información y generación de archivos en diferentes formatos.
