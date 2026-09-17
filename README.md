# ibex35-web-scraping



Programa en Python que obtiene en tiempo real los datos de las 35 empresas que componen el índice bursátil IBEX-35, los procesa y genera automáticamente un informe ejecutivo y una hoja de cálculo lista para análisis y visualización en Excel.


# Descripción
Este proyecto automatiza la obtención y el análisis de los datos del IBEX-35 publicados en la web de CincoDías. A partir de esa información, genera de forma automática:

Un informe de texto (informe_ibex35.txt) con los datos más relevantes de la jornada, listo para ser entregado a dirección.
Una hoja de cálculo (ibex35_datos.csv) con todos los datos de las 35 empresas organizados por columnas, que puede abrirse en Excel para filtrar, ordenar y crear gráficos.
El objetivo es que la herramienta pueda ejecutarse a diario, sirviendo como un sistema de análisis rápido y automatizado para los directivos de una empresa de inversión, sin necesidad de revisar manualmente los datos del mercado.

# ¿Para qué sirve?
Ahorra tiempo en la recopilación manual de datos bursátiles.
Facilita la toma de decisiones al resumir automáticamente las empresas con mayor subida, mayor bajada, mayor y menor capitalización, y la más atractiva por dividendo.
Deja los datos preparados en formato tabular para su explotación en Excel (gráficos, filtros, dashboards).
Puede integrarse en una rutina diaria de análisis financiero interno.

# ¿Cómo funciona?
1. Obtención de datos
Se conecta a la web de CincoDías mediante:

requests: realiza la petición HTTP a la página, igual que un navegador.
BeautifulSoup: analiza el HTML recibido para localizar la tabla del IBEX-35 (identificada por su clase CSS bt shortable) y extraer los datos de cada empresa.
2. Limpieza y tratamiento de datos
Los datos llegan en formato numérico español (1.234,56) y se convierten al formato inglés (1234.56) mediante sustituciones de separadores de miles y decimales. Los valores vacíos o con formato inesperado (como el PER o la rentabilidad por dividendo) se controlan con bloques try/except, asignando None cuando no es posible convertir el dato, evitando así que el programa se detenga por errores.

De cada empresa se extrae:

Nombre
Precio actual (último)
Variación del día (%)
Fecha y hora de la última cotización
Máximo y mínimo del día
Variación anual
Volumen de negociación
Capitalización bursátil
PER
Rentabilidad por dividendo
3. Cálculos
Con los datos ya limpios, se calculan mediante max() y min() (combinadas con funciones lambda):

Empresa con mayor y menor variación diaria.
Empresa con mayor y menor capitalización bursátil.
Empresa más atractiva por rentabilidad por dividendo (filtrando valores None).
Media de la variación diaria y media de la rentabilidad por dividendo del índice.
4. Generación de resultados
informe_ibex35.txt: informe claro y estructurado, listo para entregar a dirección, con las empresas destacadas del día.
ibex35_datos.csv: tabla completa con los 35 valores y sus columnas (Empresa, Último, Var %, Fecha, Hora, Máx, Mín, Var Anual %, Negociación, Capitalización, PER, Rentabilidad Dividendos), lista para abrir en Excel y generar gráficos.

# Tecnologías utilizadas
Python
requests — peticiones HTTP
BeautifulSoup (bs4) — parsing de HTML
Módulos estándar para generación de ficheros .txt y .csv
Excel — visualización y creación de gráficos a partir del .csv
 Estructura de salida
 proyecto-ibex35/
├── informe_ibex35.txt      # Resumen ejecutivo del día
├── ibex35_datos.csv        # Datos completos de las 35 empresas
└── ...

# Posibles mejoras futuras
Automatización de la ejecución diaria (por ejemplo, mediante tareas programadas).
Envío automático del informe por correo electrónico.
Generación de gráficos directamente desde Python.
Histórico de datos para análisis de tendencias a lo largo del tiempo.

# Notas
Este proyecto tiene un fin educativo/demostrativo sobre web scraping, tratamiento de datos y generación automática de informes en Python.
