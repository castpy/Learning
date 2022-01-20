from random import randint
from time import sleep

print('='*15, 'Jogo da Adivinhação', '='*15)
sleep(1)
print('Acabei de pensar em um número de 0 a 10')
sleep(1)
print('Tente adivinhar!!')

cpu = randint(0, 11)
contador = 0
palpite = ''

while palpite != cpu:
    palpite = int(input('Qual seu palpite? '))
    contador += 1
    if cpu > palpite:
        print('Mais!!!!')
    if cpu < palpite:
        print('Menos!!!')
    if palpite == cpu:
        print('Parabéns! Você acertou em {} repetições.'.format(contador))
    