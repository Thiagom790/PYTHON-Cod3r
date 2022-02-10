#! python
# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(quantidade):
    resultado = [0, 1]
    # o _ significa uma váriavel que não está sendo usada
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequência
    for fib in fibonacci(20):
        print(fib)
