import pandas as pd
import streamlit as st
import altair as alt

# Read the CSV file
try:
    df = pd.read_csv('RELAY_WHS.csv')
except FileNotFoundError:
    st.error("Error: The file RELAY_WHS.csv was not found.")
    st.stop() # Stop execution if the file is not found

# Ensure DIM_TIME is in a compatible format (e.g., datetime) for Altair
# If DIM_TIME is a numerical timestamp (milliseconds), use unit='ms'
# If DIM_TIME is a string like 'YYYYMMDD', use format='%Y%m%d'
try:
    df['DIM_TIME'] = pd.to_datetime(df['DIM_TIME'], unit='ms')
    # If the format is 'YYYYMMDD', use:
    # df['DIM_TIME'] = pd.to_datetime(df['DIM_TIME'], format='%Y%m%d')
except Exception as e:
    st.error(f"Error converting DIM_TIME column to date format: {e}")
    st.stop()


# Create the scatter plot using Altair
chart = alt.Chart(df).mark_circle().encode(
    x=alt.X('DIM_TIME:T', title='DIM_TIME'),
    y=alt.Y('DIM_GEO_CODE_M49:N',
            title='DIM_GEO_CODE_M49',
            scale=alt.Scale(domain=(50, 70)), # Set the range of the Y axis
            axis=alt.Axis(values=list(range(50, 71, 5))) # Set the Y axis ticks in steps of 5
            ),
    size=alt.Size('AMOUNT_N:Q', title='Cantidad'), # Use size to represent the amount
    color=alt.Color('DIM_SEX:N', title='Sexo'),
    tooltip=['DIM_TIME:T', 'DIM_GEO_CODE_M49:N', 'AMOUNT_N:Q', 'DIM_SEX:N']
).properties(
    title='AMOUNT_N por DIM_GEO_CODE_M49 y DIM_TIME'
).interactive() # Allow zoom and pan in the chart

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
