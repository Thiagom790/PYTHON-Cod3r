#! python
# na função abaixo sequencia é um parametro padrão
def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números na sequência
    for fib in fibonacci(20):
        print(fib)
