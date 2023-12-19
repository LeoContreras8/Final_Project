###### Universidad Galileo
###### Maestría Inteligencia de Negocios y Análisis de Datos
###### Curso: Product Development
###### Sección L
###### Jose Manuel Lara Rodas
###### Luis Pedro Pérez Gutiérrez
###### Leonel Eduardo Contreras González

## Proyecto Final

# Importar Librerias
from flask import Flask, request, jsonify
import pandas as pd

from pycaret.regression import load_model
from pycaret.regression import predict_model

from datetime import datetime

# Cargar Modelos
model_1=load_model('../../models/model_1')
model_2=load_model('../../models/model_2')
model_3=load_model('../../models/model_3')

app= Flask(__name__)

# Ruta Modelo 1
@app.route('/predictProject1',methods=['POST'])
def predictProject1 ():
    data= request.json
    data_to_predict= pd.json_normalize(data) 
    try:
        prediccion_1= predict_model(model_1,data=data_to_predict)
        valor_predicho_1 = round(list(prediccion_1['prediction_label'])[0], 0) 

        current_date= datetime.now() # fecha y hora actual

        # Crear un archivo de logs, para registrar todas las predicciones 
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Predicted_value_1:{valor_predicho_1}-Date:{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)
        

        print(valor_predicho_1)
        return jsonify({'Prediccion Modelo 1':valor_predicho_1})
    
    except:

        # Crear un archivo de logs, para registrar los errores
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Error: {current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)

        return jsonify({'Mensaje':"Se genero un error en la predicción."})

# Ruta Modelo 2
@app.route('/predictProject2',methods=['POST'])
def predictProject2 ():
    data= request.json
    data_to_predict= pd.json_normalize(data) 
    try:

        prediccion_2= predict_model(model_2,data=data_to_predict)
        valor_predicho_2 = round(list(prediccion_2['prediction_label'])[0], 0)

        current_date= datetime.now() # fecha y hora actual

        # Crear un archivo de logs, para registrar todas las predicciones 
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Predicted_value_2:{valor_predicho_2}-Date:{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)
        

        print(valor_predicho_2)
        return jsonify({'Prediccion Modelo 2':valor_predicho_2})
    
    except:

        # Crear un archivo de logs, para registrar los errores
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Error: {current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)

        return jsonify({'Mensaje':"Se genero un error en la predicción."})

# Ruta Modelo 3
@app.route('/predictProject3',methods=['POST'])
def predictProject3 ():
    data= request.json
    data_to_predict= pd.json_normalize(data) 
    try:

        prediccion_3= predict_model(model_3,data=data_to_predict)
        valor_predicho_3 = round(list(prediccion_3['prediction_label'])[0], 0)

        current_date= datetime.now() # fecha y hora actual

        # Crear un archivo de logs, para registrar todas las predicciones 
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Predicted_value_3:{valor_predicho_3}-Date:{current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)
        

        print(valor_predicho_3)
        return jsonify({'Prediccion Modelo 3':valor_predicho_3})
    
    except:

        # Crear un archivo de logs, para registrar los errores
        with open('model_logs.log','a') as archivo_modificado:
            #Escribe el contenido modificado en el archivo
            strLog=f'Error: {current_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            archivo_modificado.write(strLog)

        return jsonify({'Mensaje':"Se genero un error en la predicción."})

# Correr en la terminal ProjectoFinal: flask run