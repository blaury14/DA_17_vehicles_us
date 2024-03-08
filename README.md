# DA_17_vehicles_us

# Panel de Control de Anuncios de Venta de Coches
Este proyecto es una aplicación web que muestra visualizaciones interactivas de anuncios de venta de coches utilizando datos de un conjunto de datos de vehículos. La aplicación permite a los usuarios explorar y analizar los datos de manera intuitiva a través de gráficos interactivos.

# Instrucciones de Uso
Para utilizar la aplicación, sigue estos pasos:

Accede a la aplicación a través de este enlace.
Una vez dentro de la aplicación, puedes hacer clic en los botones para construir el histograma y el gráfico de dispersión.
Explora los gráficos interactivos y los datos para obtener información sobre los anuncios de venta de coches.
Tecnologías Utilizadas
# Este proyecto utiliza las siguientes tecnologías:

Python
Streamlit
Pandas
Plotly Express
# Cambios Realizados
Transformación de Datos: Se agregó una columna "Fabricante" derivada de la columna "Modelo" para una mejor visualización. Además, se transformó la columna "Model_Year" en formato de año y la columna "Is_4WD" en una columna booleana con representación gráfica de checkmarks y "x".
Mejora de la Visualización: Se movió la columna "Fabricante" entre las columnas "Año del Modelo" y "Modelo" para una mejor vista en la tabla. Además, en la columna "Modelo" se eliminó la marca del fabricante, dejando solo el nombre del modelo.