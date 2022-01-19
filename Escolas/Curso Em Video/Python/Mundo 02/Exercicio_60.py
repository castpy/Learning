#============== Método 1 ==============#
from math import factorial
print('\033[32m='*10, 'Primeiro método fatorial', '='*10,'\033[m')
n1 = int(input('Digite um número: '))
fat = factorial(n1)
print('O fatorial de {} é {}'.format(n1, fat))
#=======================================#

#============== Método 2 ==============#
print('\033[33m='*10, 'Segundo método fatorial', '='*11,'\033[m')
n2 = int(input('Digite um número: '))
cont = n2
fato = 1
print('Calculando {}! '.format(n2), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fato *= cont
    cont -= 1
print('{}'.format(fato))
#=======================================#