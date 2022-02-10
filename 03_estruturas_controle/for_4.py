#! python

# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# funcao sortear_dado numeros entre 1 e 6
# For com range 1 a 6
# Se for impar continue
# Se o numero for par e igual ao valor sorteado
# pela funcao dado imprimir 'ACERTOU' e depois chamar o break
# Se não acetar chama o else... print('Não acertou o número')

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número!')
