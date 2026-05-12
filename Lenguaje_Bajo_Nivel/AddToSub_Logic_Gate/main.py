import os

def print_options():
    print("Opciones:")
    print("1. Sumar binarios")
    print("2. Restar binarios")
    print("3. Compuertas lógicas")
    print("4. Exit")
    valOptions()
    
def valOptions():
    x = input("Seleccione una opción: ")
    match x:
        case "1":
            sumar_binarios()
        case "2":
            restar_binarios()
        case "3":
            compuertas_logicas()
        case "4":
            exit()
        case _:
            print("Opción inválida. Intente de nuevo.")
            os.system("PAUSE")
            os.system("cls")
            print_options()
    
def sumar_binarios():
    print("Suma de binarios")
    A = obtener_binario(input("Ingrese el primer número binario: "))
    B = obtener_binario(input("Ingrese el segundo número binario: "))
    print("Resultado:", bin(int(A, 2) + int(B, 2))[2:])

def restar_binarios():
    print("Resta de binarios")
    A = obtener_binario(input("Ingrese el primer número binario: "))
    B = obtener_binario(input("Ingrese el segundo número binario: "))
    print("Resultado:", bin(int(A, 2) - int(B, 2))[2:])
    
def compuertas_logicas():
    print("Compuertas lógicas")
    try:
        A = int(input("Ingrese el primer número: "))
        B = int(input("Ingrese el segundo número: "))
        bits = max(A.bit_length(), B.bit_length())
        mask = (1 << bits) - 1
        
        print("Número A en binario:", bin(A)[2:].zfill(bits))
        print("Número B en binario:", bin(B)[2:].zfill(bits))
        print("-" * 10)
        
        print("AND:", bin(A & B)[2:].zfill(bits))
        print("OR:", bin(A | B)[2:].zfill(bits))
        print("XOR:", bin(A ^ B)[2:].zfill(bits))
        print("NOT A:", bin(~A & mask)[2:].zfill(bits))
        print("NOT B:", bin(~B & mask)[2:].zfill(bits))
        
    except ValueError:
        print("Los números ingresados no son válidos. Intente de nuevo.")
        os.system("PAUSE")
        os.system("cls")
        compuertas_logicas()

def obtener_binario(x):
    try:
        int(x, 2)
        return x
    except ValueError:
        print("El numero ingresado no es un número binario válido. Intente de nuevo.")
        return obtener_binario(input("Ingrese un número binario: "))

def __main__():
    while True:
        os.system("PAUSE")
        os.system("cls")
        print_options()
    
__main__()