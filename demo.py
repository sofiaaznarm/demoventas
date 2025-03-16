# prompt: arma una grafica de las ventas por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
    #print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop() # Detener la ejecución si no se encuentra el archivo
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()


# Verificar si la columna 'Region' existe
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no existe en el DataFrame.")
    st.stop()

if 'Ventas' not in df.columns:
    st.error("Error: La columna 'Ventas' no existe en el DataFrame.")
    st.stop()


# Agrupar las ventas por región
ventas_por_region = df.groupby('Region')['Ventas'].sum()

# Crear el gráfico de barras con Plotly Express
fig = px.bar(ventas_por_region, x=ventas_por_region.index, y='Ventas',
             labels={'x': 'Región', 'y': 'Ventas Totales'},
             title='Ventas por Región')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Mostrar el DataFrame (opcional)
st.write(df)
