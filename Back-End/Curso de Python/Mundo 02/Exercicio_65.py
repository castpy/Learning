resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    n1 = int(input('Digite um número: '))
    soma += n1
    quantidade += 1
    if quantidade == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}.\nO maior número foi {} e o menor foi {}.'.format(quantidade, media, maior, menor))
