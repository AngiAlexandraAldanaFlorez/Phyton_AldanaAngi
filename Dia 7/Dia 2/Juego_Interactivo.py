def JuegoAdivinaNumero():
    NumeroSecreto = 42
    intentos=0

    while intentos < 10:
        intentos += 1
        a = int(input(f'Ingresa un numero, intento #{intentos}:'))
                
        if NumeroSecreto > a:
            print ('El Numero es mayor que el numero que ingresaste')
        elif NumeroSecreto < a:
            print ('El Numero es menor que el numero que ingresaste')
        else: 
            a == NumeroSecreto
            print(f'¡Adivinaste! El número secreto era {NumeroSecreto}.')
            print(f'Número de intentos: {intentos}')
    else:
        print(f'Has agotado tus 10 intentos. El número secreto era {NumeroSecreto}.')
        
JuegoAdivinaNumero()


            
            

    

    



        
