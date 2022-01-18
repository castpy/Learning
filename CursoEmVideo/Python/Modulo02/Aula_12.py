nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Olá, Gustavo!')
elif nome == 'Marcus':
    print('Olá, Marcus!')
else:
    print('Olá, {}!'.format(nome))