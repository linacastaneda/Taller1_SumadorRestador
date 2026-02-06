"""
Sumador – Restador binario de 4 bits
Implementado usando únicamente puertas AND, OR y NOT
"""

# ===============================
# PUERTAS LÓGICAS
# ===============================

def AND(a, b):
    # Puerta AND: retorna 1 solo si ambos valores son 1
    return a & b

def OR(a, b):
    # Puerta OR: retorna 1 si al menos uno de los valores es 1
    return a | b

def NOT(a):
    # Puerta NOT: invierte el valor (0->1, 1->0)
    return 1 - a


# ===============================
# XOR CONSTRUIDO CON PUERTAS BÁSICAS
# ===============================

def XOR(a, b):
    # Puerta XOR: retorna 1 si los valores son diferentes
    # (a AND NOT b) OR (NOT a AND b)
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


# ===============================
# SUMADOR COMPLETO DE 1 BIT
# ===============================

def full_adder(a, b, cin):
    # Primer XOR entre a y b
    s1 = XOR(a, b)
    # Segunda XOR con el acarreo de entrada para obtener el bit de suma
    suma = XOR(s1, cin)

    # Se generan los acarreos parciales
    c1 = AND(a, b)      # Acarreo si a y b son 1
    c2 = AND(a, cin)    # Acarreo si a y el acarreo de entrada son 1
    c3 = AND(b, cin)    # Acarreo si b y el acarreo de entrada son 1

    # El acarreo de salida es 1 si alguno de los acarreos parciales es 1
    cout = OR(OR(c1, c2), c3)

    # Retorna el bit de suma y el acarreo de salida
    return suma, cout


# ===============================
# SUMADOR – RESTADOR DE 4 BITS
# ===============================

def adder_subtractor_4bits(A, B, M):
    # Lista para almacenar los resultados de cada bit
    resultado = []
    # El acarreo inicial es igual al modo (0 para suma, 1 para resta)
    carry = M

    # Procesa cada bit de los números de 4 bits
    for i in range(4):
        # Modifica B[i] con XOR(B[i], M) para aplicación de modo
        # Si M=0 (suma): B[i] se mantiene igual
        # Si M=1 (resta): B[i] se invierte (complemento a 1)
        b_mod = XOR(B[i], M)
        # Llama al sumador completo de 1 bit
        s, carry = full_adder(A[i], b_mod, carry)
        # Almacena el bit de resultado
        resultado.append(s)

    # Retorna el resultado de 4 bits y el acarreo final
    return resultado, carry
