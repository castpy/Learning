resposta = 'S'
soma = media = cont = maior = menor = 0
while resposta in 'Ss':
    n1 = int(input('Digite um número: '))
    cont += 1
    soma += n1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('A média de todos os valores é de {}'.format(media))
print('O maior número é {} e o menor é {}'.format(maior, menor))