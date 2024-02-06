def calcular_definitiva(n1, n2, n3):
        n1=nota1*0.30
        n2=nota2*0.30
        n3=nota3*0.40
        notadefinitiva=n1+n2+n3
        return notadefinitiva    
Estudiantes=2
list=[]
#estudiante1
for i in range(Estudiantes):
    nota1=int(input('Ingrese nota #1 '))
    nota2=int(input('Ingrese nota #2 '))
    nota3=int(input('ingrese nota #3 '))

    notadefinitiva=calcular_definitiva(nota1,nota2,nota3)
    list.append(notadefinitiva)
    if notadefinitiva < 2:
        print('No puede habilitar')
    elif notadefinitiva < 3:
        print('Reprobó')
    elif notadefinitiva > 3:
        print('¡Aprobó!')
    elif notadefinitiva > 4.5: 
        print('¡Felicitaciones!')

    print(f'nota definitiva= {notadefinitiva}')

print(list)

if list[1]>list[2]:
    print('Promedio mayor es el estudiante #1')
    