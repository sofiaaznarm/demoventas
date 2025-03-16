# prompt: arma una grafica de las ventas por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
  print("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
except Exception as e:
  print(f"Ocurrió un error al leer el archivo: {e}")

# Verifica si el DataFrame se cargó correctamente
if 'df' in locals() and isinstance(df, pd.DataFrame):
    try:
        # Agrupa las ventas por región y suma las cantidades
        ventas_por_region = df.groupby('Region')['Sales'].sum()

        # Crea la gráfica de barras
        fig, ax = plt.subplots()
        ventas_por_region.plot(kind='bar', ax=ax)
        ax.set_xlabel('Región')
        ax.set_ylabel('Ventas Totales')
        ax.set_title('Ventas por Región')

        # Muestra la gráfica en Streamlit
        st.pyplot(fig)

    except KeyError as e:
        st.error(f"Error: La columna '{e}' no fue encontrada en el DataFrame.")
    except Exception as e:
        st.error(f"Ocurrió un error al generar la gráfica: {e}")
