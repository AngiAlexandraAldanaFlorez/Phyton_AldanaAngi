import json

P=open('Dia 8/data.json')
miJson=json.load(P)
ventas = miJson.get('ventas')
pedidos = ventas.get('pedidos')

#1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar 
#ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.

#print(miJson["ventas"]["pedidos"][0]["fecha"])


ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)

for i in ordenados:
    print(i)

#2.Devuelve todos los datos de los dos pedidos de mayor valor.
print('------------------------------------------')
ordenados1 = sorted(pedidos, key=lambda x: x["total"], reverse=True)
print(ordenados1[0])
print(ordenados1[1])

#3. Devuelve un listado con los identificadores de los clientes que han realizado 
#algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.

lista=[]
for i in miJson['ventas']['pedidos']:
    lista.append(i['id_cliente'])
    lista2=set(lista)
    print(lista2)








##miJson["ventas"]["clientes"][0]["lola"]=miJson["ventas"]["clientes"][0].pop("id")
##l=miJson["ventas"]["clientes"][0].pop("id")
##nuevo_json= json.dumps(miJson)


