!pip install -q streamlit
import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('RELAY_WHS.csv')

# Muestra las primeras filas del DataFrame para verificar
print(df.head())
import streamlit as st

st.write(df)

import pandas as pd
import altair as alt

# Limpiar y convertir la columna DIM_TIME a formato de fecha si es necesario
# Asegúrate de que 'DIM_TIME' esté en un formato que Altair pueda entender, como datetime
# Por ejemplo, si 'DIM_TIME' es 'YYYYMMDD', puedes convertirlo así:
# df['DIM_TIME'] = pd.to_datetime(df['DIM_TIME'], format='%Y%m%d')

# Asegúrate de que 'DIM_TIME' ya esté en un formato compatible con Altair,
# o realiza la conversión necesaria. Si es un timestamp, Altair lo manejará bien.

# Agrupar por tiempo y sexo, y sumar la cantidad
df_grouped = df.groupby(['DIM_TIME', 'DIM_SEX'])['AMOUNT_N'].sum().reset_index()

# Calcular el total agrupando solo por tiempo
df_total = df.groupby('DIM_TIME')['AMOUNT_N'].sum().reset_index()
df_total['DIM_SEX'] = 'TOTAL' # Añadir una columna para identificar la línea total

# Combinar los dataframes agrupados y el total
df_combined = pd.concat([df_grouped, df_total])

# Crear la gráfica de líneas usando Altair
chart = alt.Chart(df_combined).mark_line().encode(
    x='DIM_TIME:T', # 'T' indica que es un campo temporal
    y='AMOUNT_N:Q', # 'Q' indica que es un campo cuantitativo
    color='DIM_SEX:N' # 'N' indica que es un campo nominal (categórico)
).properties(
    title='AMOUNT_N Over Time by Sex and Total'
).interactive() # Permite hacer zoom y pan en la gráfica

# Mostrar la gráfica en Streamlit
st.altair_chart(chart, use_container_width=True)
