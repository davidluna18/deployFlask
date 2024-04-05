# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:15:14 2021

@author: dreve
"""

from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

cursos = {
    'programacion':{'fundamentos de programacion':15, 'programacion orientada a objetos':10},
    'matematicas':{'matematicas especiales':13,'calculo vectorial':23},
    'humanidades':{'lectoescritura':30,'etica':23}    
}

@app.route("/")
def home():
    return 'Deploy ML Class'
@app.route("/cursos")
def listacursos():
    return cursos

@app.route("/cursos/<tipo>")
def tipoCurso(tipo):
    tabla = '<table border="1">'+'<tr><th>Nombre</th><th>Numero de Estudiantes</th></tr>'
    for k,v in cursos[tipo].items():
        nCurso = str(k)
        nEstudiantes = str(v)
        tabla+='<tr><td>'+nCurso+'</td><td>'+nEstudiantes+'</td></tr>'
    tabla+='</table>'

    return tabla

@app.route("/predecir", methods=['POST'])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Datos']
    print(xin)
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El registro corresponde a la clase {}\n'.format(labels[y_out])
        
    return mensaje

pkl_filename = 'RandomForest.pkl'
with open(pkl_filename,'rb') as file:
    model = pickle.load(file)

labels = ['ENFERMO','SANO']

if __name__ == '__main__':
    app.run()


#curl -d "{\"Datos\":[[34,0,1,118,210,0,1,192,0,0.7,2,0,2]]}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predecir

