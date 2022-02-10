#! python
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        nome_arquivo = sys.argv[0][2:]
        print("É necessário informar o raio do círculo.")
        print(f"Sintaxe: {nome_arquivo} <raio>")
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print("Área do círculo", area)