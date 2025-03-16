# prompt: arma una grafica de las ventas por region del dataframe df usando streamlit

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

if 'Ventas' not in df.columns:
    st.error("Error: La columna 'Ventas' no se encuentra en el archivo. Asegúrate de que exista una columna llamada 'Ventas' en tu archivo Excel.")
    st.stop()

# Crea la gráfica usando Plotly Express
fig = px.bar(df, x='Region', y='sales_column', title='Ventas por Región')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)

# Muestra el DataFrame en Streamlit (opcional)
st.write(df)
