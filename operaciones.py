# Entrada de números ingresados por el usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Suma
suma = numero1 + numero2
print("La suma de", numero1, "+", numero2, "es:", suma)

# Resta
resta = numero1 - numero2
print("La resta de", numero1, "-", numero2, "es:", resta)

# Multiplicación
multiplicacion = numero1 * numero2
print("La multiplicación de", numero1, "*", numero2, "es:", multiplicacion)

# División
if numero2 == 0:
    print("Error: No es posible dividir por cero.")
else:
    division = numero1 / numero2
    print("La división de", numero1, "/", numero2, "es:", division)