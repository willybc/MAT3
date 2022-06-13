# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 04:08:31 2022

@author: wilfr
"""

#%% 1.
# Solicitar al usuario que ingrese dos numeros y mostrar cual de los dos es menor.
# No considerar el caso en que ambos numeros son iguales

a = input("Ingrese primer numero \n")
b = input("Ingrese segundo numero \n")

if ( a > b ):
    print(f"primer numero es mayor : {a} > {b}")
else:
    print(f"primer numero es mayor : {b} > {a}")

#%% 2.
# Requerir al usuario que ingrese un dia de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sabado o domingo. Si el dia
# ingresado no es ninguno de esos, imprimir otro mensaje

dia = input("Ingrese un dia de la semana \n")

if ( dia == "lunes"):
    print("Es lunes! \n")
    
elif ( dia == "sabado"):
    print("Es sabado! \n")

elif ( dia == "domingo"):
    print("Es domingo! \n")

else:
    print("Otro mensaje \n")
    
#%% 3.
# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
# candidato A por el partido rojo
# candidato B por el partido verde
# candidato C por el partido azul
# Segun el candidato se le debe imprimir el mensaje "Usted ha votado por el partido {color q corresponda}
# Si el usuario ingresa una opcion que no corresponde a ninguno de los candidatos disponibles, indicar "Opcion erronea"

candidato = input("Ingrese el candidato por el que quiere votar: A, B, C \n")

a = "partido rojo"
b = "partido verde"
c = "partido azul"

if ( candidato == "A" or candidato == "a" ):
    print(f"Usted ha votado por el partido {a} \n")

elif ( candidato == "B" or candidato == "b" ):
    print(f"Usted ha votado por el partido {b} \n")
    
elif ( candidato == "C" or candidato == "c" ):
    print(f"Usted ha votado por el partido {c} \n")

else:
    print("Opcion erronea \n")

#%% 4.
# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "es vocal"
# Se debe validar que el usuario ingrese solo un caracter. Si ingresa un string de mas de un caracter, informale
# que no se puede procesar ese dato.

letra = input("Escriba una letra \n")

if ( len(letra) > 1):
    print("No se puede procesar este dato! \n")
    
elif ( letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("Es una vocal \n")

else:
    print("No es vocal :( \n")
    
#%% 5.
# Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4
# y no debe ser divisible por 100, excepto que tambien sea divisible por 400.

anio = float(input("Escriba el año \n"))

if ( anio % 4 == 0 ):
    if ( anio % 100 != 0 or anio % 400 == 0):
        print("Es bisiesto \n")
    else:
        print("No es bisiesto \n")
else:
    print("No es bisiesto \n")

#%% 6.
# Un instituto de enseñanza necesita un programa que permita, cada dia, procesar observaciones sobre las clases de ese
# dia. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un dia de la semana
# diferente:
#   . los lunes se dicta el nivel inicial
#   . los martes el nivel intermedio
#   . los miercoles el nivel avanzado
#   . los jueves son para practica
#   . los viernes para consultas

# a. Se debe comenzar por solicitar al usuario que ingrese el dia
# b. Una vez indicado el dia, el usuario necesita poder indicar si ese dia se tomaron examenes, pero solo si se
#    se trata de los niveles inicial, intermedio o avanzado, ya que las practicas y las consultas no tienen examenes
# c. Si hubo examenes, el usuario ingresara cuantos alumnos aprobaron y cuantos no, y el programa le mostrara el
#    porcentaje de aprobados.
# d. Si el dia fue el correspondiente a practica, el usuario debera ingresar el porcentaje de asistencia a clase y el
#    programa le indicara "asistio la mayoria" en caso de que la asistencia sea mayor al 50% o "no asistio la mayoria"
#    si no es asi.
# e. Si se trata de las consultas y se debera emitir "Clase de consulta" y solicitar al usuario que ingrese la
#    cantidad de alumnos de la clase y el arancel en $ por cada alumno que consulta, para luego imprimir el ingreso
#    total en $.
# Nota: Establecer los criterios necesarios, por ejemplo cantidad de alumnos por niveles

dia_actual = input("Ingrese el dia: ")

if ( dia_actual == "lunes" or dia_actual == "martes" or dia_actual == "miercoles"):
    examenes = input("Tomaron examen este dia? \n (si o no) :" )
    
    if ( examenes == "si" ):
        cant_aprobados = int(input("Ingrese cantidad de aprobados: "))
        cant_desaprobados = int(input("Ingrese cantidad de desaprobados: "))
        
        total = cant_aprobados + cant_desaprobados
        porc_aprobados = float((cant_aprobados * 100)/total)
        
        print(f"Porcentaje de aprobados: {porc_aprobados}")

elif ( dia_actual == "jueves" ):
    porc_asistencia =int(input("Ingresa el porcentaje de asistencia a clase: ") )
    
    if ( porc_asistencia > 50):
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")

elif ( dia_actual == "viernes" ):
    print("Clase de consulta")
    cant_alumnos = int(input("Ingrese cantidad de alumnos de la clase: "))
    arancel = float( input("Ingrese arancel en $ por consulta: ") )
    
    total_clase_consulta = float(cant_alumnos * arancel)
    print(f"Ingreso total: {total_clase_consulta}")

else:
    print("Error\nDebe escribir un dia del lunes al viernes.")