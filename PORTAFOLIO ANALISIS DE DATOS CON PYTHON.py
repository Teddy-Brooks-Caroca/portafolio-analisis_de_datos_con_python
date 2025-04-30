### PORTAFOLIO ANALISIS DE DATOS CON PYTHON ###

# 1. Fundamentos de Python y manipulación inicial

# 1.1 Crear un script para generar el dataset ficticio desde listas y diccionarios.

import pandas as pd

db_barrio_serena = {
    "Id_hogar": [f"LSV-{str(i).zfill(3)}" for i in range(1, 41)],
    "Direccion": [
        "Calle Los Aromos 1234", "Avenida del Mar 203", "Calle Las Palmeras 657", "Pasaje Gabriela Mistral 15", 
        "Callejón Los Arrayanes 88", "Camino El Romeral 322", "Calle Los Pimientos 121", "Avenida Islón 1001", 
        "Callejón Los Lirios 57", "Calle Los Jazmines 789", "Calle Francisco de Aguirre 1445", "Avenida Cuatro Esquinas 932", 
        "Pasaje Valle Hermoso 12", "Callejón Los Quillayes 306", "Calle Las Margaritas 228", "Callejón Cordovez 78", 
        "Avenida Balmaceda 1050", "Pasaje El Milagro 55", "Calle La Cantera 509", "Callejón Las Rosas 132", 
        "Calle Los Álamos 84", "Avenida Colina El Pino 1480", "Pasaje Estrella del Norte 18", "Callejón Vista Hermosa 44", 
        "Calle El Tofo 633", "Avenida Cerro Grande 1499", "Callejón Los Helechos 71", "Calle Santa Margarita 945", 
        "Callejón Parque Inglés 59", "Calle Los Copihues 119", "Avenida Ruta 5 Norte 1012", "Pasaje El Escorial 23", 
        "Callejón Las Hortensias 86", "Calle Pedro Pablo Muñoz 238", "Callejón Las Camelias 115", "Avenida Juan Cisternas 310", 
        "Calle Las Violetas 901", "Pasaje Vista La Bahía 41", "Callejón San Ramón 108", "Calle Laguna Verde 622"
    ],
    "Habitaciones": [
        2, 3, 4, 1, 3, 5, 2, 4, 3, 2, 1, 4, 2, 3, 5, 3, 4, 1, 2, 3, 3, 2, 4, 1, 5, 2, 3, 4, 2, 1, 
        3, 2, 5, 3, 4, 2, 1, 3, 2, 4
    ],
    "Superficie_m2": [
        60, 75, 90, 45, 120, 80, 100, 70, 95, 110, 85, 140, 65, 80, 115, 105, 130, 55, 70, 100, 
        120, 60, 90, 150, 100, 110, 95, 80, 85, 140, 60, 125, 105, 90, 115, 110, 95, 75, 130, 100
    ],
    "Anio_construccion": [
        1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 
        1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997, 1998, 
        1999, 1997, 1998, 1999, 1997, 1998, 1999, 1997
    ],
    "Valor_estimado": [
        65000000, 70000000, 75000000, 80000000, 85000000, 90000000, 95000000, 100000000, 105000000, 110000000, 
        65000000, 70000000, 75000000, 80000000, 85000000, 90000000, 95000000, 100000000, 105000000, 110000000, 
        65000000, 70000000, 75000000, 80000000, 85000000, 90000000, 95000000, 100000000, 105000000, 110000000, 
        65000000, 70000000, 75000000, 80000000, 85000000, 90000000, 95000000, 100000000, 105000000, 110000000
    ],
    "Patio": [
        True, False, True, False, False, False, True, True, False, False, 
        True, False, True, False, False, False, True, False, False, False, 
        True, False, True, True, False, False, True, True, False, False, 
        True, False, True, False, False, False, True, False, False, False
    ],
    "Tipo_vivienda": [
        "Casa", "Departamento", "Cabaña", "Casa", "Departamento", "Casa", "Cabaña", "Casa", "Departamento", "Cabaña", 
        "Casa", "Departamento", "Cabaña", "Casa", "Departamento", "Casa", "Cabaña", "Casa", "Departamento", "Cabaña", 
        "Casa", "Departamento", "Cabaña", "Casa", "Departamento", "Casa", "Cabaña", "Casa", "Departamento", "Cabaña", 
        "Casa", "Departamento", "Cabaña", "Casa", "Departamento", "Casa", "Cabaña", "Casa", "Departamento", "Cabaña"
    ],
    "Nombre_dueno": [
        "Juan Pérez González", "Ana Gómez Rodríguez", "Carlos Sánchez Martínez", "Lucía Martínez López", "Pedro Rodríguez García", 
        "Marta Díaz Fernández", "Luis Fernández García", "Sara López Martínez", "José González Pérez", "Elena Ramírez González", 
        "Miguel Torres López", "Carmen Díaz Rodríguez", "Raúl Morales Pérez", "Patricia Fernández Sánchez", "Javier Sánchez Ruiz", 
        "Victoria Martínez García", "Andrés González López", "Pilar Ruiz Pérez", "Raúl López Fernández", "Mónica García Rodríguez", 
        "Antonio Hernández Sánchez", "Ana María López Ramírez", "David García Torres", "Beatriz Martínez González", "Eduardo Pérez López", 
        "Laura Jiménez Fernández", "Francisco Álvarez García", "Isabel Sánchez Ramírez", "Carlos Ramírez López", "Patricia López Pérez", 
        "Alberto González Díaz", "Manuel Díaz García", "Susana Hernández Ramírez", "José María Torres Pérez", "Dolores Fernández López", 
        "Raúl García Rodríguez", "Gabriela Ruiz Martínez", "Luis Ramírez Sánchez", "Carmen Rodríguez García", "Cristina Pérez González"
    ],
    "Fecha_censo": [
        "15/04/2023", "15/04/2023", "15/04/2023", "15/04/2023", "15/04/2023", "15/04/2023", "15/04/2023", "15/04/2023", 
        "15/04/2023", "15/04/2023", "15/05/2017", "15/05/2017", "15/05/2017", "15/05/2017", "15/05/2017", "15/05/2017", 
        "15/05/2017", "15/05/2017", "15/05/2017", "15/05/2017", "15/06/2010", "15/06/2010", "15/06/2010", "15/06/2010", 
        "15/06/2010", "15/06/2010", "15/06/2010", "15/06/2010", "15/06/2010", "15/06/2010", "15/07/2010", "15/07/2010", 
        "15/07/2010", "15/07/2010", "15/07/2010", "15/07/2010", "15/07/2010", "15/07/2010", "15/07/2010", "15/07/2010"
    ]
}


