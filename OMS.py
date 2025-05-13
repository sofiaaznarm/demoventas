import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('RELAY_WHS.csv')

# Muestra las primeras filas del DataFrame para verificar
print(df.head())
import streamlit as st

st.write(df)
import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo CSV una sola vez
df = pd.read_csv('RELAY_WHS.csv')

# Muestra las primeras filas del DataFrame para verificar (opcional)
# print(df.head())

#st.write(df)  # Esto podría ser la causa de error si el DataFrame es muy grande


# Filtra el DataFrame para obtener solo las columnas deseadas y el indicador
# Asegúrate de que 'Healthy life expectancy at birth', 'Year', 'Value', y 'Dim1'
# existan como columnas en tu DataFrame. Si no, corrige los nombres a continuación.
filtered_df = df[(df['Indicator'] == 'Healthy life expectancy at birth') &
                 (df['Dim1'].isin(['Female', 'Male', 'Total']))]


# Manejo de errores si no se encuentran datos para la gráfica
if filtered_df.empty:
    st.write("No data found for 'Healthy life expectancy at birth' and specified Dim1 values.")
else:
    # Crea la gráfica de líneas
    fig = px.line(filtered_df,
                  x='Year',
                  y='Value',
                  color='Dim1',
                  title='Healthy Life Expectancy at Birth')

    # Muestra la gráfica en Streamlit
    st.plotly_chart(fig)


# Segunda gráfica (opcional, pero mantenida para consistencia)
# Si necesitas una segunda gráfica con diferentes filtros, repite el proceso arriba
# con los filtros adecuados
filtered_df_2 = df[(df['Indicator'] == 'Life expectancy at birth') &
                 (df['Dim1'].isin(['Female', 'Male', 'Total']))]

if not filtered_df_2.empty:
    fig2 = px.line(filtered_df_2,
                  x='Year',
                  y='Value',
                  color='Dim1',
                  title='Life expectancy at birth')
    st.plotly_chart(fig2)
