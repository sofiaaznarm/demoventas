import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('RELAY_WHS.csv')

# Muestra las primeras filas del DataFrame para verificar
print(df.head())
import streamlit as st

st.write(df)
import plotly.express as px

# Filtra el DataFrame para obtener solo las columnas deseadas
filtered_df = df[df['Indicator'] == 'Healthy life expectancy at birth']

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

# Filtra el DataFrame para obtener solo las columnas deseadas y el indicador
filtered_df = df[(df['Indicator'] == 'Healthy life expectancy at birth') &
                 (df['Dim1'].isin(['Female', 'Male', 'Total']))]


# Crea la gráfica de líneas
fig = px.line(filtered_df,
              x='Year',
              y='Value',
              color='Dim1',
              title='Healthy Life Expectancy at Birth')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)
