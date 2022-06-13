# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% 4
# Que resultados se obtendran al evaluar las siguientes expresiones
from math import *

print( int (exp( 2 * log (3) ) ))
print( round( 4*sin(3 * pi) / 2 ))
print( abs(log10(.01) * sqrt(25) ))
print(round(3.21123 * log10(1000), 3))

#%% 5
# Desarrola un programa que permita leer 2 valores y que emita por pantalla lo siguiente
# Suma, resta, producto, division, resto, promedio y el doble producto del primero menos la mitad del segundo

a = float(input("Escriba primer valor \n"))
b = float(input("Escriba segundo valor \n"))

suma = a+b
resta = a-b
producto = a*b
division = a/b
resto = a%b
promedio = (a+b)/2
extra = (a*2)-(b/2)

print(f"\nSuma: {suma} \nResta: {resta} \nProducto: {producto}\nDivision: {division} \nResto: {resto} \nPromedio: {promedio} \nExtra: {extra}\n")

#%% 6
# Dada una cierta cantidad de galones, los convierta a litros y dada una medida en millas las convierta a metros,
# ambos con entrada de tipo flotante

cant_galones = int( input("Escriba cantidad de galones \n") )

cant_millas = float( input("Escriba una medida en millas \n") )

conv_galones_a_litros = float( (cant_galones * 3.78541)/1 )

conv_millas_a_metros = (cant_millas * 1609.34)/1

print(f"{cant_galones} galones equivale a {conv_galones_a_litros} litros")
print(f"{cant_millas} millas equivale a {conv_millas_a_metros} metros")

#%% 7
# Dada una cantidad de segundos los convierta en horas, minutos y segundos.

cant_segundos = int( input("Escribe x segundos \n") )

conv_horas = int(cant_segundos/3600)
conv_minutos = int( (cant_segundos%3600)/60)
conv_segundos= int( ((cant_segundos%3600)%60))

print(f"Horas {conv_horas}, minutos {conv_minutos} y segundos {conv_segundos} \n")

#%% 8
# Pedir al usuario su peso(en kg) y estatura(en metros)
# Calcular el indice de masa corporal, lo almacene en una variable, y muestre por pantalla redondeado con dos decimales

peso = int(input("Escriba peso en kilos \n"))
estatura = float(input("Escriba estatura en metros \n"))

masa_corporal = float ( peso / (estatura ** 2) )
masa_redondeada = round(masa_corporal,2)

print(f"\nMasa corpotal : {masa_redondeada} \n")

#%% 9
# Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Suele hacer por correo y la empresa
# de logistica les cobra por peso de cada paquete asi que deben calcular el peso de los payasos y muñecas que saldran
# en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g.
# Escribe un programa que lea el numero de payasos y muñecas vendidos en el ultimo pedido y calcule el peso total
# del paquete que sera enviado

num_payasos = int(input("Escribe la cantidad de payasos \n"))
num_munecas = int(input("Escribe la cantidad de muñecas \n"))

peso_payaso = 112
peso_muneca = 75

peso_total_payaso = num_payasos * peso_payaso
peso_total_muneca = num_munecas * peso_muneca

peso_total = peso_total_payaso + peso_total_muneca

print(f"Peso total: {peso_total} \n")

#%% 10
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interes al año. Estos ahorros no se
# cobran hasta finales de año y se te suman al balance final de tu cuenta de ahorros. Escribe un programa que 
# comience leyendo la cantidad de dinero depositada en la cuenta de ahorros. El programa debe calcular y mostrar
# por pantalla la cantidad de ahorros tras el primer, segundo y tercer año. Redondea cada cantidad a dos decimales

cant_dinero_depositada = float(input("Escriba la cantidad de dinero depositada \n") ) 
1
primero = round((cant_dinero_depositada*4)/100 + cant_dinero_depositada, 2)
segundo = round((primero*4)/100 + primero, 2) 
tercer = round((segundo*4 )/100 + segundo, 2)

print(f" primer: {primer} \n segundo: {segundo} \n tercer: {tercer} \n")