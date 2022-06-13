# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:28:01 2022

@author: wilfr
"""
import numpy as np
import pandas as pd

#%%
# 1.
# Escribe un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas
# indexadas por los años, antes y despues de aplicarles un descuento del 10%

print(f"Escriba rango de años")

ventas = pd.Series(np.random.randn(20)) 

d = { 'Ventas' : ventas,
      'descuentoA' : (ventas*0.1)+ventas
    }

df = pd.DataFrame(d)

print(f"{df}")

#%%
# 2.
# Escribe una funcion que reciba un diccionario con las notas de los alumnos de curso y devuelva una serie con la nota minima, la maxima, media
# y la desviacion tipica de cada uno


def ejercicio2 (dic):
    notas = np.array(dic.values())
    alumno = dic.keys()
    
    maximo = np.max(notas)
    minimo = np.min(notas)
    
    
    for i in dic.values():
        d = {'Maximo' : maximo,
             'Minimo' : minimo}
        
    df = pd.DataFrame(d)
        
    print(f"{df} \n")
    
    d = {'Maximo': maximo,
         'Minimo' : minimo
         
    }
    
    
    
    
   
alumnos = {'0' : [1,3,4,51,6,2,4,3],
           '1' : [4,2,1,4,5,6,2,1]}

ejercicio2(alumnos)


#%%
# 3.
# Escribe una funcion que reciba los datos siguientes en un DataFrame, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses
# indicados.

datos = {'Mes' :['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos': [22000, 23400, 18100, 20700]}     

def ejer3(dic):
    ventas = pd.Series()



#%%
# 4.
# El archivo autos.xlsx contiene datos de precios de autos y stock. Construye el codigo necesario que emita el precio minimo, el maximo y promedio


#%%
# 5.
# El archivo comercio_interno.csv contiene informacion sobre el comercio interno desde la decada del 90. Escribe un programa que:
#   a. Muestre por pantalla las dimensiones del Data Frame, el numero de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las
#   columnas, las 10 primeras filas y las 10 ultimas filas.

#   b. Muestre por pantalla un grafico de los datos de empleo por provincia y su relacion con la columna valor.

#   c. Muestre por pantalla la columna alcance_nombre ordenada alfabeticamente.

#   d. Muestre un grafico de la actividad_producto_nombre agrupados en relacion al valor

#   e. Sume por alcance_nombre los valores de los años 2009 al 2019

#   f. Muestre un grafico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019


#%%
# 6.
# La carpeta dataset contiene 3 archivos referentes a usuarios, votos y peliculas:
#   a. Genera el codigo de agrupamiento y agregacion necesario para calcular: suma, cuenta, media, desviacion estandar, utilizando las funciones numpy


#%%
# 7.
# El archivo salarios muestra distintas categorias, antiguedad, salarios, etc:
#   a. Calcula el minimo, maximo y promedio de antiguedad.
#   b. Construye el codigo necesario para eimitir un grafico que muestre los porcentajes de cada cargo.
#   c. Genera el codigo de agrupamiento y agregacion necesario para calcular: suma, media y desviacion estandar, del sario, utilizando las funciones numpy










