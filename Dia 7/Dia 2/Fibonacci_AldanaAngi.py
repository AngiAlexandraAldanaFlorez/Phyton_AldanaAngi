##  ---- fibonacci ----
print('Bienvenido')
print('''¿Que es la sucesion Fibonacci? Esta serie numérica empieza con 0 y 1, siguiendo con la 
      suma de los dos números anteriores hasta el infinito: 1, 1, 2, 3, 5, 8...''')
print('----------------------------------------------------------------------------------------')
n= int(input('''A continuacion, Ingrese un numero el cual representara hasta qué término
             se generará la secuencia Fibonacci   '''))

a=0
b=1
for i in range(n):
        print(a)
        c = a+b
        a = b
        b = c
        
print('A finalizado la secuencia')

P= str(input('''¿El usuario desea continuar? Si desea continuar escriba numero uno (1) 
             de lo contrario escriba numero cero (0) '''))

while P =="1": 
        n= int(input('Escribe numero '))
        a=0
        b=1
        for i in range(n):
            print(a)
            c = a+b
            a = b
            b = c
        P= str(input('''¿El usuario desea continuar? Si desea continuar escriba numero uno (1)
                  de lo contrario escriba numero cero (0) '''))
if P=="0":
        print('A finalizado la secuencia')