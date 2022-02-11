from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    cpu = randint(0, 10)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {cpu}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente....')
print(f'Você perdeu e sua pontuação é {v}')