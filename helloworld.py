print("Hello World puñetas")
print("=" * 19)

# VARIABLES
nombre, apellido = 'Joaquin', 'Navedo'
print(nombre, apellido)

# TIPOS PRIMTIVOS
nombre = 'Joaquin'  # literal string
edad = 28  # literal int
pi = 3.1416  # literal decimal
usoreloj = True  # literal boolean
usorelojs = None  # literal null or empty

# TIPOS DINAMICOS
nombre = 'Joaquin'
print(type(nombre))
nombre = 10
print(type(nombre))

# LISTAS
letras = ['a', 'b', 'c']
print(letras[0])  # letra a
print(letras[1])  # letra b
print(letras[2])  # letra c

print(letras[-1])  # letra c
print(letras[-2])  # letra b
print(letras[-3])  # letra a

# MULTIPLE INDICES
palabra = 'python'
print(palabra[0:2])  # se exculye la letra en la posicion 2 => 'py'
print(palabra[2:])  # se excluye antes del 2 'thon'
print(palabra[:2])  # se excluye despues del 2 => 'py'

# LISTAS ANIDADAS O SUBLISTAS
nombre, apellido, edad = 'Joaquin', 'Navedo', 28
personas = [
    [nombre, apellido, edad],
    ['Yamileth', 'Mayo', 27],
    ['Sandra', 'Torres', 27]
]

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = a, b, c
e = a + b + c
print(d)
print(e)

print(personas[2][2])  # ambso debuelben la misma respuesta
print(personas[-1][-1])
print(personas[0][0])
print(len(personas))
print(len(personas[0]))

letras = ['a', 'b', 'c', 'd', 'e']
print(letras[:3])
# haciendo esto seleccionamos los tres primeras posiciones y las cambiamos a maysculas
letras[:3] = ['A', 'B', 'C']
print(letras)
letras[:3] = []  # vacioamos el valor de las primeras 3 posiciones
print(letras)


# DICCIONARIOS
colores = {
    'rojo': 'red',
    'azul': 'blue',
    'negro': 'balck'
}
colores['gris'] = 'gray'  # sobre escritura

print(colores['gris'])
print(colores['negro'])
print(len(colores))  # sale 4 por que sobre escribi el gris

# LECTURA POR TECLADO
# valor = input('Introduce un valor: ')
# valor = int(valor)
valor = float(input('Introduce un valor: '))
print(valor)

# FUNCIONES


def sayHi(nombre, apellido):
    print('hello', nombre, apellido)


sayHi('Joaquin', 'Navedo')

# FUNCIONES CON RETORNO


def doblar(numero):
    print(numero * 2)


doblar(5)


def double(number):
    return number * 2


number = double(5)
numberdouble = double(double(double(5)))
print(number)
print(numberdouble)
