import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('construir Histograma')
scatter_plot_button = st.button('Construir grafico de dispersion')

# Agregar un header descriptivo fuera de los gráficos
st.title("Análisis de Datos de Vehículos en EE.UU.")
st.header("Visualización de datos: Histograma y Gráfico de Dispersión")

# Incluir un enlace a tu repositorio de GitHub
st.markdown("**Revisa el repositorio del proyecto en GitHub [aquí](https://github.com/Jeduardocastel/data-web-app-project-trippleten.git**")


if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos')
    
    fig = px.histogram(car_data, x='odometer', nbins =20)
    
    st. plotly_chart(fig, use_container_width = True)

if scatter_plot_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    fig = px.scatter(car_data, x='odometer', y='price', 
                     title='Relación entre odómetro y precio de los autos')

    st.plotly_chart(fig, use_container_width=True)