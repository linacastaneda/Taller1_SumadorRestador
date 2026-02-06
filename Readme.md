# Sumador / Restador de 4 Bits usando Puertas Lógicas

## Descripción general
Este proyecto implementa un **sumador–restador de 4 bits** utilizando únicamente **puertas lógicas básicas** (AND, OR y NOT). A partir de estas puertas se construye la operación XOR, un **sumador completo de 1 bit**, y finalmente un sistema de **4 bits conectado en cascada**.

La implementación se realiza en **Python**, simulando el comportamiento interno de un circuito digital a nivel de hardware, similar al de una **Unidad Aritmético-Lógica (ALU)**.

---

## Objetivos
- Implementar la suma y resta binaria de 4 bits.
- Construir todas las operaciones a partir de puertas lógicas básicas.
- Simular el funcionamiento real de un sumador–restador digital.
- Validar la implementación mediante pruebas unitarias.

---

## Diseño del sistema

### Arquitectura general

![Diagrama lógico del sumador-restador de 4 bits](./DiagramaLogico.png)
El sistema está compuesto por **cuatro sumadores completos de 1 bit (SC)** conectados en cascada, formando un **ripple-carry adder**.

Cada sumador completo recibe:
- Un bit del operando **A**
- Un bit del operando **B** (posiblemente invertido)
- Un acarreo de entrada (**Cin**)

Y produce:
- Un bit de salida (**S**)
- Un acarreo de salida (**Cout**)

El **Cout** de cada etapa se conecta al **Cin** de la siguiente.

---

### Control de suma y resta
La operación se controla mediante el bit **M (Modo)**:

| M | Operación |
|---|----------|
| 0 | Suma |
| 1 | Resta |

Para la resta se utiliza el **complemento a dos**:

A − B = A + (~B + 1)


Esto se logra mediante:
- Una compuerta **XOR** entre cada bit de **B** y el bit **M**
- La inicialización del acarreo de entrada con el valor de **M**

---

## Diagrama lógico del sistema

El siguiente diagrama muestra el diseño completo del **sumador–restador de 4 bits**, construido a partir de **sumadores completos de 1 bit (SC)** conectados en cascada y controlados por la señal de modo **M**.

- Cada bit del operando **B** se combina con **M** mediante una compuerta XOR.
- El acarreo de salida (**Cout**) de cada SC se conecta al acarreo de entrada (**Cin**) del siguiente.
- El primer **Cin** se inicializa con **M**, permitiendo implementar el complemento a dos en la resta.

<p align="center">
  <img src="./DiagramaLogico.png" alt="Diagrama lógico del sumador-restador de 4 bits" width="700">
</p>

La implementación en software es una **traducción directa** de este diseño lógico.

---

### Correspondencia entre diagrama e implementación

| Elemento del diagrama | Implementación en Python |
|----------------------|--------------------------|
| XOR entre B y M | `XOR(B[i], M)` |
| Cin inicial | `acarreo = M` |
| Sumador completo (SC) | `sumador_completo()` |
| Propagación de acarreo | variable `acarreo` |
| Salidas S0–S3 | lista `resultado` |
| Acarreo final C3 | `acarreo` final |

---

## Implementación

### Lenguaje utilizado
- Python 3

### Estructura del proyecto


SUMADOR_RESTADOR4BITS/
│
├── DiagramaLogico.png
├── README.md
├── Sumador_Restador.py
├── Tests.py
└── pycache/


---

## Puertas lógicas implementadas

### Tabla de verdad – AND
| A | B | AND |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Tabla de verdad – OR
| A | B | OR |
|---|---|----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Tabla de verdad – NOT
| A | NOT(A) |
|---|--------|
| 0 | 1 |
| 1 | 0 |

### Tabla de verdad – XOR
| A | B | XOR |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

## Sumador completo de 1 bit

### Tabla de verdad
| A | B | Cin | S | Cout |
|---|---|-----|---|------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

---

## Pruebas y validación

### Herramienta utilizada
Se utilizó el módulo **unittest** de Python.

### Resultados
Al ejecutar:


python Tests.py


El sistema devuelve:


OK


Confirmando que todas las funciones cumplen con el diseño lógico propuesto.