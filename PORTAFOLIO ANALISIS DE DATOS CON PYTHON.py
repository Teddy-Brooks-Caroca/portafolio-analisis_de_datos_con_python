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

Calcular el promedio de metros cuadrados por tipo de vivienda.

Usar comprensión de listas para transformar valores (ej. convertir superficies de m² a pies²).

Crear una función que calcule el valor por metro cuadrado.

Escribir una función que identifique viviendas con más de 20 años.

Guardar y cargar el dataset como archivo .csv.

🔢 2. Numpy aplicado al análisis de datos
Crear un array con los valores de superficie y realizar estadísticas básicas.

Normalizar los valores de superficie.

Comparar la media de superficie entre casas y departamentos usando boolean indexing.

Usar álgebra lineal para simular una transformación de precios (matriz de coeficientes).

Aplicar máscaras booleanas para encontrar viviendas con superficie > media.

Calcular el percentil 25, 50 y 75 de los precios.

Crear una matriz 2D que combine habitaciones y superficie, y graficarla con imshow.

🐼 3. Pandas I – Exploración y limpieza
Leer el dataset desde un .csv y explorar los tipos de datos.

Verificar y modificar índices del DataFrame.

Detectar y corregir valores faltantes (NaN).

Eliminar registros con datos inconsistentes (ej. superficie negativa).

Crear columnas nuevas: antigüedad de la vivienda, valor por m².

Ordenar las viviendas por precio descendente.

Seleccionar viviendas construidas antes del año 2000 y con más de 3 habitaciones.

🧮 4. Pandas II – Agrupaciones y fechas
Agrupar por tipo de vivienda y calcular estadísticas de precios.

Contar cuántas viviendas tienen patio por tipo de vivienda.

Convertir las fechas de censo a formato datetime.

Calcular cuántos años pasaron desde el último censo.

Crear una tabla pivote que cruce tipo de vivienda y si tiene patio.

Graficar con pandas.plot() la evolución del precio promedio por antigüedad.

Usar .query() para seleccionar viviendas con más de 100m² y menos de $80 millones.

📊 5. Visualización con Matplotlib
Histograma del valor de las viviendas.

Gráfico de dispersión entre superficie y precio.

Boxplot del precio por tipo de vivienda.

Gráfico de barras de cantidad de viviendas por tipo.

Pie chart del porcentaje de viviendas con/ sin patio.

Subplots que muestren superficie vs. precio por tipo de vivienda.

Agregar título, ejes y leyenda personalizada al gráfico de dispersión.

