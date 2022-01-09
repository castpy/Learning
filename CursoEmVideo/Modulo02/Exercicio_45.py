print('=' * 30)
print('Game - Pedra, Papel, Tesoura v.1.0')
print('=' * 30)

from random import randint
lista = ('Pedra', 'Papel', 'Tesoura')

cpu = randint(0, 2)

player = int(input('''
[0] Pedra
[1] Papel
[2] Tesoura

-> '''))

print('''
{0}
        CPU: {1}
        \033[32mVocê\033[m: {2}
{3}'''.format("-=" * 20, lista[cpu], lista[player], "-=" * 20))

if cpu == 0: #CPU - PEDRA
    if player == 0:
        print('Deu empate!')
    elif player == 1:
        print('\033[32mJogador ganhou!\033[m')
    elif player == 2:
        print('\033[31mJogador perdeu!\033[m')
    else:
        print('Escolha inválida')

elif cpu == 1: #CPU - PAPEL
    if player == 0:
        print('\033[31mJogador perdeu!\033[m')
    elif player == 1:
        print('Deu empate!')
    elif player == 2:
        print('\033[32mJogador ganhou\033[m')
    else:
        print('Escolha inválida')

elif cpu == 2: #CPU - TESOURA
    if player == 0:
        print('\033[32mJogador ganhou!\033[m')
    elif player == 1:
        print('\033[31mJogador Perdeu!\033[m')
    elif player == 2:
        print('Deu empate!')
    else:
        print('Escolha inválida')
