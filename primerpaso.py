n = 0               # asignacion de 0 en n
while n < 10:       # expresion relacional que devuelve true
    if (n % 2) == 0:        # expresion aritmetica t relacional
        print(n, 'es un numero par')
    else:
        print(n, 'es un numero inpar')
    n = n + 1           # expresion aritmetica n = n +1 equivalente a operacion en asignacion

# OPERATORS & EXMPRESIONS

nota_1 = 10
nota_2 = 7
nota_3 = 4

# Podemos multiplicar en tanto por 1 cada nota y sumarlas
nota_final = nota_1 * 0.15 + nota_2 * 0.35 + nota_3 * 0.50
print("La nota final es", nota_final)

cadena = 'odevaN niuqaoJ 01'
# cadena volteada
# se usa el slicin (::) para voltear cadenas
cadena_volteada = cadena[::-1]
print(cadena_volteada)
print(cadena_volteada[3:], 'ha sacado un', cadena_volteada[:2], 'de nota')

# operadores relacionales
suma = 1 + 1 == 3
print(suma)  # false

# operador logico
not True == False  # true
not True  # false

# operador de asignacion
a = 0
a += 5
a
print(a)  # 5
a *= 2
a
print(a)  # 10
a /= 2
a
print(a)  # 5.0
a **= 5
a
print(a)  # 3125.0
a %= 2
a
print(a)  # 1 modulo en asignacion
