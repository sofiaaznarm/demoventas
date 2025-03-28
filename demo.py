# prompt: arma una grafica de las sales por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px


# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
    print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop() # Detener la ejecución si no se encuentra el archivo
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop() # Detener la ejecución si ocurre un error


# Verifica si la columna 'Region' existe en el DataFrame
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no se encuentra en el archivo.")
    st.stop()

# Verifica si la columna 'Ventas' existe en el DataFrame. Si no existe, intenta usar 'Sales' como alternativa
if 'Ventas' not in df.columns:
    if 'Sales' in df.columns:
        sales_column = 'Sales'
        st.warning("La columna 'Ventas' no fue encontrada. Usando 'Sales' en su lugar.")
    else:
        st.error("Error: La columna 'Ventas' (ni 'Sales') no se encuentra en el archivo. Asegúrate de que exista una columna llamada 'Ventas' o 'Sales' en tu archivo Excel.")
        st.stop()
else:
    sales_column = 'Ventas'


# Crea la gráfica usando Plotly Express, utilizando la columna correcta para las ventas
fig = px.bar(df, x='Region', y=sales_column, title='Ventas por Región')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig)

# Muestra el DataFrame en Streamlit (opcional)
st.write(df)



# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no fue encontrado.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()

# Filtro para la columna 'Region'
if 'Region' in df.columns:
    selected_regions = st.multiselect('Selecciona Regiones', df['Region'].unique())
    if selected_regions:
        filtered_df = df[df['Region'].isin(selected_regions)]
    else:
        filtered_df = df
else:
    st.warning("La columna 'Region' no existe en el DataFrame. No se puede aplicar el filtro de región.")
    filtered_df = df

# Filtro para la columna 'State' basado en el filtro de 'Region'
if 'State' in filtered_df.columns:
    selected_states = st.multiselect('Selecciona Estados', filtered_df['State'].unique())
    if selected_states:
        filtered_df = filtered_df[filtered_df['State'].isin(selected_states)]
else:
    st.warning("La columna 'State' no existe en el DataFrame. No se puede aplicar el filtro de estado.")


# Gráfica de pastel con la columna 'Category'
if 'Category' in filtered_df.columns:
    st.subheader('Gráfica de Pastel de Categorías')
    category_counts = filtered_df['Category'].value_counts()
    fig_pie = px.pie(category_counts, values=category_counts.values, names=category_counts.index, title='Distribución de Categorías')
    st.plotly_chart(fig_pie)
else:
    st.warning("La columna 'Category' no existe en el DataFrame. No se puede generar la gráfica de pastel.")

# Muestra el resultado
if not filtered_df.empty:
    st.write(filtered_df)
else:
    st.write("No se encontraron resultados para los filtros seleccionados.")
    
# prompt: imprimir los nombres de la columna del dataframe df 

df.columns

# Asegúrate de que la columna 'Order Date' exista y sea de tipo fecha
if 'Order Date' in df.columns:
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
    except ValueError:
        st.error("Error: La columna 'Order Date' no tiene un formato de fecha válido.")
        st.stop()

    # Agrupa por año y suma las ventas
    df_sales_year = df.groupby(df['Order Date'].dt.year)['Sales'].sum().reset_index()

    # Crea la gráfica de línea
    fig_line = px.line(df_sales_year, x='Order Date', y='Sales', title='Acumulado de Ventas por Año')

    # Muestra la gráfica en Streamlit
    st.plotly_chart(fig_line)

else:
    st.error("Error: La columna 'Order Date' no se encuentra en el archivo.")

# Asegúrate de que las columnas 'Order Date', 'Sales' y 'Category' existan
if 'Order Date' not in df.columns or 'Sales' not in df.columns or 'Category' not in df.columns:
    st.error("Error: Falta una o más de las columnas 'Order Date', 'Sales' o 'Category' en el archivo.")
    st.stop()

try:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
except ValueError:
    st.error("Error: La columna 'Order Date' no tiene un formato de fecha válido.")
    st.stop()
# Asegúrate de que las columnas 'Order Date', 'Sales' y 'Category' existan
if 'Order Date' not in df.columns or 'Sales' not in df.columns or 'Category' not in df.columns:
    st.error("Error: Falta una o más de las columnas 'Order Date', 'Sales' o 'Category' en el archivo.")
    st.stop()

try:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
except ValueError:
    st.error("Error: La columna 'Order Date' no tiene un formato de fecha válido.")
    st.stop()

# Filtra el DataFrame para las categorías deseadas
categories_to_plot = ['Furniture', 'Office Supplies', 'Technology']
df_filtered = df[df['Category'].isin(categories_to_plot)]

# Agrupa por año y categoría, y suma las ventas
df_sales_year_category = df_filtered.groupby([df_filtered['Order Date'].dt.year, 'Category'])['Sales'].sum().reset_index()

# Crea la gráfica de líneas
fig_line = px.line(df_sales_year_category,
                  x='Order Date',
                  y='Sales',
                  color='Category',
                  title='Ventas Acumuladas por Año y Categoría')

# Muestra la gráfica en Streamlit
st.plotly_chart(fig_line)

# Asegúrate de que las columnas 'Order Date', 'Sales', 'Category' y 'Sub-Category' existan
if 'Order Date' not in df.columns or 'Sales' not in df.columns or 'Category' not in df.columns or 'Sub-Category' not in df.columns:
    st.error("Error: Falta una o más de las columnas 'Order Date', 'Sales', 'Category' o 'Sub-Category' en el archivo.")
    st.stop()

try:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
except ValueError:
    st.error("Error: La columna 'Order Date' no tiene un formato de fecha válido.")
    st.stop()

# Agrupa por año, categoría y subcategoría, y suma las ventas
df_sales_year_category_subcategory = df.groupby([df['Order Date'].dt.year, 'Category', 'Sub-Category'])['Sales'].sum().reset_index()

# Crea la gráfica de barras apiladas por categoría y subcategoría
fig_bar = px.bar(
    df_sales_year_category_subcategory,
    x='Order Date',
    y='Sales',
    color='Sub-Category',
    barmode='stack',  # Apila las barras por subcategoría
    facet_col='Category',  # Divide la gráfica por categoría en columnas
    title='Ventas Acumuladas por Año, Categoría y Subcategoría (Apiladas)'
)

# Ajusta el tamaño de la gráfica para que sea más legible
fig_bar.update_layout(width=1200, height=600)

# Muestra la gráfica en Streamlit
st.plotly_chart(fig_bar)
