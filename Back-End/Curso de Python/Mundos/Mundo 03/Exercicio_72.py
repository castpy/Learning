texto = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'Seis', 'sete', 'oito', 'Nove', 'dez', 'onze', 'doze', 'trese', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    op = int(input('Digite um número de 0 a 20: '))
    if op >= 0 and op < 21:
        print('Você digitou {}'.format(texto[op]))
        break
    else:    
        print('\033[31mDigite um número válido!\033[m')
        continue