import streamlit as st
import pandas as pd

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.write(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
