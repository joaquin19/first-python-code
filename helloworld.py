print("Hello World puñetas")
print("=" * 19)

# esta parte son variables
nombre, apellido = 'Joaquin', 'Navedo'
print(nombre, apellido)

# esta parte son tipos primitivos
nombre = 'Joaquin'  # literal string
edad = 28  # literal int
pi = 3.1416  # literal decimal
usoreloj = True  # literal boolean
usorelojs = None  # literal null or empty

# esta parte son los tipos dinamicos
nombre = 'Joaquin'
print(type(nombre))
nombre = 10
print(type(nombre))

# esta arte es de Listas
letras = ['a', 'b', 'c']
print(letras[0])  # letra a
print(letras[1])  # letra b
print(letras[2])  # letra c

print(letras[-1])  # letra c
print(letras[-2])  # letra b
print(letras[-3])  # letra a

# Listas anidadas o sublistas
nombre, apellido, edad = 'Joaquin', 'Navedo', 28
personas = [
    [nombre, apellido, edad],
    ['Yamileth', 'Mayo', 27],
    ['Sandra', 'Torres', 27]
]

print(personas[2][2])  # ambso debuelben la misma respuesta
print(personas[-1][-1])
print(personas[0][0])
print(len(personas))
print(len(personas[0]))

# Diccionarios
colores = {
    'rojo': 'red',
    'azul': 'blue',
    'negro': 'balck'
}
colores['gris'] = 'gray'  # sobre escritura

print(colores['gris'])
print(colores['negro'])
print(len(colores))  # sale 4 por que sobre escribi el gris

# Funciones


def sayHi(nombre, apellido):
    print('hello', nombre, apellido)


sayHi('Joaquin', 'Navedo')

# Funciones con retorno


def doblar(numero):
    print(numero * 2)


doblar(5)


def double(number):
    return number * 2


number = double(5)
numberdouble = double(double(double(5)))
print(number)
print(numberdouble)
