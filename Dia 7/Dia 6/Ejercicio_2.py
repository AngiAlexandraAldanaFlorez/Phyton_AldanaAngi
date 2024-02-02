def negate(num):
    num_Negativo = num*-1
    return num_Negativo
num=int(input(' '))
resulta_negativo=negate(num)
print(resulta_negativo)
if num>10000:
    print('True')
else:
    print('False')


#Bugs:
##1. En el print no puso parentesis a los datos
#por lo cual no se van a imprimir
    
##2. No tiene condicionales para que nos de como resultado True or False

##3. No escribe el proceso de convertir el numero positivo a negativo