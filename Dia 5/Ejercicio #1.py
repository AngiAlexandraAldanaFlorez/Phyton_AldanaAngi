T= int(input())
for case in range(T):
    texto=input("")
    numeros=input("")
    n=0
    k=0
    T_n=list()
    textoLista = texto.split('')
    numerosLista= numeros.split('')
    n=int(textoLista[0])
    k=int(textoLista[1])
    for p in range(n):
        numerito = int(numerosLista[p])
