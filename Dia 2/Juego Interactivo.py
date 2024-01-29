NumeroSecreto = 42
NumeroSecreto == 42
a=int

for i in range(1,11,1):
    while a != NumeroSecreto:
        for j in range(1,11,1):
            print (j)
        a= (input('Ingresa un numero, intento #',j+0))
        if NumeroSecreto > a:
                    print ('Numero es mayor que el numero que ingresaste')
        if NumeroSecreto < a:
                    print ('Numero es menor que el numero que ingresaste')
        if i == 10:
                    print('Han acabado tus intentos')
        if a == NumeroSecreto:
                    print ('¡Adivinaste!')

    

    



        
