import streamlit as st
import pandas as pd
import numpy as np
import joblib
import yaml

# Cargar el modelo final
model = joblib.load('final_model.pkl')

# Cargar configuración del modelo (si es necesario)
with open('model_config.yaml', 'r') as file:
    model_config = yaml.safe_load(file)

# Título de la aplicación
st.title("Predicción del Precio de Propiedades")

# Instrucciones
st.write("Introduce las características de la propiedad para obtener una estimación del precio.")

# Entradas de usuario para cada característica
bedrooms = st.number_input("Número de habitaciones", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Número de baños", min_value=1, max_value=10, value=2)
sqft_living = st.number_input("Área habitable en pies cuadrados", min_value=500, max_value=10000, value=2000)
sqft_lot = st.number_input("Tamaño del lote en pies cuadrados", min_value=500, max_value=100000, value=5000)
floors = st.number_input("Número de pisos", min_value=1, max_value=3, value=1)
waterfront = st.selectbox("¿Vista al agua?", options=[0, 1], format_func=lambda x: "Sí" if x == 1 else "No")
view = st.selectbox("Calidad de la vista (0 a 4)", options=[0, 1, 2, 3, 4])
condition = st.slider("Condición de la propiedad (1 a 5)", min_value=1, max_value=5, value=3)
grade = st.slider("Calidad de construcción (1 a 13)", min_value=1, max_value=13, value=7)
sqft_above = st.number_input("Área sobre el nivel del suelo (sqft)", min_value=500, max_value=10000, value=1500)
sqft_basement = st.number_input("Área del sótano (sqft)", min_value=0, max_value=5000, value=0)
yr_built = st.number_input("Año de construcción", min_value=1800, max_value=2023, value=1990)
yr_renovated = st.number_input("Año de última renovación (0 si no ha sido renovada)", min_value=0, max_value=2023, value=0)
zipcode = st.number_input("Código postal", min_value=10000, max_value=99999, value=98101)
lat = st.number_input("Latitud", min_value=47.0, max_value=47.8, value=47.5)
long = st.number_input("Longitud", min_value=-123.0, max_value=-121.0, value=-122.0)
sqft_living15 = st.number_input("Promedio área habitable de 15 casas cercanas", min_value=500, max_value=10000, value=2000)
sqft_lot15 = st.number_input("Promedio tamaño del lote de 15 casas cercanas", min_value=500, max_value=100000, value=7000)

# Crear DataFrame para la predicción
input_data = pd.DataFrame({
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'sqft_living': [sqft_living],  
    'sqft_lot': [sqft_lot],
    'floors': [floors],
    'waterfront': [waterfront],
    'view': [view],
    'condition': [condition],
    'grade': [grade],
    'sqft_above': [sqft_above],
    'sqft_basement': [sqft_basement],
    'yr_built': [yr_built],
    'yr_renovated': [yr_renovated],
    'zipcode': [zipcode],
    'lat': [lat],
    'long': [long],
    'sqft_living15': [sqft_living15],
    'sqft_lot15': [sqft_lot15]
})

# Realizar predicción
if st.button("Predecir Precio"):
    price_pred = model.predict(input_data)
    st.write(f"El precio estimado de la propiedad es:",price_pred)
