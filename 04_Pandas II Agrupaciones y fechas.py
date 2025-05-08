# 4. Pandas II – Agrupaciones y fechas

# 4.1 Agrupar por tipo de vivienda y calcular estadísticas de precios.

resumen_estadistico = df_barrio_serena.groupby("Tipo_vivienda").agg(
    cantidad = ("Valor_estimado", "count"),
    media_precios = ("Valor_estimado","mean"),
    mediana_precios = ("Valor_estimado", "median"),
    desviacion_std = ("Valor_estimado", "std"),
    varianza = ("Valor_estimado", "var"),
    minimo = ("Valor_estimado", "min"),
    maximo = ("Valor_estimado", "max")
)

print(":::: RESUMEN ESTADISTICO ::::")
print(resumen_estadistico)
print(":::::::::::::::::::::::::::::")

# 4.2 Contar cuántas viviendas tienen patio por tipo de vivienda.

conteo_viviendas_patio = df_barrio_serena[df_barrio_serena["Patio"] == True].groupby("Tipo_vivienda").agg(
    cantidad_con_patio = ("Patio", "count")
)

print(":::: CONTEO DE CASAS CON PATIO ::::")
print(conteo_viviendas_patio)
print("*Recordar que es bolean count")
print(":::::::::::::::::::::::::::::::::::")

# 4.3 Convertir las fechas de censo a formato datetime.

df_barrio_serena["Fecha_censo"] = pd.to_datetime(df_barrio_serena["Fecha_censo"], format='mixed', dayfirst=True, errors='coerce')


# 4.4 Calcular cuántos años pasaron desde el último censo.

fecha_ultimo_censo = df_barrio_serena["Fecha_censo"].max()

hoy = pd.Timestamp.now()
diferencia = hoy - fecha_ultimo_censo
anios_transcurridos = diferencia.days / 365.25  # Aproximación incluyendo años bisiestos

print(":" * 40)
print(f"Pasaron aproximadamente {anios_transcurridos:.2f} años desde el último censo.")
print(":" * 40)

# 4.5 Crear una tabla pivote que cruce tipo de vivienda y si tiene patio.

print(df_barrio_serena["Patio"].unique()) #al ser boleanos, nos aseguramos que sean solo valores TRUE o FALSE

pivote_vivienda_patio = pd.pivot_table(
    data=df_barrio_serena,
    index='Tipo_vivienda',
    columns='Patio',
    values='Valor_estimado',  # o cualquier columna no nula
    aggfunc='count',
    fill_value=0
)

pivote_vivienda_patio.columns = ['Sin_patio', 'Con_patio']

print(pivote_vivienda_patio)

# 4.6 Graficar con pandas.plot() la evolución del precio promedio por antigüedad.

df_barrio_serena["Antigüedad"] = 2025 - df_barrio_serena["Anio_construccion"]

promedio_por_antiguedad = df_barrio_serena.groupby("Antigüedad")["Valor_estimado"].mean()
promedio_por_antiguedad = promedio_por_antiguedad.sort_index()

promedio_por_antiguedad.plot(
    kind='line',
    title="Evolución del precio promedio por antigüedad",
    xlabel="Antigüedad (años)",
    ylabel="Precio promedio",
    grid=True
)

plt.show()

# 4.7 Usar .query() para seleccionar viviendas con más de 100m² y menos de $80 millones.

filtrado_vivienda_valor = df_barrio_serena.query("Superficie_m2 > 100 & Valor_estimado < 800000000")

print(filtrado_vivienda_valor)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
