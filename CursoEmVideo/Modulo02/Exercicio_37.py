num = int(input('Digite um número: '))
op = int(input('''
    \033[32m Para qual base de numerica você deseja converter?\033[m
[1] Binário
[2] Octal
[3] Hexadecimal

-> '''))

if op == 1:
    print('{} Em binário o valor é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} Em Octal o valor é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} Em Hexadecimal o valor é {}'.format(num, hex(num)[2:]))
else:
    print('Algo deu errado!')   