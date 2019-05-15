number1 = float(input('first number: '))
number2 = float(input('second number: '))
opcion = 0

print('''
Que quieres perro?

1) sumar ese
2) restar culo
3) multiplicar bato
''')

opcion = int(input('selecciona tu opcion: '))

if opcion == 1:
    print('la suma de', number1, '+', number2,
          'es igual a:', number1 + number2)
elif opcion == 2:
    print('la resta de', number1, '-', number2,
          'es igual a:', number1 - number2)
elif opcion == 3:
    print('la multiplicacion de', number1, '*',
          number2, 'es igual a:', number1 * number2)
else:
    print('esa mierda no existe perro!!!!')

# toma 1
numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: "))

# toma 2
# Primera forma con función sum()
suma = sum(range(0, 101, 2))
print(suma)

# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1

print(suma)

suma = 0
numeros = int(input("¿Cuántos números quieres introducir? "))
for x in range(numeros):
    suma += float(input("Introduce un número: "))
print("Se han introducido", numeros, "números que en total han sumado",
      suma, "y la media es", suma/numeros)

# toma 3
numeros = [1, 3, 6, 9]
while True:
    numero = int(input("Escribe un número del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
if numero in numeros:
    print("El número", numero, "se encuentra en la lista", numeros)
else:
    print("El número", numero, "no se encuentra en la lista", numeros)

# toma 4
lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']
lista_3 = []
for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)

# toma 5
print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))
