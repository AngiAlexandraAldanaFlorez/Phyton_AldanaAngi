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