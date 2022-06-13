# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:31:54 2022

@author: wilfr
"""

#%% 1
# Escribe un programa que pida la cantidad de numeros positivos que se tienen que ingresar y a continuacion
# pida numeros hasta que se hayan ingresado la cantidad de numeros indicada.

n = int(input(f"Escriba la cantidad de numeros positivos que se tienen que ingresar: "))
i = 1

while i <= n:
    input(f'Escriba numero {i} ')
    i += 1

print("Programa terminado")

#%% 2
# Escribe un programa que pida dos numeros enteros. El programa pedira de nuevo el segundo numero mientras
# no sea mayor que el primero. El programa termina y emitira los numeros.

a = int(input(f"Escriba el primer numero entero: "))
b = int(input(f"Escriba el segundo numero entero: "))

while b > a:
    b = int(input(f"Escriba el segundo numero entero: "))

print(a)
print(b)

#%% 3
# Escribe un programa que pida numeros decimales mientras el usuario escriba numeros mayores que el primero.

a = int(input(f"Escriba numero decimales: "))
b=99999999999

while b > a:
    b = int(input(f"Escriba otro numero decimal"))
    
print(a)
print(b)

#%% 4
# Escribe un programa que pida numeros enteros mientras el usuario ingresa numeros cada vez mas grandes,
# el programa emite en cada iteracion el numero anterior ingresado y finaliza ingresando un numero menor

anterior = int(input(f"Escriba numero decimales: "))
nuevo = int(input(f"Escriba otro numero decimal: "))

while nuevo > anterior:
    
    anterior = nuevo
    print(f"anterior = {anterior}")
    nuevo = int(input(f"Escriba otro numero decimal: "))
    
#%% 5
# Escribe un programa que pida numeros mientras no se escriba un numero negativo. El programa terminara
# emitiendo la suma de los numeros ingresados

a = int(input(f"Escriba numero decimales: "))
acumulador = 0

while a > 0:
    acumulador += a
    a = int(input(f"Escriba numero decimales: "))
    
print(f"acumulador = {acumulador}")

#%% 6
# Escribe un programa que pida un valor limite positivo y a continuacion pida numeros hasta que la suma
# de los numeros introducidos supere el limite inicial.

limite = int(input(f"Escriba un valor de limite positivo: "))
suma = 0

while suma < limite:
    a = int(input(f"Escriba numero: "))
    suma += a

print(limite)
print(suma)

#%% 7
# Escribe un programa que pida primero dos numeros enteros (minimo y maximo) y que despues pida numeros
# enteros situados entre ellos. El programa terminara cuando se escriba un numero que no este comprometido
# entre los dos valores iniciales y emitira la cantidad de numeros ingresados.

minimo = int(input(f"Escriba el minimo: "))
maximo = int(input(f"Escriba el maximo: "))
cont = 0

num = int(input(f"Escriba numero: "))

while minimo<num and maximo>num:
    num = int(input(f"Escriba numero: "))
    cont+=1

print(f"contador = {cont}")

#%% 8
# Escribe un programa que pida numeros pares mientras el usuario indique que quiere seguir introduciendo numeros.
# Para indicar que quiere seguir escribiendo numeros, el usuario debera contestar 'S' o 's' a la pregunta

loop=1
# 1 encendido
# 0 apagado

num=1
while loop == 1:
    
    while (num % 2 != 0):
        num = int(input(f"Escriba un numero par: "))
        
    respuesta = input(f"Quiere seguir introduciendo numeros? Escriba 's' o 'S' para continuar: ")
    
    if(respuesta == 's' or respuesta == 'S' ):
        pass
    else:
        loop = 0
    
    num=1