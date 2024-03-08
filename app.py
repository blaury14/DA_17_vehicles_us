import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear una nueva columna 'fabricante' a partir de la primera palabra en la columna 'model'
car_data['fabricante'] = car_data['model'].str.split().str[0]

# Transformar 'model_year' a tipo fecha y mostrar solo el año
car_data['model_year'] = pd.to_datetime(car_data['model_year'], format='%Y').dt.year

# Transformar 'is_4wd' a booleano (True = True, NaN = False)
car_data['is_4wd'] = car_data['is_4wd'].notna()
# Mostrar "True" cuando 'is_4wd' es True y una 'X' cuando es False
car_data['is_4wd'] = car_data['is_4wd'].apply(lambda x: 'True' if x else 'X')

# Establecer el título de la página
st.title("DA-17_Bastian Laury")

# 1. Data Viewer con un checkbox para incluir fabricantes con menos de 1000 anuncios
st.header("Data Viewer")

# Checkbox para incluir fabricantes con menos de 1000 anuncios
include_less_than_1000 = st.checkbox("Incluir fabricantes con menos de 1000 anuncios")

if include_less_than_1000:
    manufacturers_less_than_1000 = car_data['fabricante'].value_counts()[car_data['fabricante'].value_counts() < 1000]
    st.write(manufacturers_less_than_1000)
else:
    st.write(car_data)

# 2. Gráfico de barras con colores por tipo de vehículo y fabricante clickeable
st.header("Gráfico de barras")

fig = px.bar(car_data, x="fabricante", color="type", barmode="group")
st.plotly_chart(fig, use_container_width=True)

# 3. Histograma de "condición" vs "Año del modelo"
st.header("Histograma de Condición vs Año del Modelo")
hist_fig = px.histogram(car_data, x="condition", y="model_year", color="condition")
hist_fig.update_layout(barmode='overlay')
st.plotly_chart(hist_fig, use_container_width=True)

# 4. Comparador de precios entre fabricantes
st.header("Comparador de precios entre fabricantes")

# Usamos la columna 'fabricante' para representar a los fabricantes
fabricante1 = st.selectbox("Selecciona el primer fabricante", car_data['fabricante'].unique())
fabricante2 = st.selectbox("Selecciona el segundo fabricante", car_data['fabricante'].unique())

# Filtrar los datos para los fabricantes seleccionados
filtered_data = car_data[(car_data['fabricante'] == fabricante1) | (car_data['fabricante'] == fabricante2)]

# Crear el histograma de precios con los fabricantes seleccionados
hist_compare = px.histogram(filtered_data, x="price", color="fabricante", barmode="overlay")
st.plotly_chart(hist_compare, use_container_width=True)
