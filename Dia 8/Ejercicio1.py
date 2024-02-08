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
    lista.append(i["id_cliente"])
sin_repetir = set(lista)
ultimo_conjunto = sin_repetir[-1]  
print(ultimo_conjunto)

#4. Devuelve un listado de todos 
#los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.

import datetime

fecha_inicio_2017 = datetime.datetime(2017, 1, 1)
fecha_fin_2017 = datetime.datetime(2017, 12, 31)

pedidos_2017_superiores_500 = []

for pedido in miJson['ventas']['pedidos']:
    fecha_pedido = datetime.datetime.strptime(pedido['fecha'], '%Y-%m-%d')
    if fecha_inicio_2017 <= fecha_pedido <= fecha_fin_2017:
        cantidad_total = pedido['total']
        if cantidad_total > 500:
            pedidos_2017_superiores_500.append(pedido)

# Imprimir los pedidos encontrados
for pedido in pedidos_2017_superiores_500:
    print(pedido)





##miJson["ventas"]["clientes"][0]["lola"]=miJson["ventas"]["clientes"][0].pop("id")
##l=miJson["ventas"]["clientes"][0].pop("id")
##nuevo_json= json.dumps(miJson)


