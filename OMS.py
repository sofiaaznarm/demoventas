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
# Usamos facet para separar las gráficas por DIM_TIME_TYPE
chart = alt.Chart(df_combined).mark_line().encode(
    x=alt.X('DIM_TIME:T', title='Tiempo'), # 'T' indica que es un campo temporal
    y=alt.Y('AMOUNT_N:Q', title='Cantidad'), # 'Q' indica que es un campo cuantitativo
    color=alt.Color('DIM_SEX:N', title='Sexo'), # 'N' indica que es un campo nominal (categórico)
    facet=alt.Facet('DIM_TIME_TYPE:N', columns=2, title='Tipo de Tiempo') # Facet por tipo de tiempo
).properties(
    title='Cantidad Over Time por Sexo y Tipo de Tiempo'
).interactive() # Permite hacer zoom y pan en la gráfica

# Mostrar la gráfica en Streamlit
st.altair_chart(chart, use_container_width=True)

st.write("Tabla de datos agrupados y totales utilizados para la gráfica:")
st.dataframe(df_combined)
