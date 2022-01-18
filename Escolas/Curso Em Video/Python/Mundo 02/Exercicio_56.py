somaidade = 0
media = 0
totalDeMulher20 = 0
maiorIdadeHomem = 0
nomeDoMaisVelho = ''


for i in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(i), '-'*5)
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade

    if i == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo == 'F' and idade < 20:
        totalDeMulher20 += 1
    

media = somaidade / 4

print('A média da idade de todas as pessoas é de {} anos.'.format(media))
print('O homem mais velho {} anos e se chama {}.'.format(maiorIdadeHomem, nomeDoMaisVelho))
if totalDeMulher20 > 1:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalDeMulher20))
else:
    print('Ao todo é apenas {} mulhere com menos de 20 anos.'.format(totalDeMulher20))
