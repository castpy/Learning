n1 = float(input('Sua primeira nota: '))
n2 = float(input('Sua segunda  nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você está reprovado! Sua média foi de {}'.format(media))
elif 7 > media >= 5:
    print('Você está de recuperação! Sua média foi de {}'.format(media))
elif media >= 7:
    print('Parabéns, você está aprovado! Sua média foi de {}'.format(media))
else:
    print('Algo deu errado!')