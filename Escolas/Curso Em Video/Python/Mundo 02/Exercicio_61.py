print('=' * 20)
print('10 termos de uma PA - Com While')
print('=' * 20)

n1 = int(input('Prieiro  termo: '))
n2 = int(input('Digite a razão: '))
dec = n1 + (10 -1) * n2
termo = n1
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += n2
    contador += 1
print('ACABOU')