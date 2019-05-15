# SENTENCIA IF
if (True):
    print('::::::SENTENCIAS IF:::::')

a = 5
if a == 2:
    print('a vale 2')
if a == 5:
    print('a vale 5')

a = 5
b = 10
if a == 5:
    print('a vale', a)
    if b == 10:
        print('y b vale', b)

if a == 5 and b == 10:
    print('a vale', a, 'y b vale', b)

n = 11
if n % 2 == 0:
    print(n, 'es un par')
else:
    print(n, 'es impar')

command = 'out'
if command == 'in':
    print('welcome to system')
elif command == 'say hi':
    print('Hi , i hope you fine')
elif command == 'out':
    print('out of system....')
else:
    print('unknown command')

nota = float(input('introduce una nota: '))
if nota >= 9:
    print('aaaa pirruuuu')
elif nota >= 7 and nota < 9:
    print('por poquito culo')
else:
    print('coti')

# SENTENCIA WHILE
c = 0
while c <= 5:
    c += 1
    print('c vale', c, 'SENETNCIAS WHILE')
else:
    print('se ha cumplido toda la iteracion y c vale', c)

c = 0
while c <= 5:
    c += 1
    if (c == 2):
        print('rompemos el bucle cuando c vale', c)
        break
    print('c vale', c)
else:
    print('se ha cumplido toda la iteracion y c vale', c)

c = 0
while c <= 5:
    c += 1
    if (c == 2):
        print('continuamos despues de que c vale', c)
        continue
    print('c vale', c)
else:
    print('se ha cumplido toda la iteracion y c vale', c)

print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", n1+n2)
    elif opcion == '3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")

# SENTENCIA FOR
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
# estas sentencias equivalen lo mismo pero for es mas sencillo y eficaz
while (indice < len(numeros)):
    print(numeros[indice])
    indice += 1

for number in numeros:
    print(number)

# estas sentencias equivalen lo mismo pero for es mas sencillo y eficaz
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
for number in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)

cadena = 'hola que hace?'
for caracter in cadena:
    print(caracter)

cadena2 = ''
for caracter in cadena:
    cadena2 += '*'
print(cadena)
print(cadena2)

for i in range(10):
    print(i)
