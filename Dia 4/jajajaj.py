from itertools import permutations

def calcular_probabilidad(n, k):
    numeros = list(range(1, n+1))
    parejas = list(permutations(numeros, 2))

    count_divisibles = 0

    for pareja in parejas:
        suma = sum(pareja)
        if suma % k == 0:
            count_divisibles += 1

    return count_divisibles

def main():
    t = int(input("Ingrese el número de casos a repetir (t): "))
    
    for _ in range(t):
        nk_input = input("Ingrese dos números separados por un espacio (n k): ")
        n, k = map(int, nk_input.split())

        resultado = calcular_probabilidad(n, k)

        print(f"{_ + 1}: {resultado}", end=" ")

if __name__ == "__main__":
    main()