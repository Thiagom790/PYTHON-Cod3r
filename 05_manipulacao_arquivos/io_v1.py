#! python
arquivo = open('pessoas.csv')
dados = arquivo.read()
# liberei os recursos desse arquivo que o sistema estava usando
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(",")))
