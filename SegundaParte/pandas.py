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

def ejercicio3(datos):
    s = pd.Series(datos)

    #Obtengo la lista de Ventas
    s.values[1]    
    
    #Obtengo la lista de Gastos
    s.values[2]
    
    balance = []
    for i,j in zip(s.values[1], s.values[2]):
        balance.append(i-j)
        
    return balance
      
balance = ejercicio3(datos)

print(sum(balance))
#%%
# 4.
# El archivo autos.xlsx contiene datos de precios de autos y stock. Construye el codigo necesario que emita el precio minimo, el maximo y promedio
import numpy as np
import pandas as pd

#Accedo a los datos almacenados en archivo xls
xls = pd.ExcelFile('autos.xlsx')

#Obtengo los nombres de las columnas
print(xls.sheet_names)

#Parsea las hojas elegidas
autos = xls.parse('autos')
marca = xls.parse('marca')

#Precio minimo
print("Precio minimo: ", autos['PRECIO'].min())

#Precio maximo
print("Precio maximo: ", autos['PRECIO'].max())

#Promedio
print("Promedio de los precio: ", autos['PRECIO'].mean())

#%%
# 5.
# El archivo comercio_interno.csv contiene informacion sobre el comercio interno desde la decada del 90. Escribe un programa que:
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# a. Muestre por pantalla las dimensiones del Data Frame, el numero de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las
# columnas, las 10 primeras filas y las 10 ultimas filas.

datos = pd.read_csv('./comercio_interno.csv', encoding='latin-1')
df = pd.DataFrame(datos)

# Dimensiones del Data Frame
print("Dimensiones: ", df.ndim)

# Numero de datos que contiene
print("Datos que contiene: ", df.size)

# Nombres de sus columnas y filas
print("Nombre de las columnas: ", df.keys())

# Los tipos de datos de las columnas
print("Tipo de datos de las columnas ", df.dtypes)

# Las primeras 10 filas
print("Las primeras 10 filas: \n", df.head(10))

# Las ultimas 10 filas
print("Las ultimas 10 filas \n", df.tail(10))

# b. Muestre por pantalla un grafico de los datos de empleo por provincia y su relacion con la columna valor.
print(df.filter(items=["sector_id", "sector_nombre", "valor"]))

# c. Muestre por pantalla la columna alcance_nombre ordenada alfabeticamente.
print(df.filter(items=["alcance_nombre"]).sort_values(by="alcance_nombre"))

# d. Muestre un grafico de la actividad_producto_nombre agrupados en relacion al valor
#df2 = df.filter(items=["actividad_producto_nombre", "valor"])
#df2.plot(x="actividad_producto_nombre", y="valor" , kind="bar")
#plt.show()

# e. Sume por alcance_nombre los valores de los años 2009 al 2019


# f. Muestre un grafico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019


#%%
# 6.
# La carpeta dataset contiene 3 archivos referentes a usuarios, votos y peliculas:
#   a. Genera el codigo de agrupamiento y agregacion necesario para calcular: suma, cuenta, media, desviacion estandar, utilizando las funciones numpy

datos1 = pd.read_csv('./dataset/movies.txt', sep="::", encoding='latin-1')
df1 = pd.DataFrame(datos1)

datos2 = pd.read_csv('./dataset/ratings.txt', sep="::", encoding='latin-1')
df2 = pd.DataFrame(datos2)

datos3 = pd.read_csv('./dataset/users.txt', sep="::", encoding='latin-1')
df3 = pd.DataFrame(datos3)



#%%
# 7.
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# El archivo salarios muestra distintas categorias, antiguedad, salarios, etc:
datos = pd.read_csv('./salarios.csv', encoding='latin-1')
df7 = pd.DataFrame(datos)

#   a. Calcula el minimo, maximo y promedio de antiguedad.
print("Minimo de Antiguedad: ", df7["yrs.service"].min() )

print("Maximo de Antiguedad: ", df7["yrs.service"].max() )

print("Promedio de Antiguedad ", df7["yrs.service"].mean() )

# b. Construye el codigo necesario para emitir un grafico que muestre los porcentajes de cada cargo.
new_df = df7['rank'].value_counts().rename_axis('rank').reset_index(name='counts')

your_labels = new_df['rank']
your_values = new_df['counts']

plt.pie(your_values, labels=your_labels ,autopct="%0.1f %%")
plt.show()

#plt.figure()
#plt.bar(your_labels, your_values, width=0.2)

# c. Genera el codigo de agrupamiento y agregacion necesario para calcular: suma, media y desviacion estandar, del sario, utilizando las funciones numpy
#a = df7.groupby("salary").sum()
