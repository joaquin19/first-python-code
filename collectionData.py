# TUPLES
from collections import deque
tuple = (100, 'hola', [1, 2, 3, 4], -50)
print(tuple)
print(tuple[0])
print(tuple[2:])
print(len(tuple[1]))
print(len(tuple))
print(tuple.index(-50))
print(tuple.count(100))

# CONJUNTOS
conjunto = set()
conjunto = {1, 2, 3}
print(conjunto)
conjunto.add('A')
print(conjunto)

grupo = {'erick', 'dave', 'jasso', 'joaquin'}
print('joaquin' in grupo)

L = [1, 2, 3, 3, 2, 1]
c = set(L)
print(c)
l = list(c)
print(l)
l = list(set(L))
print(l)

# DICCIONARIOS
vacio = {}
type(vacio)
print(type(vacio))

colores = {'amarillo': 'yelow', 'azul': 'blue', 'verde': 'green'}
print(colores['azul'])
numeros = {10: 'diez', 20: 'veinte', 34: 'treinta y cuatro'}
print(numeros[34])  # modifica del diccionario
numeros[10] = 'quince'
print(numeros)
del(colores['azul'])  # borra del diccionario
print(colores)
edades = {'joaquin': 27, 'sandra': 26, 'nacim': 23}
edades['joaquin'] += 1
print(edades)
for edad in edades:
    print(edad)
    print(edades[edad])
for claves in edades:
    print(claves, edades[claves])

for c, v in edades.items():
    print(c, v)

# COLLECCION DE DATOS AVANZADOS
pjOfWow = []

wow = {'name': 'Trall', 'class': 'Chaman',
       'raza': 'Orco', 'status': 'Jefe de Guerra'}
pjOfWow.append(wow)
print(pjOfWow)
wow = {'name': 'Arthas', 'class': 'Death Knight',
       'raza': 'Human-No-Dead', 'status': 'King Linch'}
pjOfWow.append(wow)
print(pjOfWow)

for wow in pjOfWow:
    print(wow['name'], wow['class'], wow['raza'], wow['status'])

# PILAS Y COLAS
pila = [3, 4, 5]
pila.append(6)
pila.append(7)  # saca el elemento 7 y 6 de la pila
print(pila)
print(pila.pop())  # saca un elemnto de la pila

cola = deque()
print(cola)
cola = deque(['joaquin', 'alejandro', 'lex'])
print(cola)
cola.append('Sandra')
print(cola)
cola.popleft()
print(cola)
