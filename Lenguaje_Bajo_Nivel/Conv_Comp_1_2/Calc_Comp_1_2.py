import os 

def logic():
    try:
        num = int(input("Ingresa un numero decimal positivo: "))
        if 0 <= num <= 255:
            bits = calcBits(num)
            print("Numero binario: ", format(num, f"0{bits}b"))
            comp1 = CompA1(num, bits)
            print("Complemento A1: ", comp1)
            comp2 = CompA2(num, bits)
            print("Complemento A 2: ", comp2)
            print(f"Comprobacion:\n {bin(num)[2:].zfill(bits)}\n+{comp2}\n{'-' * (bits + 1)}\n {Comp(num, int(comp2,2), bits)}")
        else:
            print("Error de rango")

    except ValueError:
        print("Debes ingresar un numero entero valido")

def calcBits(x):
    bits = max(1, x.bit_length())
    return 8 if bits >= 5 else 4

def CompA1(x, bits):
    mask = (1 << bits) - 1
    return format((~x) & mask, f"0{bits}b")

def CompA2(num, bits):
    mask = (1 << bits) - 1
    return format((~num + 1) & mask, f"0{bits}b")

def Comp(x, comp2, bits):
    mask = (1 << bits) - 1
    return format(((x + comp2) & mask), f"0{bits}b")

def run():
    while(True):
        os.system("clear")
        logic()
        res = input("¿Deseas continuar? (Ingresa cualquier letra o \'n\' para finalizar): ")
        if ('N' == res or 'n' == res):
            exit(0)

run()