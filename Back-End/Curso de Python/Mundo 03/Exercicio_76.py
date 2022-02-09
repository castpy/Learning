lista = (
    'Lapis', 1.50,
    'Caderno', 15.75,
    'Mochila', 100,
    'Caneta', 1.25,
    'Notebook', 2500
)

print('-'*50)
print(f'{"Lista de preços":^40}')
print('-'*50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f' R$:{lista[pos]:.2f}')
print('-'*50)
