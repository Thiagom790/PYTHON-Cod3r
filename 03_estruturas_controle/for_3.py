#! python
produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'Estoque': 793}

for chave in produto:
    print(chave)

print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, "=", valor)

# eu depois consigo acessar os valor fora do for
# então cuidado
print(chave, valor)
