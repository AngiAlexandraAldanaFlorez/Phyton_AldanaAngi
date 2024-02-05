import main
main.bienvenido()

import main
name=str(input('ingrese su nombre '))
main.bienvenidoConNombre(name)

from main import multiplica
resultado = multiplica(3, 4)
print(resultado)

from main import saludos
mensaje = saludos()
print(mensaje)
