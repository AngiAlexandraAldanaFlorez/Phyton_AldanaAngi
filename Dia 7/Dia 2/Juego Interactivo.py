NumeroSecreto = 42
NumeroSecreto == 42
a=int

for i in range(1,11,1):
    while a != NumeroSecreto:
        for j in range(1,11,1):
            a = int(input('Ingresa un numero, intento #'))
            if j == 10:
                print('Han acabado tus intentos')
                break
            else: 
                a == NumeroSecreto
                print ('¡Adivinaste!')
            print("Intento # ", j)
            if NumeroSecreto > a:
                print ('Numero es mayor que el numero que ingresaste')
            elif NumeroSecreto < a:
                print ('Numero es menor que el numero que ingresaste')
            
            

    

    



        
