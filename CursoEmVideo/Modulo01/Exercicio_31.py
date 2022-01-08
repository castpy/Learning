distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    print('Sua viagem irá custar R${}'.format(distancia * 0.50))
if distancia > 200:
    print('Sua viagem irá custar R${}'.format(distancia * 0.45))