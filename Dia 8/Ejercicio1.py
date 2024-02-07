import json

P=open('data.json')
miJson=json.load(P)
print(miJson)

#1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar 
#ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.

x=str(input('ingrese'))
miJson['nombre']=x
print(miJson)