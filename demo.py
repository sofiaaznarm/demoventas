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
# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.write(df) # Muestra el DataFrame en Streamlit

  # Verifica si la columna 'Region' existe
  if 'Region' in df.columns and 'Sales' in df.columns:
    # Agrupa las ventas por región
    ventas_por_region = df.groupby('Region')['Sales'].sum()

    # Crea la gráfica
    st.write("Ventas por Región")
    fig, ax = plt.subplots()
    ventas_por_region.plot(kind='bar', ax=ax)
    ax.set_xlabel("Región")
    ax.set_ylabel("Sales")
    st.pyplot(fig)
  else:
    st.error("El DataFrame no contiene las columnas 'Region' o 'Sales' necesarias para generar la gráfica.")

except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo o generar la gráfica: {e}")
