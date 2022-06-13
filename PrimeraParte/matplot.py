# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:03:55 2022

@author: wilfr
"""

#%% 1
# Dado el siguiente problema con su programacion en Python. Genera los graficos con Diagramas de Venn que representen las respuestas de los encuestados.
# Investiga si puedes utilizar subplots para representar todas las operaciones:
    
    # Un grupo de jovenes fue entrevistado para conocer sus preferencias de los siguientes medios de transporte
    # moto, auto y bicicleta
    # Los datos de la encuesta fueron los siguientes:
    
    #1. 5 jovenes prefieren solamente la moto
    #2. 38 jovenes prefieren la moto
    #3. A 9 jovenes no les gusta el automovil como medio de transporte
    #4. 3 jovenes prefieren la moto y la bicicleta, pero no el auto
    #5. 20 prefieren la moto y el auto, pero no la bicicleta
    #6. A 72 no les gusta la bicicleta como medio de transporte
    #7. Un solo joven, no prefiere ninguno de estos tres medios de transporte
    #8. A 61 no les gusta la moto como medio de transporte

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles,venn2

M = { 5, 20, 3, 10 }
A = { 46, 20, 10, 14}
B = { 0, 3, 10, 14 }
U = { 1 }

def conjuntoSolo(a,b,c):
    return  a-b & a-c

#1. 5 jovenes prefieren solamente la moto
def punto1():
    return M-A & M-B
    
#2. 38 jovenes prefieren la moto
def punto2():
    suma = 0
    for elemento in M:
        suma += elemento
        
    return suma

#3. A 9 jovenes no les gusta el automovil como medio de transporte
def punto3():
    punto3 = (M-A) | (B-A)
    suma = 0
    for elemento in punto3:
        suma += elemento
    
    return punto3

#4. 3 jovenes prefieren la moto y la bicicleta, pero no el auto
punto4 = M&B - A

#5. 20 prefieren la moto y el auto, pero no la bicicleta
punto5 = (M&A) - B 

#6. A 72 no les gusta la bicicleta como medio de transporte
def punto6():
    punto6 = (M-B) | (A-B)
    suma = 0
    for elemento in punto6:
        suma += elemento
    
    return punto6

#7. Un solo joven, no prefiere ninguno de estos tres medios de transporte
punto7 = U

#8. A 61 no les gusta la moto como medio de transporte
punto8 = (B-M) | (A-M)

plt.figure('Ejercicio 1')

#Dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=("A", "M", "B", "U"))

# establecemos el tamaño de la fuente
for subset in ("001", "010", "011", "100", "101", "110", "111"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('010').set_text(punto1())
diagram.get_label_by_id('011').set_text(punto4)
diagram.get_label_by_id('110').set_text(punto5)
diagram.get_label_by_id('001').set_text(conjuntoSolo(B,A,M))

diagram.get_label_by_id('100').set_text(conjuntoSolo(A,M,B))

diagram.get_label_by_id('101').set_text( (A & B) -M)
diagram.get_label_by_id('111').set_text((M & A) & B )
#diagram.get_label_by_id('1000').set_text(punto8)

# marcamos los contronos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# recuadro
plt.axis('on')
plt.show()

#Muestro los conjuntos
print(f"Los conjuntos son : \nM={M}, A={A}, B={B} y U={U} \n")

#Funcion in
print("Funcion in. Busco si 5 esta en el conjunto M: ")
print(5 in M, end=" \n\n")

#Funcion len
print("Funcion len. Muestro el modulo de A: ")
print(len(A), end=" \n\n")

#Funcion not
print("Funcion not. Muestro si 10 no esta en B: ")
print(10 not in B, end= "\n\n")

#Funcion add
print("Funcion add. Añado un elemento al conjunto U: ")
print(U.add('x'), end=" \n\n")

#Funcion remove
print("Funcion remove. Elimino un elemento al conjunto U: ")
print(U.remove('x'), end=" \n\n")

#Funcion intersection
print("Funcion intersection. Muestro la interseccion entre B y A: ")
print(B&A, end=" \n\n")

#Funcion union
print("Funcion union. Muestro la union entre M y A: ")
print(M|A, end=" \n\n")

#Funcion diferencia -
print("Funcion diferencia. Aplico la funcion diferencia entre A y B: ")
print(A-B, end=" \n\n")

#Funcion ^
print("Funcion issubset. Muestro si M es un subconjunto de A: ")
print(A^B, end= " \n\n")

#Funcion issubset
print("Funcion issubset. Muestro si M es un subconjunto de A: ")
print(M.issubset(A), end=" \n\n")

#%% 2.
# En una escuela de 600 alumnos, 100 no estudian ningun idioma extranjero, 450 estudian frances y 50 estudian frances e ingles
# Cuantos estudian solo ingles?
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles,venn2

plt.figure('Ejercicio 2')

ninguno = { 100 }
ingles = { 50 }
frances = {400, 50 }

#Dibujamos los diagramas
diagram = venn3(subsets = (400, 50, 50, 100, 0, 0, 0), set_labels = ('Frances', 'Ingles', 'No estudian'), alpha = 0.5);

diagram.get_label_by_id("100").set_text(frances-ingles)
diagram.get_label_by_id("110").set_text(ingles&frances)
diagram.get_label_by_id("010").set_text(ingles)
diagram.get_label_by_id("001").set_text(ninguno)
# recuadro
plt.axis('on')
plt.show()

#%% 3.
# En una escuela de 500 estudiantes, hay 125 estudiantes inscritos en Algebra II, 275 estudiantes que practican deportes y
# 52 estudiantes que estan inscritos en Algebra II y practican deportes.
# Crea un diagrama de Venn para ilustrar esta informacion.
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles,venn2

U = { 500 }
A = { 52, 73 }
D = { 52, 223 }

diagram = venn3(subsets = (125, 275, 52, 0, 0, 0, 0), set_labels = ("Algebra II", "Deportes") )

diagram.get_label_by_id("100").set_text(A-D)
diagram.get_label_by_id("110").set_text(A & D)
diagram.get_label_by_id("010").set_text(D-A)

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {U}",
         size=10)

plt.axis('on')  # Recuadro
plt.title("Estudiantes")
plt.show()

# Solucion:
# Primero, establezcamos que el conjunto representa los estudiantes inscritos en Algebra II y el conjunto representa los
# estudiantes que practican deportes. Generalmente hablando, es mas facil empezar en el centro o en la interseccion del
# diagrama de Venn. Una vez que ubicamos 52 en la interseccion, podemos restarlo al numero total de estudiantes que practican
# deporte al numero total de estudiantes inscritos en Algebra II para determinar cuantos solo hacen una actividad o la otra.
# Finalmente, podemos restar este total a 500 para encontrar cuantos estan completamente fuera de los circulos

#Tambien existen simbolos que pueden utilizarse para describir el numero de elementos en cada region del diagrama

#%% 4.
# Que funciones de Python, dadas en el ejercicio1, puedes representar con la simbologia dada en la imagen del ejercicio 3?


#%% 5.
# Crea un diagrama de Venn para ilustrar la informacion siguiente acerca de los subconjuntos M y N en el universo U:
    
#n(M) = 89; n(N) = 103; n(M U N) = 130; n(U) - 178
M = { 89 }
N = { 103 }


# Solucion: De nuevo, comenzamos en el medio de la interseccion. Debemos determinar cuantos elementos hay en la
# interseccion. Consideremos que cuando agregamos elementos M a los elementos en N, agregamos los elementos de la 
# interseccion 2 veces. Esto sucede porque se cuentan en el conjunto M y tambien en N. Observaste que:
# n(M) + n(N) = 89 + 103 = 192
# mientras el:
# n(M U N) = 130
# Hemos contado 2 veces los 62 (192-130) elementos en M interseccion N.
# Ahora podemos poner este numero en el diagrama y resolver como en el ejemplo anterior.
# En general, para los dos conjuntos, M y N, podemos usar la formula:
#

#%% 6