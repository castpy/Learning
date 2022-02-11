pessoas = maior = homem = mulher = 0

while True:
    print('-'*30)
    print(' '*5, '\033[32mCADASTRE UMA PESSOA\033[m')
    print('-'*30)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas += 1
    print('-'*30)
    op = str(input('Deseja continuar? [S/N] \n')).upper().strip()[0]

    if idade >= 18:
        maior += 1
    if sexo == 'F':
        mulher += 1
    if sexo == 'M':
        homem += 1

    if op == 'S':
        continue
    else:
        break
print('#'*30)
print(f'Total de Pessoas = {pessoas}\nTotal de Homens = {homem}\nTotal de Mulheres = {mulher}\nMaiores de 18 anos = {maior}')
print('#'*30)
