n1 = float(input('A quantos KM/H o carro estava? '))
if n1 >= 80:
    print('Você estava a {}KM/H.'.format(n1))
    print('Você foi multado em R${:.2f}'.format((n1 - 80) * 7))
