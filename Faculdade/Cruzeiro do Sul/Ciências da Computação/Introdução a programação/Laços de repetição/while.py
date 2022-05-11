nome = input('Qual seu nome? ')

while True:
    a = input(f'Olá {nome.upper()}! Para finalizar o script digite 0: ')
    if a == '0':
        print('Saindo...')
        break
    else: 
        continue