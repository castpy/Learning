nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # com isso o nome ocupará 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # com isso o nome ocupará 20 caracteres a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # com isso o nome ocupará 20 caracteres a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # com isso o nome ocupará 20 caracteres centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) # com isso o nome ocupará 20 caracteres centralizado com sinais de igualdade em volta

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma dos numeros é {}'.format(n1 + n2))
print('A subtração dos numeros é {}'.format(n1 - n2))
print('A multiplicação dos numeros é {}'.format(n1 * n2))
print('A divisão dos numeros é {:.3f}'.format(n1 / n2))
print('A potenciação dos numeros é {}'.format(n1 ** n2))
print('A divisão inteira dos numero é {}'.format(n1 // n2))
print('O resto da divisão dos numeros é {}'.format(n1 % n2))