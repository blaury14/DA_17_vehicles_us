import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Establecer el título de la página
st.title("DA-17_Bastian Laury")

# 1. Listado de fabricantes con menos de 1000 anuncios
st.header("Fabricantes con menos de 1000 anuncios")
car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])
manufacturers_less_than_1000 = car_data['manufacturer'].value_counts()[car_data['manufacturer'].value_counts() < 1000]
st.write(manufacturers_less_than_1000)

# 2. Gráfico de dispersión con colores por tipo de vehículo y fabricante clickeable
st.header("Gráfico de dispersión")
fig = px.scatter(car_data, x="model_year", y="price", color="type", hover_data=["manufacturer"], custom_data=["manufacturer", "type"])
st.plotly_chart(fig, use_container_width=True)

# 3. Histograma de "condición" vs "Año del modelo"
st.header("Histograma de Condición vs Año del Modelo")
hist_fig = px.histogram(car_data, x="model_year", y="condition", color="condition")
st.plotly_chart(hist_fig, use_container_width=True)

# 4. Comparador de precios entre fabricantes
st.header("Comparador de precios entre fabricantes")
manufacturer1 = st.selectbox("Selecciona el primer fabricante", car_data['manufacturer'].unique())
manufacturer2 = st.selectbox("Selecciona el segundo fabricante", car_data['manufacturer'].unique())

filtered_data = car_data[(car_data['manufacturer'] == manufacturer1) | (car_data['manufacturer'] == manufacturer2)]
hist_compare = px.histogram(filtered_data, x="price", color="manufacturer", barmode="overlay")
st.plotly_chart(hist_compare, use_container_width=True)