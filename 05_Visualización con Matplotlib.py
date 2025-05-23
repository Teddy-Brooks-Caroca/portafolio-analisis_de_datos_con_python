# 5. Visualización con Matplotlib

# 5.1 Histograma del valor de las viviendas.

import matplotlib.pyplot as plt

df_barrio_serena["Valor_estimado"] = df_barrio_serena["Valor_estimado"] / 1000  # Convertir a miles en lugar de millones
df_filtrado = df_barrio_serena[df_barrio_serena["Valor_estimado"] > 0] #Filtramos solo los valores positivos

plt.figure(figsize=(10, 5)) #Se redimensiona el grafico

plt.hist(df_filtrado["Valor_estimado"], bins= 5,color="blue", edgecolor="black",label="Viviendas")

plt.xlabel("Valor estimado ($)")
plt.ylabel("Frecuencia")
plt.title("Histograma de valores de vivienda")
plt.legend()
plt.show()

# 5.2 Gráfico de dispersión entre superficie y precio.

df_barrio_serena["Valor_estimado"] = df_barrio_serena["Valor_estimado"] / 1000  
df_filtrado = df_barrio_serena[df_barrio_serena["Valor_estimado"] > 0] 

plt.figure(figsize=(10, 5))

plt.scatter(df_filtrado["Superficie_m2"], df_filtrado["Valor_estimado"], color="blue", alpha=0.7)

plt.xlabel("Superficie en m²")
plt.ylabel("Valor estimado (miles $)")
plt.title("Gráfico de dispersión: Superficie vs. Precio")

plt.show()

# 5.3 Boxplot del precio por tipo de vivienda.

df_barrio_serena["Valor_estimado"] = df_barrio_serena["Valor_estimado"] / 1000  
df_filtrado = df_barrio_serena[df_barrio_serena["Valor_estimado"] > 0] 

tipos_vivienda = df_barrio_serena.groupby("Tipo_vivienda")["Valor_estimado"].apply(list)

plt.figure(figsize=(10, 5))
plt.boxplot(tipos_vivienda, patch_artist=True, boxprops=dict(facecolor="lightblue"))

plt.xticks(range(1, len(tipos_vivienda) + 1), tipos_vivienda.index, rotation=15) 
plt.xlabel("Tipo de vivienda")
plt.ylabel("Valor estimado ($)")
plt.title("Boxplot de precios por tipo de vivienda")

plt.show()

# 5.4 Gráfico de barras de cantidad de viviendas por tipo.

conteo_viviendas_general = df_barrio_serena["Tipo_vivienda"].value_counts()

conteo_viviendas_general.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Cantidad de viviendas por tipo")
plt.xlabel("Tipo de vivienda")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# 5.5 Pie chart del porcentaje de viviendas con/ sin patio.

conteo_patio = df_barrio_serena["Patio"].value_counts()

etiquetas = ["Con patio", "Sin patio"] # etiquetamos según sea el caso

colores = ["lightgreen", "lightcoral"] # como opción le ponemos color a cada opción

plt.pie(conteo_patio, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
plt.title("Porcentaje de viviendas con y sin patio")
plt.axis('equal')  # Para que sea un círculo perfecto
plt.tight_layout()

plt.show()

# 5.6 Subplots que muestren superficie vs. precio por tipo de vivienda.


df_filtrado = df_barrio_serena[df_barrio_serena["Valor_estimado"] > 0].copy()
df_filtrado["Valor_millones"] = df_filtrado["Valor_estimado"] / 1e6 #versión mas corta de millones

# filtaramos para hacer los subplot
vivienda_casa = df_filtrado[df_filtrado["Tipo_vivienda"] == "Casa"]
vivienda_dpto = df_filtrado[df_filtrado["Tipo_vivienda"] == "Departamento"]

# le damos las dimensiones
plt.figure(figsize=(12, 5))

# Subplot 1: Casa
plt.subplot(1, 2, 1)
plt.scatter(vivienda_casa["Superficie_m2"], vivienda_casa["Valor_millones"], color="mediumseagreen", edgecolor="black")
plt.title("Casa")
plt.xlabel("Superficie (m²)")
plt.ylabel("Valor estimado (millones)")

# Subplot 2: Departamento
plt.subplot(1, 2, 2)
plt.scatter(vivienda_dpto["Superficie_m2"], vivienda_dpto["Valor_millones"], color="cornflowerblue", edgecolor="black")
plt.title("Departamento")
plt.xlabel("Superficie (m²)")
plt.ylabel("Valor estimado (millones)")

plt.tight_layout()
plt.suptitle("Superficie vs. Valor estimado por tipo de vivienda", fontsize=14, y=1.05)
plt.show()

# 5.7 Agregar título, ejes y leyenda personalizada al gráfico de dispersión.

'''
Se estiliza gráfico del ejercicio 5.2 estilizando tanto la forma como su contenido
'''

# Aseguramos que no haya valores negativos en el precio
df_barrio_serena["Valor_estimado"] = df_barrio_serena["Valor_estimado"] / 1000000
df_filtrado = df_barrio_serena[df_barrio_serena["Valor_estimado"] > 0]

# Creamos figura
plt.figure(figsize=(10, 6))

# Gráfico de dispersión
plt.scatter(
    df_filtrado["Superficie_m2"],
    df_filtrado["Valor_estimado"],
    color="mediumblue",
    alpha=0.6,
    edgecolor="black",
    label="Viviendas"
)

# Etiquetas y título mejorados
plt.title("Relación entre Superficie y Valor Estimado", fontsize=14, fontweight='bold')
plt.xlabel("Superficie (m²)", fontsize=12)
plt.ylabel("Valor estimado (en millones)", fontsize=12)

# Agregamos leyenda personalizada
plt.legend(loc="upper left", frameon=True, shadow=True)

# Rejilla para mejorar lectura
plt.grid(True, linestyle='--', alpha=0.5)

# Ajuste final de layout
plt.tight_layout()
plt.show()

# ::::::::::::::::::::::::::::::::: FIN PORTAFOLIO :::::::::::::::::::::::::::::::::