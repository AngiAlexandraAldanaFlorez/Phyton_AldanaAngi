t = int(input(""))
list=[]
for p in range (--t):
    print(list)

    n,k= int(input(" "))
    print(n, k)
    
    for _ in range(t):
        def calcular_probabilidad(n, k):
            nk_input = input("Ingrese dos números separados por un espacio (n k): ")
        n, k = map(int, nk_input.split())

        resultado = calcular_probabilidad(n, k)

        print(f"{_ + 1}: {resultado}", end=" ")

        x= input("")
        a=[*x]
        print(a)
        for i in range(5):
            numero=int(a[i])
            a[i]=numero
        print(a)



