print('=' * 20)
print('10 termos de uma PA - Com While')
print('=' * 20)

n1 = int(input('Prieiro  termo: '))
n2 = int(input('Digite a razão: '))
dec = n1 + (10 -1) * n2
termo = n1
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += n2
        contador += 1
    print('PAUSE')
    mais = int(input('Quantos termos a mais você quer mostrar a mais? '))
print('Fim')
print('Progressão finalizada com {} termos.'.format(total))