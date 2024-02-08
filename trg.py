comerciales = [
    {'nombre': 'Juan', 'apellidos': 'González', 'comision': 0.08},
    {'nombre': 'María', 'apellidos': 'López', 'comision': 0.12},
    {'nombre': 'Pedro', 'apellidos': 'Martínez', 'comision': 0.06},
    {'nombre': 'Ana', 'apellidos': 'García', 'comision': 0.10},
    {'nombre': 'Luis', 'apellidos': 'Sánchez', 'comision': 0.04},
]

# Filtrar los comerciales con comisión entre 0.05 y 0.11 y obtener su nombre y apellidos
comerciales_filtrados = [{'nombre': c['nombre'], 'apellidos': c['apellidos']} for c in comerciales if 0.05 <= c['comision'] <= 0.11]

print(comerciales_filtrados)

comerciales = [
    {'nombre': 'Juan', 'apellidos': 'González', 'comision': 0.08},
    {'nombre': 'María', 'apellidos': 'López', 'comision': 0.12},
    {'nombre': 'Pedro', 'apellidos': 'Martínez', 'comision': 0.06},
    {'nombre': 'Ana', 'apellidos': 'García', 'comision': 0.10},
    {'nombre': 'Luis', 'apellidos': 'Sánchez', 'comision': 0.04},
]

# Inicializamos la comisión máxima con un valor muy bajo
comision_maxima = float('-inf')

# Iteramos sobre los comerciales y actualizamos la comisión máxima si encontramos una comisión mayor
for comercial in comerciales:
    if comercial['comision'] > comision_maxima:
        comision_maxima = comercial['comision']

print("La comisión máxima es:", comision_maxima)


