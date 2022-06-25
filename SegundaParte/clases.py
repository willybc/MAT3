# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:17:25 2022

@author: wilfr
"""

#%% 1.
# Define los metodos:
# a. parar, que emitira el mensaje 'ZzZzzzZZZ'
# b. marchar, que emitira el mensaje 'blablablaaaa'
# c. contar, que emitira el mensaje '1, 2, 3, 4, ...' (enteros positivos, mayores a 0, hasta el tope que le indiques)
# d. emitir, que emitira el nombre dado a la maquina y la edad en funcion de la fecha de puesta en marcha.

# El programa debera pedir al usuario:
# a. si desea crear una maquina, en el caso de que su respuesta sea afirmativa, instanciar el objeto
# b. que le de un nombre, id, fecha de puesta en marcha.
# c. que le indique si quiere que emita su nombre.
# d. que le indique si quiere que lo ponga en marcha.
# e. que le indique si quiere que lo pare.
# f. que le indique si quiere escucharlo contar pero debe decirle hasta que numero.

class Maquina:
    
    def __init__(self, nombre, id, fecha):
        self.nombre = nombre
        self.id = id
        self.fecha = fecha
        
        print()
        print("instancia.nombre(), para emitir el nombre. \n")
        print("instancia.marchar(), para poner en marcha. \n")
        print("instancia.parar(), para parar. \n")
        print("instancia.contar(int), para escuchar cantar pero debe decir hasta que numero \n")
        
    def parar(self):
        print("ZzZzzzZZZ")
    
    def marchar(self):
        print("blablablaaaa")
    
    def contar(self, cant):
        contador = 0
        while (contador < cant):
            contador += 1
            print(f"{contador}, ", end = ' ')
            
    def emitir(self):
        print(f"nombre: {self.nombre}")
    
s1 = Maquina("maquina1", 1, 13062022)
    

#%% 2.
# Crea la clase Actividad. Esta clase hereda de maquina.
# a. Define los atributos: nombre y edad
# b. Redefine el metodo emitir para que emita todos los datos.
# c. Puedes definir una o mas actividades o trabajos para la maquina?. Si es asi define al menos una.

class Actividad(Maquina):
    #maquina(nombre, id, fecha)    
    def __init__(self, nombre, id, fecha, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir(self):
        super().emitir()
        print(f"edad: {self.edad}")
        
    def saluda(self):
        print("Buenas!")
    
    def despidete(self):
        print("Chaufa!")

s2 = Actividad("maquina2", 2, 3060, 15)

#%% 3.
# Crea la clase Maquinita. Esta clase hereda de Maquina y Actividad
# a. Define los atributos: nombre y edad # segun la fecha de puesta en marcha
# b. Define los metodos avanzar y retroceder
# c. Redefine el metodo emitir para esta clase
# d. Si la edad es superior a 2 años puede tener una actividad y emitirla, en caso contrario debe emitir una
# excepcion: 'No tiene actividad, todavia esta aprendiendo!' (ver pdf errores, excepciones... ..)

class Maquinita(Actividad):
    
    def __init__(self, nombre, id, fecha, edad):
        self.nombre = nombre
        self.edad = edad
        self.fecha = fecha
        
        if self.edad > 2:
            print("puede tener actividad")
            self.emitir()
        else:
            raise Exception ("No tiene actividad, todavia esta aprendiendo!")
    
    def avanzar(self):
        print("Ejecutando metodo avanzar")
    
    def retroceder(self):
        print("Ejecutando metodo retroceder")
    
    def emitir(self):
        super().emitir()
        print(f"fecha: {self.fecha}")
        
        
s3 = Maquinita("maquina3", 3, 3060, 2)        
        

#%% 4.
# Crear la clase Superheroe
# a. El constructor debe recibir, nombre edad, estado (sin poder, con poder, representado por True o False ) y una
# cantidad (numero) maxima de poder

# b. Metodo usar_poder, donde se ira restando el poder utilizado cuando trabaje de superheroe,
# si se intenta usar mas de lo que tiene como poder, debe emitir una excepcion que diga 'Me quede sin poder!!' buahhh

# c. Cuando el poder se agote debes revivir al superheroe.

# d. Metodo tener_poder, donde recibira un valor que determinara la cantidad de poder a reutilizar,
# si supera la cantidad maxima del atributo debe emitir una excepcion que diga 'Desbordamiento de poder!!',
# este desbordamiento se penalizara y la diferencia se restara  al maximo permitido.

# e. Metodo revivir, reinicia al superheroe con poder necesario para pedir tener_poder.

# f. Metodo volar, para activarlo debe tener al menos el 20% de poder y cada minuto que vuele, le resta 2% de poder.

# g. Metodo perforar, para activarlo debe tener al menos el 20% de poder y cada minuto que perfore, la resta 5% de poder.

class Superheroe:
    
    def __init__(self, nombre, edad, estado, cantMaxPoder):
        self.nombre = int(nombre)
        self.edad = int(edad)
        self.estado = bool(estado)
        
        self.cantMaxPoder = int(cantMaxPoder)
        self.poder = int(cantMaxPoder)
        
    def usar_poder(self, cant):
        if self.poder >= cant:
            self.poder -= cant
            
            if self.poder == 0:
                self.estado = False
            
        else:
            self.estado = False
            raise Exception ("Me quede sin poder!!, buahhh")
    
    def estado (self):
        if self.poder < 0:
             return False
    
    #Cuando el poder se agote, se puede revivir con metodo revivir()
    def revivir(self):
        #Reinicia al heroe con poder necesario para pedir tener_poder
        self.poder += 1
        self.estado = True
       
    def volar(self, minutos):
        descuento = 0
        if (self.cantMaxPoder > self.cantMaxPoder * 0.2 ):
            descuento = minutos * 2 
            self.poder -= ( ( self.poder * descuento ) / 100 )
            
    def perforar(self, minutos):
        descuento = 0
        if (self.cantMaxPoder> self.cantMaxPoder * 0.2):
            descuento = minutos * 5
            self.poder -= ( ( self.poder * descuento ) / 100 )
        
    def tener_poder(self, valor):
        if valor > self.cantMaxPoder:
            #Penalizacion: Diferencia se restara al maximo permitido
            self.cantMaxPoder -= valor
            raise Exception ("Desbordamiento de poder!!")
        else:
            self.poder += valor
    
#%% 5
# Crear la clase Mate que describa el funcionamiento de la bebida
# a. El constructor debe recibir como parametro n, la cantidad maxima de cebadas en base a la cantidad de 
# yerba vertida en el recipiente que tambien debe ser un parametro.

# b. Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un numero).

# c. Un atributo para el estado (lleno o vacio).

# d. Un metodo cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepcion
# que imprima el mensaje: Uhh! Te quemaste!

# e. Un metodo beber, que vacia el mate y le resta una cebada disponible.
# Si se intenta beber un mate vacio se debe lanzar una excepcion que imprima el mensaje: El mate esta vacio! ...

class Mate:
    
    def __init__(self, n, cantMaximaCebadas, cantidadYerba):
        self.cantMaximaCebadas = cantMaximaCebadas
        self.cantidadYerba = cantidadYerba
        
        #Atributo para cantidad de cebadas restantes hasta que se lave el mate
        self.cantidadCebadas = n
        
        #Atributo estado lleno(True) or vacio(False)
        self.estado = False
        
        def cebar(self):
            #si se intenta cebar con el mate lleno, se debe lanzar una excepcion
            if(self.estado == True):
                raise Exception("Uhh! Te quemaste!")
            else:
                #llena el mate con agua
                self.estado = True
            
        def beber(self):
            #si se intenta beber un mate vacio se debe lanzar una excepcion
            if(self.estado == False):
                raise Exception("El mate esta vacio!")
            else:
                #vacia el mate y le resta una cebada disponible
                self.estado = False
                self.cantidadCebada -= 1
            
#Nota: 
    #No se usa cantMaximaCebadas para nada
    #n que es?, no se especifica. Por lo tanto interpreto que es cantidadCebadas       
        
