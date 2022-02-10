#! python

import csv
from urllib import request


def read(url):
    # esse request ele faz um requisição
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # o r ele mostra o arquivo como se fosse cru
    # ou seja isso chama string raw
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