df_barrio_serena = pd.DataFrame(db_barrio_serena)

print(df_barrio_serena)

# 1.2 Escribir funciones para filtrar viviendas por número de habitaciones.

print(df_barrio_serena[df_barrio_serena['Habitaciones'].isin([2, 3, 5])])
print(df_barrio_serena[ df_barrio_serena['Habitaciones'] == 3 ])
print(df_barrio_serena[df_barrio_serena['Habitaciones'].between(2, 4)])

# 1.3 Calcular el promedio de metros cuadrados por tipo de vivienda.

print(df_barrio_serena.groupby('Tipo_vivienda')['Superficie_m2'].mean())

# 1.4 Usar comprensión de listas para transformar valores (ej. convertir superficies de m² a pies²).

df_barrio_serena['Superficie_pies2'] = [x * 10.7639 for x in df_barrio_serena['Superficie_m2']]

print(df_barrio_serena)

# 1.5 Crear una función que calcule el valor por metro cuadrado.

def precio_por_metrocuadrado(Superficie_m2,Valor_estimado):
    valor_metro = Valor_estimado/Superficie_m2
    return valor_metro

df_barrio_serena['Valor_m2'] = df_barrio_serena.apply(lambda fila: precio_por_metrocuadrado(fila['Superficie_m2'], fila['Valor_estimado']), axis=1)

