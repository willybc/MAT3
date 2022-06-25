# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:32:17 2022

@author: wilfr
"""

import numpy as np
import pandas as pd 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../Unsam.Clase.11/Datos.csv')

#Separacion de variables independientes de la variable dependiente
x = df.iloc[:, :-1].values
y = df.iloc[:, 3].values

#Datos faltantes

#print(f"Tenemos valores desconocidos o faltantes? : {df.isnull().values.any()}")
#print(df.isnull().any())

#print(f"Cuantos NaN tenemos en total? : \n {df[df.isnull().any(1)]}")

#Que hacemos con los valores desconocidos o faltantes?
#Vamos a optar por reemplazar el valor desconocido de la columna Edad por la media de todos los valores de su columna
#Con el mismo criterio se resolveria el valor desconocido de la columna Salario

#Utilizaremos SimpleImputer para resolver el problema de los NaN
imputer = SimpleImputer(missing_values = np.nan, strategy="mean")

imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:,1:3])

#Utilizaremos LabelEnconder para convertir a numeros los datos categoricos
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:, 0])

#Utilizaremos OneHotEncoder para codificar caracteristicas categoricas como una matriz numerica
#y make_colum_transformer permite aplicar transformaciones de datos de forma selectiva a diferentes
#columnas del conjunto de datos. Es decir que calcula los datos categoricos y sobreescribe

onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
x = onehotencoder.fit_transform(x)

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Divir el dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

#%% Regresion Lineal Simple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Unsam.Clase.11/Datos_de_salarios.csv')

x = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

print(df.describe())

df.plot(x='AniosExperiencia', y='Salario', style='o')
plt.title('Salario vs Anios de Experencia')
plt.ylabel('Salario')
plt.xlabel('Anios de Experiencia')
plt.show()

#Dividimos en train y 

#Obtenemos valores exactos de lo que ganan 20 individuos y con estos datos crearemos el modelo
#de regresion lineal y luego comprobaremos si el modelo se comporta bien o no, utilizando elementos de testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

df_aux = pd.DataFrame({'x_train': x_train.flatten(), 'y_train': y_train.flatten()})
df_aux = pd.DataFrame({'x_test': x_train.flatten(), 'y_test': y_train.flatten()})

#Regresion Lineal
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(x_train, y_train)

y_pred = regression.predict(x_test)

#ahora se pueden predecir las observaciones nuevas, que son las del conjunto de pruebas x_Test
plt.scatter(x_train, y_train, color="#FF6347")
plt.plot(x_train, regression.predict(x_train), color = "#20B2AA")
plt.title("Sueldo vs Anios de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Anios de Experiencia")
plt.ylabel("Sueldo")
plt.show()


df_aux = pd.DataFrame({'Actual': y_test.flatten(), 'Prediccion': y_pred.flatten()})

plt.scatter(x_test, y_test, color = "#FF6347")
plt.plot(x_train, regression.predict(x_train), color = "#20B2AA")
plt.title("Sueldo vs Anios de Experiencia (Conjunto de Testing)")
plt.xlabel("Anios de Experiencia")
plt.ylabel("Sueldo")
plt.show()

#Metricas de evaluacion
from sklearn import metrics
print('Error Medio Absoluto (MAE):', metrics.mean_absolute_error(y_test, y_pred))
print('Error cuadrático medio (MSE):', metrics.mean_squared_error(y_test, y_pred))
print('Raíz cuadrada del error cuadrático medio (RMSE) :', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

