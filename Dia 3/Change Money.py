a = int(input('Ingresa valor a pagar'))

while True:
        division = a % 10
        if (division != 0):
            k= division/5
            if (k != 0):
                p= k / 1
                print(p)

except ValueError:
    print("Por favor ingrese valores válidos.")