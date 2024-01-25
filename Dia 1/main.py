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
entradaUsuario = str(input("Ingresa tu edad: " ))
print ("Tu edad es: ", entradaUsuario)
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

    
    




## Desarrolado por ANGI ALEXANDRA ALDANA FLOREZ - 1097096369