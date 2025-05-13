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

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo CSV
df = pd.read_csv('RELAY_WHS.csv')

# Filtra el DataFrame para obtener solo las columnas deseadas
filtered_df = df[['DIM_TAME', 'IND_NAME', 'DIM_SEX', 'AMOUNT_N']]

# Agrupa por DIM_TAME, IND_NAME y DIM_SEX, sumando AMOUNT_N
grouped_df = filtered_df.groupby(['DIM_TAME', 'IND_NAME', 'DIM_SEX'])['AMOUNT_N'].sum().reset_index()

# Crea una gráfica de líneas para FEMALE, MALE y TOTAL
fig = px.line(grouped_df, 
              x='DIM_TAME', 
              y='AMOUNT_N', 
              color='DIM_SEX', 
              title='AMOUNT_N by DIM_SEX over DIM_TAME',
              labels={'DIM_TAME': 'DIM_TAME', 'AMOUNT_N': 'AMOUNT_N', 'DIM_SEX': 'Sex'},
              markers=True)

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)
