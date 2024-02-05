## -------------------------------
## ---- Ejercicio 1 ----
## -------------------------------

# ---- Funciones ----
# función sin parámetros ni retorno de valor 
def bienvenido():
    print("¡Bienvenido!")

# función con parámetro sin retorno 
def bienvenidoConNombre(name):
    print("Bienvenido " + name + "!")

# función con parámetros y con retorno
def multiplica(val1, val2): 
    return val1 * val2

# función sin parámetro
def saludos():
    print("Hola, ¿cómo estás hoy?")

if __name__ == "_main_":
    print("Hola Mundo")

    # ---- Datos Primitivos ----
    # ... (código anterior)

    # ---- Entradas parte del usuario con definición de tipo dato primitivo----
    entradaUsuario = str(input("Ingresa tu edad: "))
    print("Tu edad es: ", entradaUsuario)

    # ---- Ciclos ----
    ## Ciclo for
    for i in range(5, 10, 2):
        print(i)
    
    # Ciclo while
    booleanito = True
    while booleanito == True:
        print("sigo vivo")
        booleanito = False

    # ---- Condiciones ----
    texto1 = "campus"
    if texto1 == "campus":
        print("soy campus")
    else:
        print("No soy campus")

    # ---- Llamadas a funciones ----
    name = input("Ingresa tu nombre: ")
    bienvenidoConNombre(name)

## Desarrolado por ANGI ALEXANDRA ALDANA FLOREZ - 1097096369