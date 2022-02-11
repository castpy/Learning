print('-'*20)
print('Sequencia de Fibonacci')
print('-'*20)

n = int(input('Quantos termos você quer mostrar? '))

termo1 = 0
termo2 = 1
contador = 3
print('{} -> {}'.format(termo1, termo2), end='')

while contador <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    contador += 1
    termo1 = termo2
    termo2 = termo3
print(' -> Fim')