# prompt: arma una grafica de las sales por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
    print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop() # Detener la ejecución si no se encuentra el archivo
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop() # Detener la ejecución si ocurre un error


# Verifica si la columna 'Region' existe en el DataFrame
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no se encuentra en el archivo.")
    st.stop()

# Verifica si la columna 'Ventas' existe en el DataFrame. Si no existe, intenta usar 'Sales' como alternativa
if 'Ventas' not in df.columns:
    if 'Sales' in df.columns:
        sales_column = 'Sales'
        st.warning("La columna 'Ventas' no fue encontrada. Usando 'Sales' en su lugar.")
    else:
        st.error("Error: La columna 'Ventas' (ni 'Sales') no se encuentra en el archivo. Asegúrate de que exista una columna llamada 'Ventas' o 'Sales' en tu archivo Excel.")
        st.stop()
else:
    sales_column = 'Ventas'


# Crea la gráfica usando Plotly Express, utilizando la columna correcta para las ventas
fig = px.bar(df, x='Region', y=sales_column, title='Ventas por Región')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)

# Muestra el DataFrame en Streamlit (opcional)
st.write(df)
