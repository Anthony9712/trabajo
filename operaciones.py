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

num = int(input("Introduzca un número entero positivo mayor que 2: "))

divisor = 2

while num % divisor != 0:
    divisor = divisor + 1

if divisor == num:
    print(str(num) + " es primo")
else:
    print(str(num) + " no es primo")

def verificar(self):
    codigo = self.codigoT.get()

    for i in codigo:
        if i not in '0123456789':
            self.codigoT.delete(codigo.isdigit(i), codigo.isdigit(i)+1)