#! python
arquivo = open('pessoas.csv')
# dessa forma eu utilizo o streaming
# eu consumo de forma mais otimizadas os recursos
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