df_barrio_serena['Valor_m2'] = df_barrio_serena['Valor_m2'].round(2)

print(df_barrio_serena)

# 1.6 Escribir una función que identifique viviendas con más de 20 años.

from datetime import datetime

annio_actual = datetime.now().year

def vivienda_por_annio(Id_hogar,Anio_construccion):
    if(annio_actual - Anio_construccion) >= 20:
        return (f"La casa {Id_hogar} casa tiene mas de 20 años")
    else:
        return (f"La casa {Id_hogar} casa tiene menos de 20 años") 

df_barrio_serena['Estado_vivienda'] = df_barrio_serena.apply(
    lambda fila: vivienda_por_annio(fila['Id_hogar'], fila['Anio_construccion']),
    axis=1
)

print(df_barrio_serena[['Id_hogar', 'Estado_vivienda']])

# 1.7 Guardar y cargar el dataset como archivo .csv.

df_barrio_serena.to_csv('barrio_serena.csv', index=False)

df_barrio_serena = pd.read_csv('barrio_serena.csv')

print(df_barrio_serena)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# 2. Numpy aplicado al análisis de datos

# 2.1 Crear un array con los valores de superficie y realizar estadísticas básicas.

import numpy as np

array_superficie_m2 = np.array(df_barrio_serena["Superficie_m2"])

media_superficie_m2 = array_superficie_m2.mean()
mediana_superficie_m2 = np.median(array_superficie_m2)
minimo_superficie_m2 = np.min(array_superficie_m2)
maximo_superficie_M2 = np.max(array_superficie_m2)
desviacion_superficie_M2 = np.std(array_superficie_m2)
varianza_superficie_M2 = np.var(array_superficie_m2)

print(":::: RESUMEN ESTADÍSTICO BÁSICO ::::")
print(f"Media: {media_superficie_m2}" "\n"
      f"Mediana: {mediana_superficie_m2}" "\n"
      f"Minimo: {minimo_superficie_m2}" "\n"
      f"Máximo: {maximo_superficie_M2}" "\n"
      f"Desviación: {desviacion_superficie_M2}" "\n"
      f"Varianza: {varianza_superficie_M2}")
print(":::::::::::::::::::::::::::::::::::::")

print(":::: COMPARATIVA ::::")
print(df_barrio_serena['Superficie_m2'].describe())
print(":::::::::::::::::::::")

# 2.2 Normalizar los valores de superficie.

df_barrio_serena['Normalizado_superficie_M2'] = (array_superficie_m2 - minimo_superficie_m2) / (maximo_superficie_M2 - minimo_superficie_m2)
df_barrio_serena['Z_superficie_M2'] = (array_superficie_m2 - media_superficie_m2) / desviacion_superficie_M2

print(df_barrio_serena)

# 2.3 Comparar la media de superficie entre casas y departamentos usando boolean indexing.

boolean_tipo_casa = df_barrio_serena["Tipo_vivienda"] == "Casa"
resultado_boolean_mean_casa = df_barrio_serena[boolean_tipo_casa]["Superficie_m2"].mean()

boolean_tipo_departamento = df_barrio_serena["Tipo_vivienda"] == "Departamento"
resultado_boolean_mean_departamento = df_barrio_serena[boolean_tipo_departamento]["Superficie_m2"].mean()

print(":::: MEDIAS AMBOS BOLEANOS ::::")
print(f"Media de casa: {resultado_boolean_mean_casa}" "\n"
      f"Media de departamento: {resultado_boolean_mean_departamento}")
print(":::::::::::::::::::::::::::::::")

# 2.4 Usar álgebra lineal para simular una transformación de precios (matriz de coeficientes).

