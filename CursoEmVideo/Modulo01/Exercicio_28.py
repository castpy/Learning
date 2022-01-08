import random
n1 = random.randint(0, 5)
op1 = int(input('Escolha um numero de 0 a 5: '))

if op1 == n1:
    print('Parabéns, você certou!')
else:
    print('Você errou! O número era {}.'.format(n1))