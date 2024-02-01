#Creación de Diccionario - {llave1:valor1,llave2:valor2}
diccionario = {'Nombre':("Danna","Mozo","Andres"),"Edad":17,"Barrio":"Zapamanga"}
print(diccionario)
print(type(diccionario))

#Buscar valor de x llave del diccionario y buscar 
#el segundo dato que contiene la subdiccionario
print(diccionario['Nombre'][1])
diccionario['Nombre']="Danna"
print(diccionario)
print(type(diccionario))
print(diccionario['Nombre'])

#Recorrer un Diccionario por llaves
for i in diccionario:
    print(i)

#Recorrer un Diccionario por valor 
for valor in diccionario:
    print(diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in diccionario.items():
    print(llave,valor)

#Limpiar un diccionario
print("############################")
#diccionario.clear() ---- OJOOOOOOOOO , RECUERDA QUE ESTO LIMPIA EL DICCIONARIO
print(diccionario)

#Guardar las llaves de un diccionario en una lista
listaLlaves= diccionario.keys()
print(listaLlaves)

#Guardar los valores de un diccionario en una lista
listaValores= diccionario.values()
print(listaValores)

#Eliminar una llave de un diccionario
diccionario.pop("Nombre")
print(diccionario)

#Eliminar un elemento del diccionario de manera aleatoria
#diccionario.popitem()
print(diccionario)

#Cruzar un diccionario a con uno b
diccionario2= {'Edad': 23, 'Barrio': 'Ruitoque'}
diccionario.update(diccionario2)
print(diccionario)