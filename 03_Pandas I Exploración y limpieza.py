# 3. Pandas I – Exploración y limpieza

# 3.1 Leer el dataset desde un .csv y explorar los tipos de datos.

df_barrio_serena = pd.read_csv('barrio_serena.csv')

print(df_barrio_serena)

print(df_barrio_serena.info())

# 3.2 Verificar y modificar índices del DataFrame.

print(df_barrio_serena.index)

df_barrio_serena.set_index("Id_hogar", inplace=True)
print(df_barrio_serena.head())

# 3.3 Detectar y corregir valores faltantes (NaN).

nuevas_casas_observadas = [
    {"Id_hogar": "LSV-041", "Direccion": "Av. Pacífico 123", "Habitaciones": 3, "Superficie_m2": 120, "Anio_construccion": 2015,
     "Valor_estimado": 95000000, "Patio": True, "Tipo_vivienda": "Casa", "Nombre_dueno": "Carmen Soto", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-042", "Direccion": "Calle 5 Norte 456", "Habitaciones": np.nan, "Superficie_m2": 110, "Anio_construccion": 2010,
     "Valor_estimado": 88000000, "Patio": False, "Tipo_vivienda": "Departamento", "Nombre_dueno": "Andrés Olivares", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-043", "Direccion": "Pasaje Lo Ovalle 9", "Habitaciones": 2, "Superficie_m2": -85, "Anio_construccion": 2008,
     "Valor_estimado": 73000000, "Patio": True, "Tipo_vivienda": "Casa", "Nombre_dueno": "Lorena Jara", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-044", "Direccion": "Calle San Martín 10", "Habitaciones": 4, "Superficie_m2": 150, "Anio_construccion": 2022,
     "Valor_estimado": np.nan, "Patio": True, "Tipo_vivienda": "Casa", "Nombre_dueno": "Cristóbal Vera", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-045", "Direccion": "Los Alerces 87", "Habitaciones": 3, "Superficie_m2": 105, "Anio_construccion": 1998,
     "Valor_estimado": -5000000, "Patio": False, "Tipo_vivienda": "Departamento", "Nombre_dueno": "Mónica Palma", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-046", "Direccion": "San Ignacio 55", "Habitaciones": 1, "Superficie_m2": 45, "Anio_construccion": 2005,
     "Valor_estimado": 60000000, "Patio": False, "Tipo_vivienda": "Departamento", "Nombre_dueno": "Jorge Lillo", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-047", "Direccion": "Av. del Mar 321", "Habitaciones": 3, "Superficie_m2": 130, "Anio_construccion": 2018,
     "Valor_estimado": 99000000, "Patio": True, "Tipo_vivienda": "Casa", "Nombre_dueno": "Francisca Reinoso", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-048", "Direccion": "Camino Real 112", "Habitaciones": np.nan, "Superficie_m2": np.nan, "Anio_construccion": 2001,
     "Valor_estimado": 82000000, "Patio": True, "Tipo_vivienda": np.nan, "Nombre_dueno": "Sin registro", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-049", "Direccion": "Monte León 28", "Habitaciones": 2, "Superficie_m2": 0, "Anio_construccion": 2000,
     "Valor_estimado": 72000000, "Patio": False, "Tipo_vivienda": "Departamento", "Nombre_dueno": "Gustavo Araya", "Fecha_censo": "2023-06-01"},

    {"Id_hogar": "LSV-050", "Direccion": "Villa Serena 51", "Habitaciones": 5, "Superficie_m2": 160, "Anio_construccion": 2019,
     "Valor_estimado": 101000000, "Patio": True, "Tipo_vivienda": "Casa", "Nombre_dueno": "Tatiana Castillo", "Fecha_censo": "2023-06-01"},
]

df_nuevas_casas = pd.DataFrame(nuevas_casas_observadas)

print(df_nuevas_casas)

print(df_nuevas_casas.isna())

print(df_nuevas_casas.isna().sum())

#Corregimos con el valor promedio (se debe tener cuidado ocn los valores negativos, en este caso existen)
media_superficie = df_nuevas_casas["Superficie_m2"].mean() 
media_valor_estimado = df_nuevas_casas["Valor_estimado"].mean()

#Otra manera de imputar es poner 0 como "no observado"
cantidad_habitaciones_0  = 0

#Corregimos los NAN
df_nuevas_casas["Superficie_m2"].fillna(media_superficie, inplace=True)
df_nuevas_casas["Valor_estimado"].fillna(media_valor_estimado, inplace=True)
df_nuevas_casas["Habitaciones"].fillna(cantidad_habitaciones_0, inplace=True)
df_nuevas_casas["Tipo_vivienda"].fillna("No observado", inplace=True)

print(df_nuevas_casas.isna().sum())


# 3.4 Eliminar registros con datos inconsistentes (ej. superficie negativa).

print(df_nuevas_casas[df_nuevas_casas["Superficie_m2"] < 0])

df_nuevas_casas = df_nuevas_casas[df_nuevas_casas["Superficie_m2"] >= 0]

print(df_nuevas_casas)

df_barrio_serena.reset_index(inplace=True)

df_barrio_serena = pd.concat([df_barrio_serena, df_nuevas_casas], ignore_index=True)

print(df_barrio_serena)


# 3.5 Crear columnas nuevas: antigüedad de la vivienda, valor por m².

df_barrio_serena["precio_por_habitacion"] = df_barrio_serena["Valor_estimado"] / df_barrio_serena["Habitaciones"]

def clasificar_valor(x):
    if x > 90000000:
        return "Premium"
    elif x > 70000000:
        return "Alta"
    elif x > 50000000:
        return "Media"
    else:
        return "Baja"

df_barrio_serena["Observaciones"] = df_barrio_serena["Valor_estimado"].apply(clasificar_valor)

print(df_barrio_serena)

# 3.6 Ordenar las viviendas por precio descendente.

orden_por_precio = df_barrio_serena.sort_values(by="Valor_estimado", ascending= True)

print(orden_por_precio)

# 3.7 Seleccionar viviendas construidas antes del año 2000 y con más de 3 habitaciones.

filtrado_annio_habitacion = df_barrio_serena[
    (df_barrio_serena["Anio_construccion"] > 25) &
    (df_barrio_serena["Habitaciones"] > 3 )
     ]

print(f"hay {len(filtrado_annio_habitacion)} casas que cumplen las condiciones")

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::