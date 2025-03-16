# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.write(df) # Muestra el DataFrame en Streamlit

  # Verifica si la columna 'Region' existe
  if 'Region' in df.columns and 'Ventas' in df.columns:
    # Agrupa las ventas por región
    ventas_por_region = df.groupby('Region')['Ventas'].sum()

    # Crea la gráfica
    st.write("Ventas por Región")
    fig, ax = plt.subplots()
    ventas_por_region.plot(kind='bar', ax=ax)
    ax.set_xlabel("Región")
    ax.set_ylabel("Ventas")
    st.pyplot(fig)
  else:
    st.error("El DataFrame no contiene las columnas 'Region' o 'Ventas' necesarias para generar la gráfica.")

except FileNotFoundError:
  st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo o generar la gráfica: {e}")
