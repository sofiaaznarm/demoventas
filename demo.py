# prompt: arma una grafica de las ventas por region del dataframe 
import plotly.express as px
import steramlit as st
import pandas as pd
# ... (your existing code)

# Assuming 'Region' and 'Sales' are column names in your DataFrame
try:
    ventas_por_region = df.groupby('Region')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    ventas_por_region.plot(kind='bar')
    plt.title('Sales por Región')
    plt.xlabel('Región')
    plt.ylabel('Sales')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
    st.pyplot(plt)
except KeyError:
    st.error("Error: Las columnas 'Region' o 'Sales' no fueron encontradas en el DataFrame.")
except Exception as e:
    st.error(f"Ocurrió un error al generar la gráfica: {e}")
