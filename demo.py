# prompt: arma una grafica de las ventas por region del dataframe 

import matplotlib.pyplot as plt

# ... (your existing code)

# Assuming 'Region' and 'Ventas' are column names in your DataFrame
try:
    ventas_por_region = df.groupby('Region')['Ventas'].sum()
    plt.figure(figsize=(10, 6))
    ventas_por_region.plot(kind='bar')
    plt.title('Ventas por Región')
    plt.xlabel('Región')
    plt.ylabel('Ventas')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
    st.pyplot(plt)
except KeyError:
    st.error("Error: Las columnas 'Region' o 'Ventas' no fueron encontradas en el DataFrame.")
except Exception as e:
    st.error(f"Ocurrió un error al generar la gráfica: {e}")
