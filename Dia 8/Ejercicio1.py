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
clientes = set()

for pedido in pedidos:
    clientes.add(pedido['id_cliente'])

clientes_con_pedido = list(clientes)
for i in clientes_con_pedido:
    print("id_cliente ",i)

#4. Devuelve un listado de todos 
#los pedidos que se realizaron durante el año 2017,
# cuya cantidad total sea superior a 500€.

pedidos_2017_mas_500 = [pedido for pedido in pedidos if pedido['fecha'].startswith('2017') and pedido['total'] > 500]
for i in pedidos_2017_mas_500:
    print(i)

#5.Devuelve un listado con el nombre y los apellidos de los comerciales 
#que tienen una comisión entre 0.05 y 0.11.

#comerciales_filtrados = [{'nombre': c['nombre'], 'apellido1': c['apellido1'], 'apellido2': c['apellido2']} for c in comerciales if 0.05 <= c['comisión'] <= 0.11]

#print(comerciales_filtrados)
comerciales = ventas.get('comerciales') 
##6.Devuelve el valor de la comisión de mayor 
#valor que existe en la tabla comercial
for comercial in comerciales:
    if comercial['comision'] > comision_maxima:
        comision_maxima = comercial['comision']

print("La comisión máxima es:", comision_maxima)

ordenados8 = sorted(comerciales     , key=lambda x: x["comisiones"], reverse=True)
print(ordenados8[0])

##miJson["ventas"]["clientes"][0]["lola"]=miJson["ventas"]["clientes"][0].pop("id")
##l=miJson["ventas"]["clientes"][0].pop("id")
##nuevo_json= json.dumps(miJson)


