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