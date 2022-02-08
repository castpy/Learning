numero = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')

texto = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'Seis', 'sete', 'oito', 'Nove', 'dez', 'onze', 'doze', 'trese', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

condicao = ''
while condicao == '':
    op = int(input('Digite um número de 0 a 20: '))
    if op >= 0 and op < 21:
        print('Você digitou {}'.format(texto[op]))
        condicao = 'p'
    else:    
        print('\033[31mDigite um número válido!\033[m')
        continue
    