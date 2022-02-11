n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

if n1 > n2:
    print('O número {} é maior'.format(n1))
elif n1 < n2:
    print('O número {} é maior'.format(n2))
elif n1 == n2:
    print('Os dois números são iguais!')
else:
    print('Algo deu errado!')
    