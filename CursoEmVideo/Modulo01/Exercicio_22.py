nome = str(input('Digite seu nome completo: '))
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúscular é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(" ")))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
