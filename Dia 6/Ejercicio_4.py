## posiscion de la bola en el espacio y el tamaño
## x y 
## calcular tamaño si se conoce el radio
## repreentacionde bola en el espacio 2d como una tupla (x,y,r)
## so bolas chocan si la distancia es menor o igual a la suma de sus radios, 
## d=ditancia entres sus cen
import math
Bola1=int
Bola2=int

#ingresar posicion Bola1
print('A continuacion ingrese la posicion de la Bola 1 en el plano cartesiano')
print(' ')
x1=float(input('X= '))
y1=float(input('Y= '))

print('A continuacion ingrese la posicion de la Bola 2 en el plano cartesiano')
print(' ')
x2=float(input('X= '))
y2=float(input('Y= '))

radio1=float(input('Radio de Bola 1= '))
radio2=float(input('Radio de Bola 2= '))
area1=3.14*radio1*radio1
area2=3.14*radio2*radio2
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
Suma_radio=radio1+radio2

if distancia <= Suma_radio:
    print("TRUE")
else:
    print("FALSE")




