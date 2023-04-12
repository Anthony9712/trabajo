def sumar(a, b):
    """Funcion que suma dos numeros"""
    return a + b

def restar(a, b):
    """Funcion que resta dos numeros"""
    return a - b

def multiplicar(a, b):
    """Funcion que multiplica dos numeros"""
    return a * b

def dividir(a, b):
    """Funcion que divide dos numeros"""
    if b == 0:
        raise ValueError("No es posible dividir entre cero")
    return a / b

def main():
    """Funcion principal del programa"""
    operacion = input("Ingrese la operacion que desea realizar (+,-,*,/): ")
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))

    if operacion == '+':
        resultado = sumar(a, b)
    elif operacion == '-':
        resultado = restar(a, b)
    elif operacion == '*':
        resultado = multiplicar(a, b)
    elif operacion == '/':
        resultado = dividir(a, b)
    else:
        print("Operacion no valida.")
        return

    print(f"El resultado de la operacion es: {resultado}")