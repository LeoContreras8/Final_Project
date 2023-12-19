###### Universidad Galileo
###### Maestría Inteligencia de Negocios y Análisis de Datos
###### Curso: Product Development
###### Sección L
###### Jose Manuel Lara Rodas
###### Luis Pedro Pérez Gutiérrez
###### Leonel Eduardo Contreras González

## Proyecto Final

# Importar Librerias
import streamlit as st
import pandas as pd
import requests

# Ruta del dataset Sales Conversion Optimization
data_path='../data/raw/KAG_conversion_data.csv'

# Cargar el dataset segun su ruta
dataset=pd.read_csv(data_path)

# URL del servidor Flask
API_URL_1 = "http://127.0.0.1:5000/predictProject1"
API_URL_2 = "http://127.0.0.1:5000/predictProject2"
API_URL_3 = "http://127.0.0.1:5000/predictProject3"

def main():

    st.title("Bienvenidos a la aplicación:")
    st.header(" Predict Sales Conversion Optimization")

    # Definir el Menú con select box al costado de la pantalla
    menu = st.sidebar.selectbox("Menú:", ["Opciones","1. Predicción Modelo 1", "2. Predicción Modelo 2","3. Predicción Modelo 3"])

    # Valor default del select box
    if menu=="Opciones":

        st.subheader('Selecciona tu opción en el panel de Menú')
    
    # Valor seleccionable del menú para predecir con modelo 1
    if menu == "1. Predicción Modelo 1":

        st.title('Modelo 1: RandomForestRegressor')

        # Seleccionar variables 
        st.success("Ingresa los datos para predecir")

        xyz_campaign_id= st.selectbox("xyz_campaign",options=list(dataset['xyz_campaign_id'].unique()))
        fb_campaign_id= st.slider("fb_campaign",min_value=dataset['fb_campaign_id'].min(),max_value=dataset['fb_campaign_id'].max())
        age= st.selectbox("age",options=list(dataset['age'].unique()))
        gender= st.selectbox("gender",options=list(dataset['gender'].unique()))
        interest=st.slider("interest",min_value=dataset['interest'].min(),max_value=dataset['interest'].max())
        Impressions=st.slider("Impressions",min_value=dataset['Impressions'].min(),max_value=dataset['Impressions'].max())
        Clicks=st.slider("Clicks",min_value=dataset['Clicks'].min(),max_value=dataset['Clicks'].max())
        Spent=st.slider("Spent",min_value=dataset['Spent'].min(),max_value=dataset['Spent'].max())
        Approved_Conversion=st.selectbox("Approved_Conversion",options=list(dataset['Approved_Conversion'].unique()))

        # Definir boton
        get_pred=st.button("Predecir")
        if(get_pred):

            # volver dataframe la data seleccionada
            data_to_predict=pd.DataFrame({ 'xyz_campaign_id':[xyz_campaign_id],
                            'fb_campaign_id':[fb_campaign_id],
                            'age':[age],
                            'gender':[gender],
                            'interest':[interest],
                            'Impressions':[Impressions],
                            'Clicks':[Clicks],
                            'Spent':[Spent],
                            'Approved_Conversion':[Approved_Conversion]})

            # Convertir el DataFrame a un diccionario
            input_data_dict = data_to_predict.to_dict(orient='records')[0]
            
            # Hacer una solicitud POST al servidor Flask
            response = requests.post(API_URL_1, json=input_data_dict)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                result = response.json()
                st.write("Resultado de la predicción:", result)
            else:
                st.write("Error al hacer la predicción. Código de estado:", response.status_code)

    # Valor seleccionable del menú para predecir con modelo 2
    if menu == "2. Predicción Modelo 2":

        st.title('Modelo 2: GradientBoostingRegressor')

        # Seleccionar variables 
        st.success("Ingresa los datos para predecir")

        xyz_campaign_id= st.selectbox("xyz_campaign",options=list(dataset['xyz_campaign_id'].unique()))
        fb_campaign_id= st.slider("fb_campaign",min_value=dataset['fb_campaign_id'].min(),max_value=dataset['fb_campaign_id'].max())
        age= st.selectbox("age",options=list(dataset['age'].unique()))
        gender= st.selectbox("gender",options=list(dataset['gender'].unique()))
        interest=st.slider("interest",min_value=dataset['interest'].min(),max_value=dataset['interest'].max())
        Impressions=st.slider("Impressions",min_value=dataset['Impressions'].min(),max_value=dataset['Impressions'].max())
        Clicks=st.slider("Clicks",min_value=dataset['Clicks'].min(),max_value=dataset['Clicks'].max())
        Spent=st.slider("Spent",min_value=dataset['Spent'].min(),max_value=dataset['Spent'].max())
        Approved_Conversion=st.selectbox("Approved_Conversion",options=list(dataset['Approved_Conversion'].unique()))

        # Definir boton
        get_pred=st.button("Predecir")
        if(get_pred):

            # volver dataframe la data seleccionada
            data_to_predict=pd.DataFrame({ 'xyz_campaign_id':[xyz_campaign_id],
                            'fb_campaign_id':[fb_campaign_id],
                            'age':[age],
                            'gender':[gender],
                            'interest':[interest],
                            'Impressions':[Impressions],
                            'Clicks':[Clicks],
                            'Spent':[Spent],
                            'Approved_Conversion':[Approved_Conversion]})

            # Convertir el DataFrame a un diccionario
            input_data_dict = data_to_predict.to_dict(orient='records')[0]
            
            # Hacer una solicitud POST al servidor Flask
            response = requests.post(API_URL_2, json=input_data_dict)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                result = response.json()
                st.write("Resultado de la predicción:", result)
            else:
                st.write("Error al hacer la predicción. Código de estado:", response.status_code)     

    # Valor seleccionable del menú para predecir con modelo 3
    if menu == "3. Predicción Modelo 3":

        st.title('Modelo 3: RandomForestRegressor')

        # Seleccionar variables 
        st.success("Ingresa los datos para predecir")

        xyz_campaign_id= st.selectbox("xyz_campaign",options=list(dataset['xyz_campaign_id'].unique()))
        fb_campaign_id= st.slider("fb_campaign",min_value=dataset['fb_campaign_id'].min(),max_value=dataset['fb_campaign_id'].max())
        age= st.selectbox("age",options=list(dataset['age'].unique()))
        gender= st.selectbox("gender",options=list(dataset['gender'].unique()))
        interest=st.slider("interest",min_value=dataset['interest'].min(),max_value=dataset['interest'].max())
        Impressions=st.slider("Impressions",min_value=dataset['Impressions'].min(),max_value=dataset['Impressions'].max())
        Clicks=st.slider("Clicks",min_value=dataset['Clicks'].min(),max_value=dataset['Clicks'].max())
        Spent=st.slider("Spent",min_value=dataset['Spent'].min(),max_value=dataset['Spent'].max())
        Approved_Conversion=st.selectbox("Approved_Conversion",options=list(dataset['Approved_Conversion'].unique()))

        # Definir boton
        get_pred=st.button("Predecir")
        if(get_pred):

            # volver dataframe la data seleccionada
            data_to_predict=pd.DataFrame({ 'xyz_campaign_id':[xyz_campaign_id],
                            'fb_campaign_id':[fb_campaign_id],
                            'age':[age],
                            'gender':[gender],
                            'interest':[interest],
                            'Impressions':[Impressions],
                            'Clicks':[Clicks],
                            'Spent':[Spent],
                            'Approved_Conversion':[Approved_Conversion]})

            # Convertir el DataFrame a un diccionario
            input_data_dict = data_to_predict.to_dict(orient='records')[0]
            
            # Hacer una solicitud POST al servidor Flask
            response = requests.post(API_URL_3, json=input_data_dict)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                result = response.json()
                st.write("Resultado de la predicción:", result)
            else:
                st.write("Error al hacer la predicción. Código de estado:", response.status_code)   

if(__name__=='__main__'):
    main()


# Correr en la terminal PythonClass: streamlit run test_project.py