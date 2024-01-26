## -------------------------------
## ---- Ejercicio 1 ----
## -------------------------------

# Impresion en consola
print ("Hola Mundo")

# ---- Datos Primitivos ----
#1. String
texto = "campus"
print(texto)
print(type(texto))
#2. Int
numeroEntero = 1
print(numeroEntero)
#3. Float
numeroDecimal = 3.1
print(numeroDecimal)
#4. Double
numeroDecimalLargo = 3.14534354453243
print(numeroDecimalLargo)
#5- Boolean
booleano= True
print(booleano)
# ---- Entradas parte del usuario con definición de tipo dato primitivo----
entradaUsuario = str(input("Ingresa tu edad: "))
print ("Tu edad es: ",entradaUsuario)
# ---- Ciclos ----
##Ciclo for
for i  in range (5,10,2):#for contador in range (desde,hasta,pasos): 
    print (i)
#Ciclo while
booleanito = True
while booleanito ==True:#while condicion_a_cumplir :
    print("sigo vivo")
    booleanito = False
# ---- Condiciones ----
texto1 = "campus"
if texto1 == "campus":
    print ("soy campus")
else:
    print ("No soy campus")

# ---- Funciones ----
# funcion sin parametros ni retorno de valor 
def diBienvenido():
    print("¡Bienvenido!")

diBienvenido()


# funcion con parametro sin retorno 
def bienvenidoConNombre(name):
    print("Bienvenido "+ name + "!")

name = input("ingresa tu nombre: ")
    
bienvenidoConNombre(name)
    
# funcion con parametros y con retorno
def multiplica(val1, val2): 
    return val1 * val2
result= multiplica(5,4)
print('multiplicacion = ',result)
    
# funcion sin parametro
def saludos():
    return "Hola, ¿como estas hoy?"
    
print(saludos())
 
# ---- Arreglos----
mascotas = ["perro", "gato", "pato", "conejo"]

print (mascotas[0])
print (mascotas[1])
print (mascotas[2])
print (mascotas[3])



## Desarrolado por ANGI ALEXANDRA ALDANA FLOREZ - 1097096369