variables = df_barrio_serena[["Habitaciones", "Superficie_m2"]]

coeficientes = np.array([8_000_000, 300_000])

precios_transformados = variables.dot(coeficientes)

precios_transformados += 5_000_000 #Agregamos un interpecto para "simular" alguna condición

df_barrio_serena["Nuevo_valor_estimado"] = precios_transformados

print(df_barrio_serena[["Valor_estimado","Nuevo_valor_estimado"]])


# 2.5 Aplicar máscaras booleanas para encontrar viviendas con superficie > media.

boolean_mask_superficie = array_superficie_m2 > media_superficie_m2

resultado_boolean_mask = array_superficie_m2[boolean_mask_superficie]

ids_casas = df_barrio_serena["Id_hogar"].values

print("Viviendas con superficie mayor a la media:")
for i,superficie in enumerate(resultado_boolean_mask):
    if superficie:
        print(f"ID: {ids_casas[i]} - Superficie: {array_superficie_m2[i]} m²")


# 2.6 Calcular el percentil 25, 50 y 75 de los precios.

array_precio_estimado = np.array(df_barrio_serena["Valor_estimado"])

precio_sorted = np.sort(array_precio_estimado)

print(f"Datos ordenados: {precio_sorted}")


percentil_25 = np.percentile(precio_sorted, 25)
percentil_75 = np.percentile(precio_sorted, 75)

print(f"Percentil 25 (Q1): {percentil_25}")
print(f"Percentil 75 (Q3): {percentil_75}")

# 2.7 Crear una matriz 2D que combine habitaciones y superficie, y graficarla con imshow.

import matplotlib.pyplot as plt

habitaciones = np.array(df_barrio_serena["Habitaciones"].values)
superficie = np.array(df_barrio_serena["Superficie_m2"].values)

matriz_2d = np.array([habitaciones, superficie])

matriz_2d = habitaciones[:, np.newaxis] * superficie  

plt.imshow(matriz_2d, cmap='viridis', interpolation='nearest', aspect='auto')
plt.colorbar()  

plt.xticks(np.arange(len(habitaciones)), habitaciones)
plt.yticks(np.arange(len(superficie)), superficie)

plt.title("Matriz 2D de Habitaciones y Superficie")
plt.xlabel("Índices de las Viviendas")
plt.ylabel("Índices de Superficies")

plt.show()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#🐼 3. Pandas I – Exploración y limpieza
#Leer el dataset desde un .csv y explorar los tipos de datos.

#Verificar y modificar índices del DataFrame.

#Detectar y corregir valores faltantes (NaN).

#Eliminar registros con datos inconsistentes (ej. superficie negativa).

#Crear columnas nuevas: antigüedad de la vivienda, valor por m².

#Ordenar las viviendas por precio descendente.

#Seleccionar viviendas construidas antes del año 2000 y con más de 3 habitaciones.

#🧮 4. Pandas II – Agrupaciones y fechas
#Agrupar por tipo de vivienda y calcular estadísticas de precios.

#Contar cuántas viviendas tienen patio por tipo de vivienda.

#Convertir las fechas de censo a formato datetime.

#Calcular cuántos años pasaron desde el último censo.

#Crear una tabla pivote que cruce tipo de vivienda y si tiene patio.

#Graficar con pandas.plot() la evolución del precio promedio por antigüedad.

#Usar .query() para seleccionar viviendas con más de 100m² y menos de $80 millones.

#📊 5. Visualización con Matplotlib
#Histograma del valor de las viviendas.

#Gráfico de dispersión entre superficie y precio.

#Boxplot del precio por tipo de vivienda.

#Gráfico de barras de cantidad de viviendas por tipo.

#Pie chart del porcentaje de viviendas con/ sin patio.

#Subplots que muestren superficie vs. precio por tipo de vivienda.

#Agregar título, ejes y leyenda personalizada al gráfico de dispersión.

