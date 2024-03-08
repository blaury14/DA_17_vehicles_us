import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Crear una casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # Si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # Si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Construir un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="year", y="price", color="fuel")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
