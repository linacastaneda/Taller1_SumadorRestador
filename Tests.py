# importamos las librerías necesarias
import unittest
# importamos todas las funciones del archivo Sumador_Restador
from Sumador_Restador import (
    Y, O, NO, XOR,
    sumador_completo,
    sumador_restador_4bits
)

# aquí probamos que todas las puertas lógicas funcionen correctamente
class TestPuertasLogicas(unittest.TestCase):

    # probamos la puerta Y (AND)
    def test_and(self):
        # 0 Y 0 = 0
        self.assertEqual(Y(0, 0), 0)
        # 0 Y 1 = 0
        self.assertEqual(Y(0, 1), 0)
        # 1 Y 0 = 0
        self.assertEqual(Y(1, 0), 0)
        # 1 Y 1 = 1
        self.assertEqual(Y(1, 1), 1)

    # probamos la puerta O (OR)
    def test_or(self):
        # 0 O 0 = 0
        self.assertEqual(O(0, 0), 0)
        # 0 O 1 = 1
        self.assertEqual(O(0, 1), 1)
        # 1 O 0 = 1
        self.assertEqual(O(1, 0), 1)
        # 1 O 1 = 1
        self.assertEqual(O(1, 1), 1)

    # probamos la puerta NO (NOT)
    def test_not(self):
        # NO(0) = 1
        self.assertEqual(NO(0), 1)
        # NO(1) = 0
        self.assertEqual(NO(1), 0)

    # probamos la puerta XOR
    def test_xor(self):
        # 0 XOR 0 = 0
        self.assertEqual(XOR(0, 0), 0)
        # 0 XOR 1 = 1
        self.assertEqual(XOR(0, 1), 1)
        # 1 XOR 0 = 1
        self.assertEqual(XOR(1, 0), 1)
        # 1 XOR 1 = 0
        self.assertEqual(XOR(1, 1), 0)


# aquí probamos el sumador completo de 1 bit
class TestSumadorCompleto(unittest.TestCase):

    # probamos todas las combinaciones posibles para sumar un bit
    def test_sumador_completo(self):
        # cada caso es (a, b, acarreo_entrada) -> (suma, acarreo_salida)
        casos = [
            (0, 0, 0, (0, 0)),  # 0 + 0 + 0 = 0, acarreo 0
            (0, 0, 1, (1, 0)),  # 0 + 0 + 1 = 1, acarreo 0
            (0, 1, 0, (1, 0)),  # 0 + 1 + 0 = 1, acarreo 0
            (0, 1, 1, (0, 1)),  # 0 + 1 + 1 = 0, acarreo 1
            (1, 0, 0, (1, 0)),  # 1 + 0 + 0 = 1, acarreo 0
            (1, 0, 1, (0, 1)),  # 1 + 0 + 1 = 0, acarreo 1
            (1, 1, 0, (0, 1)),  # 1 + 1 + 0 = 0, acarreo 1
            (1, 1, 1, (1, 1)),  # 1 + 1 + 1 = 1, acarreo 1
        ]

        # probamos cada caso
        for a, b, cin, esperado in casos:
            self.assertEqual(sumador_completo(a, b, cin), esperado)


# aquí probamos el sumador-restador de 4 bits
class TestSumadorRestador4Bits(unittest.TestCase):

    # probamos una suma de dos números de 4 bits
    def test_suma(self):
        # queremos sumar 5 + 3 = 8
        # 5 en binario es 0101 (pero al revés en nuestra representación)
        A = [1, 0, 1, 0]  # 5
        # 3 en binario es 0011 (pero al revés en nuestra representación)
        B = [1, 1, 0, 0]  # 3
        # M = 0 significa que vamos a sumar
        M = 0             # suma

        # hacemos la operación
        resultado, carry = sumador_restador_4bits(A, B, M)

        # el resultado debe ser 8, que en binario es 1000 (al revés: 0001)
        self.assertEqual(resultado, [0, 0, 0, 1])  # 8
        # no debe haber acarreo
        self.assertEqual(carry, 0)

    # probamos una resta de dos números de 4 bits
    def test_resta(self):
        # queremos restar 5 - 3 = 2
        # 5 en binario es 0101 (pero al revés)
        A = [1, 0, 1, 0]  # 5
        # 3 en binario es 0011 (pero al revés)
        B = [1, 1, 0, 0]  # 3
        # M = 1 significa que vamos a restar
        M = 1             # resta

        # hacemos la operación
        resultado, carry = sumador_restador_4bits(A, B, M)

        # el resultado debe ser 2, que en binario es 0010 (al revés: 0100)
        self.assertEqual(resultado, [0, 1, 0, 0])  # 2
        # con la resta debe haber acarreo final
        self.assertEqual(carry, 1)


# aquí ejecutamos todos los tests
if __name__ == "__main__":
    # unittest.main() corre todos los tests automáticamente
    unittest.main()
