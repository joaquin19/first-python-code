n = 0
while n < 10:
    if (n % 2) == 0:
        print(n, 'es un numero par')
    else:
        print(n, 'es un numero inpar')
    n = n + 1

# OPERATORS & EXMPRESIONS
cadena = 'odevaN niuqaoJ 01'
# cadena volteada
# se usa el slicin (::) para voltear cadenas
cadena_volteada = cadena[::-1]
print(cadena_volteada)
print(cadena_volteada[3:], 'ha sacado un', cadena_volteada[:2], 'de nota')
