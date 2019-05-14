n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

print("¿Son iguales? ", n1 == n2)
print("¿Son diferentes?", n1 != n2)
print("¿El primero es mayor que el segundo?", n1 > n2)
print("¿El segundo es mayor o igual que el primero?", n1 <= n2)

cadena = input("Escribe una cadena: ")
print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?",
      len(cadena) >= 3 and len(cadena) < 10)

numero_magico = 12345679
numero_usuario = int(input("Introduce un número del 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print("El número mágico es:", numero_magico)
