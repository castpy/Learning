print('=' * 20)
print('10 termos de uma PA')
print('=' * 20)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Digite a razão: '))
dec = n1 + (10 - 1) * n2

for c in range(n1, dec + n2, n2):
    print(c, end=' -> ')
print('Acabou')
