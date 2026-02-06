
#puertas lógicas


def Y(a, b):
    # si los dos valores son 1, retorna 1. si no, retorna 0
    return a & b

def O(a, b):
    # si al menos uno es 1, retorna 1. si los dos son 0, retorna 0
    return a | b

def NO(a):
    # invierte el valor: 0 se convierte en 1, 1 se convierte en 0
    return 1 - a

#xor con puertas AND, OR y NOT

def XOR(a, b):
    # retorna 1 si los valores son diferentes, retorna 0 si son iguales
    return O(Y(a, NO(b)), Y(NO(a), b))


#sumador completo de 1 bit

def sumador_completo(a, b, acarreo_entrada):
    # calcula XOR de a y b
    s1 = XOR(a, b)
    # calcula XOR del resultado anterior con el acarreo
    suma = XOR(s1, acarreo_entrada)

    # generamos tres acarreos posibles
    acarreo1 = Y(a, b)              # hay acarreo si a y b son 1
    acarreo2 = Y(a, acarreo_entrada)    # hay acarreo si a y el acarreo anterior son 1
    acarreo3 = Y(b, acarreo_entrada)    # hay acarreo si b y el acarreo anterior son 1

    # si alguno de los tres acarreos es 1, el acarreo de salida es 1
    acarreo_salida = O(O(acarreo1, acarreo2), acarreo3)

    # devolvemos el resultado y el acarreo para la siguiente suma
    return suma, acarreo_salida


# sumador/restador de 4 bits

def sumador_restador_4bits(A, B, M):
    # aquí guardamos los resultados de cada bit
    resultado = []
    # si M es 0 sumamos, si M es 1 restamos
    acarreo = M

    # procesamos cada uno de los 4 bits
    for i in range(4):
        # si M es 0 (suma), B se queda igual. si M es 1 (resta), B se invierte
        b_modificado = XOR(B[i], M)
        # sumamos bit por bit con el acarreo anterior
        s, acarreo = sumador_completo(A[i], b_modificado, acarreo)
        # guardamos el resultado
        resultado.append(s)

    # devolvemos los 4 bits del resultado y el acarreo final
    return resultado, acarreo
