#accedemos a la web y obtenemos el contenido HTML

from bs4 import BeautifulSoup
import requests
import csv

url = "https://cincodias.elpais.com/mercados/bolsa/ibex-35/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

tabla = soup.find("table", {"class": "bt shortable"})
filas = tabla.find("tbody").find_all("tr")


datos_ibex = []

for fila in filas:
    celdas = fila.find_all("td")
    nombre = fila.find("th").get_text(strip=True)

    # Extraer y limpiar los valores numéricos
    ultimo = float(celdas[0].get_text().replace('.', '').replace(',', '.'))
    var_pct = celdas[1].get_text().replace('%','').replace(',', '.').strip()
    try:
        var_pct = float(var_pct)
    except:
        var_pct = None

    fecha_hora = celdas[2].get_text(strip=True).replace('\n','')
    fecha, hora = fecha_hora[:10], fecha_hora[10:]

    max_val = float(celdas[3].get_text().replace('.', '').replace(',', '.'))
    min_val = float(celdas[4].get_text().replace('.', '').replace(',', '.'))

    var_anual = celdas[5].get_text().replace('%','').replace(',', '.').strip()
    try:
        var_anual = float(var_anual)
    except:
        var_anual = None

    negociacion = float(celdas[6].get_text().replace('.', '').replace(',', '.'))
    capitalizacion = float(celdas[7].get_text().replace('.', '').replace(',', '.'))

    per = celdas[8].get_text().replace(',', '.').strip()
    try:
        per = float(per)
    except:
        per = None

    rent_dvd = celdas[9].get_text().replace('%','').replace(',', '.').strip()
    try:
        rent_dvd = float(rent_dvd)
    except:
        rent_dvd = None

    datos_ibex.append([
        nombre, ultimo, var_pct, fecha, hora, max_val, min_val,
        var_anual, negociacion, capitalizacion, per, rent_dvd
    ])

# Comprobamos que se han extraído correctamente los datos del IBEX-35 y que se han limpiado los valores numéricos para antes de calcular cosas ver que este bien realizado.
# Comprobar los primeros resultados 
for d in datos_ibex[:5]:
    print(d)


# Mostrar todas las empresas extraídas para ver que esten las 35
for d in datos_ibex:
    print(d)
    
# Mostrar el número total de empresas extraídas
print(len(datos_ibex))


#parte 2
# 1. Empresa con mayor y menor variación diaria
mayor_subida = max(datos_ibex, key=lambda x: x[2])   
mayor_bajada = min(datos_ibex, key=lambda x: x[2])

# 2. Empresa con mayor y menor capitalización
mayor_cap = max(datos_ibex, key=lambda x: x[9])     
menor_cap = min(datos_ibex, key=lambda x: x[9])

# 3. Empresa más atractiva por dividendos
mejor_div = max(datos_ibex, key=lambda x: x[11] if x[11] is not None else -1)

# --- CÁLCULO DE MEDIAS ---

# Media de la Variación del día 
variaciones = [x[2] for x in datos_ibex if x[2] is not None]
media_var = sum(variaciones) / len(variaciones)
print("la media de la variacion es ", media_var)

# Media de la Rentabilidad por Dividendos 
dividendos = [x[11] for x in datos_ibex if x[11] is not None]
media_div = sum(dividendos) / len(dividendos)
print("la media de la rentabilidad por dividendos es ", media_div)

# Crear el contenido del informe
informe = f"""===== INFORME DE GONZALO DEL IBEX-35 =====

1. Variación del día:
   Mayor subida: {mayor_subida[0]} -> Último: {mayor_subida[1]}, Var %: {mayor_subida[2]}%
   Mayor bajada: {mayor_bajada[0]} -> Último: {mayor_bajada[1]}, Var %: {mayor_bajada[2]}%

2. Capitalización bursátil:
   Mayor capitalización: {mayor_cap[0]} -> {mayor_cap[9]:,.2f} €
   Menor capitalización: {menor_cap[0]} -> {menor_cap[9]:,.2f} €

3. Empresa más atractiva por dividendos:
   {mejor_div[0]} -> Rentabilidad dividendos: {mejor_div[11]}%

============================
"""

# Guardar en un archivo TXT
with open("informe_ibex35.txt", "w", encoding="utf-8") as file:
    file.write(informe)


# Definir el nombre del archivo CSV
nombre_archivo = "ibex35_datos_Gonzalo.csv"

# Encabezados para las columnas
encabezados = [
    "Empresa", "Último", "Var %", "Fecha", "Hora", "Máx", "Mín", 
    "Var Anual %", "Negociación", "Capitalización", "PER", "Rentabilidad Dividendos"
]

# Crear y escribir el CSV
with open(nombre_archivo, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(encabezados)  # escribir encabezados
    
    # Escribir los datos de cada empresa
    for fila in datos_ibex:
        writer.writerow(fila)

print(f"Archivo '{nombre_archivo}' creado correctamente con {len(datos_ibex)} empresas.")
