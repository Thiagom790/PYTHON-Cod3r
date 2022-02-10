#! python
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f"{posicao + 1})", nome)

dias_semana = (
    'Domingo',   'Segunda', 'Terça',
    'Quarta', 'Quinta', 'Sexta', 'Sábado'
)

for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('Muito legal'):
    print(letra)

for numero in {1, 2, 3, 4}:
    print(numero)
