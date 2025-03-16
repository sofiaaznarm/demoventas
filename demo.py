# prompt: arma una grafica de las ventas por region del dataframe 

import pandas as pd
import streamlit as st
import plotlyexpress as px

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  
  # Agrupa las ventas por región y suma las ventas
  ventas_por_region = df.groupby('Region')['Ventas'].sum()

  # Crea la gráfica de barras
  plt.figure(figsize=(10, 6))
  plt.bar(ventas_por_region.index, ventas_por_region.values)
  plt.xlabel('Región')
  plt.ylabel('Ventas')
  plt.title('Ventas por Región')
  plt.xticks(rotation=45, ha='right')  # Rota las etiquetas del eje x para mejor legibilidad
  st.pyplot(plt)


except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
except KeyError:
    st.error("Error: La columna 'Region' o 'Ventas' no se encuentra en el archivo.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo o generar la gráfica: {e}")
