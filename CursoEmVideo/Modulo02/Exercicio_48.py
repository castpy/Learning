soma = 0
cont = 0
for c in range (1, 501, 2):
    if (c % 3) == 0:
        soma += c
        cont += 1
print('A soma de todos os valores é {}'.format(soma))
print('Foram encontrados um total de {} números impares multiplos de 3'.format(cont))