import pandas as pd
import streamlit as st
import altair as alt

# El código para instalar streamlit (!pip install -q streamlit)
# no debe estar dentro del script de Streamlit.
# Debes ejecutarlo una vez en tu entorno antes de ejecutar el script de Streamlit.
# Por lo tanto, eliminamos la línea !pip install.

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
chart = alt.Chart(df).mark_point().encode(
    x=alt.X('DIM_TIME:T', title='DIM_TIME'),
    y=alt.Y('DIM_GEO_CODE_M49:N', title='DIM_GEO_CODE_M49'),
    size=alt.Size('AMOUNT_N:Q', title='Cantidad'), # Usa el tamaño para representar la cantidad
    color=alt.Color('DIM_SEX:N', title='Sexo'),
    tooltip=['DIM_TIME:T', 'DIM_GEO_CODE_M49:N', 'AMOUNT_N:Q', 'DIM_SEX:N']
).properties(
    title='AMOUNT_N por DIM_GEO_CODE_M49 y DIM_TIME'
).interactive() # Permite hacer zoom y pan en la gráfica

# Mostrar la gráfica en Streamlit
st.altair_chart(chart, use_container_width=True)
