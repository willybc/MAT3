# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:46:30 2022

@author: wilfr
"""

import re

texto = 'hola h0la Hola mola m0la M0la'
patrones= [ '[A-Z][A-z0-9]{3}' ]

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))
        
#%%

texto="""El poder de las expresiones regulares se manifiesta cuando agregamos caracteres
especiales a la cadena de búsqueda que nos permite controlar de manera más precisa
qué líneas coinciden con la cadena. Agregar estos caracteres especiales a nuestra
expresión regular nos permitirá buscar coincidencias y extraer datos usando unas
pocas líneas de código."""

a_buscar = "est"

x = re.finditer(a_buscar,texto)

for i in x:
    print(i.span())
    
#%%
texto="""Las expresiones regulares casi son un lenguaje de
programación para buscar y analizar cadenas."""
'''
patron para dividir donde no encuentre un caracter alfanumerico
'''

patron = re.compile(r'\W+')
palabras = patron.split(texto)

palabras[:8]

#%%
#Validar mails
import re

mails ="""aaa.bbbbbb@gmail.com, Pepe Pepitito,
ccc.dddddd@yahoo.com.ar, qué lindo día , eeeee@github.io,
https://pypi.org/project/regex/, https://ffffff.github.io,
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
"""

#VERBOSE re.X
mail = re.compile(r"""
                  \b
                  [\w.%+-]
                  +@
                  [\w.-]
                  +\.
                  [a-zA-Z]{2,6}
                  \b
                  """, re.X)

print(mail.findall(mails))

#%%
#Validar una URL
import re
url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
print(url.search("https://www.python.org/"))

print(url.search("https://www.google.com/!.html"))

#%%
#Validar una direccion IP
import re
patron=(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
ip = re.compile(patron)
print(ip.search("98.61.125.138"))
print(ip.search("256.60.124.136"))

#%%
#Validar una fecha
import re
fecha=re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')
print(fecha.search("2/10/1990"))
print(fecha.search("2-10-1990"))
print(fecha.search("32/12/2021"))
print(fecha.search("30/13/2020"))

#%%
# Practica de expresiones regulares
import re

#2. Dado el siguiente codigo
#Encuentra la expresion para que se emita ['bat', 'bot']
string = 'bat, lat, mat, bet, let, met, bit, lit, mit , bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

#3. Dado el siguiente texto
texto3 = """Maria tiene 5 años, y su hermana Valeria tiene 2.
Rita y Pedro, sus primos, tienen 3."""
#Encuentra al expresion regular que extraiga y emita solo los nombres
result3 = re.findall('[A-Z]{1}[a-z]{2,9}', texto3)
print(result3)

#4. Dado el sigueinte texto
texto2 = """Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 763-9376 | 4322 North Quad """
#Encuentra la expresion para que se mita: ['(734) 647-6333], '(734) 647-8044', '(734) 763-2285', '(734) 647-3576', '(734) 763-1251', '(734) 764-9376']

result4 = re.findall(r'\W{1}\d{3}\W{2}\d{3}-\d{4}', texto2)
print(result4)

#%%
#5. Dado el archivo pedidos.txt. Escribe un nuevo archivo 'pedidos_agrupados.txt', en el que los datos se reagrupen de la siguiente manera:


#%%
#6. Dado dos archivos de provincias.txt, que contiene un listado de las provincias de la republica Argentina y localidades.txt, que contiene un listado de
# todas las localidades de la RA con su correspondiente codigo postal

#En relacion al ejemplo dado responder:
# a. Existe la posibilidad de encontrar todos los codigos postales que le corresponden a cada provincia utilizando expresiones regulares?
# b. En el caso de respuesta afirmativa al punto anterior: La misma expresion regular del ejemplo dado es util? O hay que cambiarla?

# Al construir el programa hay que tener en cuenta que lo que une a cada provincia con sus ciudades y pueblos es el id. Se facilitan dos
# archivos en formato csv y dos en formato .txt. Si desea utilizarlos como csv, en Python se debe incluir: import cvs


#%%
# Ejercicio de 2do Parcial Simulacro
# Las siguientes lineas de texto fueron extraidas de un archivo con muchas entradas,
# representan: ip, usuario, fecha y hora y peticion. Encuentra la expresion regular
# para extraer y emitir la cadena " ". Desarrola el codigo correspondiente.

import re
texto = """
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""

patron = r'[A-Z]{1,}\s\/*.*\d\.\d'

x = re.findall(patron, texto)
print(x)

#%%
# Ejercicio 2Do Parcial 2021

texto = """ 
1,Ciudad Autonoma de Buenos Aires (CABA), ARC-C
2,Buenos Aires,AR-B
3,Catamarca,AR-K
4,Cordoba,AR-X
5,Corrientes,AR-W
6,Entre Rios,AR-E
7,Jujuy,AR-Y 
"""

#Construir el programa para hallar la expresion regular para extraer en una lista las provincias o ciudad (CABA) y la ultima letra de la cadena, sin el guion
# Ej: [Ciudad Autonoma de Buenos Aires (CABA),C,Buenos aires,B, ....]
patron = r"([A-z]{1,}/*.*\,)\s\w\w\w\-"
x = re.findall(patron, texto)
print(x)



















