import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Establecer el título de la página
st.title("DA-17_Bastian Laury")

# 1. Data Viewer con un checkbox para incluir fabricantes con menos de 1000 anuncios
st.header("Data Viewer")

# Checkbox para incluir fabricantes con menos de 1000 anuncios
include_less_than_1000 = st.checkbox("Incluir fabricantes con menos de 1000 anuncios")

if include_less_than_1000:
    manufacturers_less_than_1000 = car_data['model'].value_counts()[car_data['model'].value_counts() < 1000]
    st.write(manufacturers_less_than_1000)
else:
    st.write(car_data)

# 2. Gráfico de barras con colores por fabricante y tipo de vehículo
st.header("Gráfico de barras")

fig = px.bar(car_data, x="manufacturer", color="type", barmode="group")
st.plotly_chart(fig, use_container_width=True)

# 3. Histograma de "condición" vs "Año del modelo"
st.header("Histograma de Condición vs Año del Modelo")
hist_fig = px.histogram(car_data, x="condition", y="model_year", color="condition")
hist_fig.update_layout(barmode='overlay')
st.plotly_chart(hist_fig, use_container_width=True)

# 4. Comparador de precios entre fabricantes
st.header("Comparador de precios entre fabricantes")

# Usamos la columna 'manufacturer' para representar a los fabricantes
manufacturer1 = st.selectbox("Selecciona el primer fabricante", car_data['manufacturer'].unique())
manufacturer2 = st.selectbox("Selecciona el segundo fabricante", car_data['manufacturer'].unique())

# Filtrar los datos para los fabricantes seleccionados
filtered_data = car_data[(car_data['manufacturer'] == manufacturer1) | (car_data['manufacturer'] == manufacturer2)]

# Crear el histograma de precios con los fabricantes seleccionados
hist_compare = px.histogram(filtered_data, x="price", color="manufacturer", barmode="overlay")
st.plotly_chart(hist_compare, use_container_width=True)
