#! python

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:

        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # O file ele escreve em um arquivo de saida
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado')

if saida.closed:
    print('Arquivo de saída já foi fechado')
