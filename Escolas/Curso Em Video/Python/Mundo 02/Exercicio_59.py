from time import sleep

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

op = 0

while op != 5:
  
    op = int(input('''
[1] Somar
[2] Multiplicar
[3] Saber o Maior
[4] Selecionar Novos Números
[5] Sair
-> '''))

    if op == 1:
        soma = n1 + n2
        print('A Soma é de ({} + {} = {}).'.format(n1, n2, soma))
        sleep(1)
    elif op == 2:
        soma = n1 * n2
        print('A Multiplicação é de ({} x {} = {}).'.format(n1, n2, soma))
        sleep(1)
    elif op == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
            sleep(1)
        else:
            print('O maior número é {}'.format(n2))
            sleep(1)
    elif op == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif op == 5:
        print('Você escolheu SAIR! Adeus.')
        exit()
    else:
        print('Opção Inválida!')