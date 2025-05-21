import pandas as pd
import streamlit as st
import altair as alt

# El código para instalar streamlit (!pip install -q streamlit)
# no debe estar dentro del script de Streamlit.
# Debes ejecutarlo una vez en tu entorno antes de ejecutar el script de Streamlit.
# Por lo tanto, eliminamos la línea !pip install.
import streamlit as st
import pandas as pd
import plotly.express as px

# Assumes 'OMS.csv' is accessible in the Streamlit environment
df_oms = pd.read_csv('RELAY_WHS.csv')

df_mexico = df_oms[df_oms['GEO_NAME_SHORT'] == 'Mexico']

# Create the area chart faceted by sex
fig1 = px.area(df_mexico, x="DIM_TIME", y="AMOUNT_N", facet_col="DIM_SEX",
               title='Amount Over Time for Mexico (Faceted by Sex)')

# Display the first chart in Streamlit
st.plotly_chart(fig1, use_container_width=True)

# Create the area chart with sex as color
fig2 = px.area(df_mexico, x="DIM_TIME", y="AMOUNT_N", color="DIM_SEX",
               title='Amount Over Time para Mexico (Color by Sex)')

# Display the second chart in Streamlit
st.plotly_chart(fig2, use_container_width=True)





# Lee el archivo CSV
try:
    df = pd.read_csv('RELAY_WHS.csv')
except FileNotFoundError:
    st.error("Error: El archivo RELAY_WHS.csv no fue encontrado.")
    st.stop() # Detiene la ejecución si el archivo no se encuentra

# Muestra las primeras filas del DataFrame para verificar (opcional en Streamlit)
# st.write("Primeras filas del DataFrame:")
# st.dataframe(df.head())

st.title('Análisis de AMOUNT_N por Tiempo y Sexo')

st.write("Datos brutos:")
st.dataframe(df)

# Limpiar y convertir la columna DIM_TIME a formato de fecha
# Es crucial para que Altair pueda graficar correctamente series temporales.
# Asumiendo que DIM_TIME es un timestamp numérico, lo convertimos.
# Si el formato es diferente (por ejemplo, 'YYYYMMDD'), ajusta el código
# de pd.to_datetime con el formato correcto.
try:
    df['DIM_TIME'] = pd.to_datetime(df['DIM_TIME'], unit='ms')
    # Si el formato es 'YYYYMMDD', usa:
    # df['DIM_TIME'] = pd.to_datetime(df['DIM_TIME'], format='%Y%m%d')
except Exception as e:
    st.error(f"Error al convertir la columna DIM_TIME a formato de fecha: {e}")
    st.stop()
# Agrupar por tiempo, tipo de tiempo y sexo, y sumar la cantidad
df_grouped = df.groupby(['DIM_TIME', 'DIM_TIME_TYPE', 'DIM_SEX'])['AMOUNT_N'].sum().reset_index()

# Calcular el total agrupando solo por tiempo y tipo de tiempo
df_total = df.groupby(['DIM_TIME', 'DIM_TIME_TYPE'])['AMOUNT_N'].sum().reset_index()
df_total['DIM_SEX'] = 'TOTAL' # Añadir una columna para identificar la línea total

# Combinar los dataframes agrupados y el total
df_combined = pd.concat([df_grouped, df_total])

# Crear la gráfica de líneas usando Altair
chart = alt.Chart(df_combined).mark_line().encode(
    x=alt.X('DIM_TIME:T', title='DIM_TIME'), # 'T' indica que es un campo temporal
    y=alt.Y('AMOUNT_N:Q', title='AMOUNT_N'), # 'Q' indica que es un campo cuantitativo
    color=alt.Color('DIM_SEX:N', title='Sexo'), # 'N' indica que es un campo nominal (categórico)
    facet=alt.Facet('DIM_TIME_TYPE:N', columns=2, title='Tipo de Tiempo') # Facet por tipo de tiempo
).properties(
    title='AMOUNT_N Over Time por Sexo y Tipo de Tiempo'
).interactive() # Permite hacer zoom y pan en la gráfica

# Mostrar la gráfica en Streamlit
st.altair_chart(chart, use_container_width=True)

st.write("Tabla de datos agrupados y totales utilizados para la gráfica:")
st.dataframe(df_combined)

import streamlit as st
import matplotlib.pyplot as plt

# Título de la app
st.title("Principales causas de muerte - Mujeres (México, 2021)")

# Datos
causas = [
'COVID-19', 'Ischaemic heart disease', 'Diabetes mellitus',
'Kidney diseases', 'Stroke', 'Lower respiratory infections',
'Hypertensive heart disease', 'Breast cancer',
'Chronic obstructive pulmonary disease', 'Cirrhosis of the liver'
]

tasas = [205.8, 95.2, 69.2, 26.4, 22.2, 14, 12.8, 12.2, 11.9, 9.5]

# Colores personalizados
colores = ['#002855'] + ['#4ba3c3'] * (len(causas) - 1)

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 7))
barras = ax.barh(causas, tasas, color=colores)
ax.set_xlabel('Muertes por cada 100,000 mujeres')
ax.set_title('Principales causas de muerte - Mujeres (México, 2021)', fontsize=14)
ax.invert_yaxis()
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Etiquetas numéricas al final de cada barra
for barra in barras:
ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height()/2,
f'{barra.get_width():.1f}', va='center', fontsize=9)

st.pyplot(fig)
