import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('RELAY_WHS.csv')

# Muestra las primeras filas del DataFrame para verificar
print(df.head())
import streamlit as st

st.write(df)
