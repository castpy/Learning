peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('{:.1f} Você está a baixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('{:.1f} Você está com o peso ideal!'.format(imc))
elif imc >= 25 and imc <= 30:
    print('{:.1f} Você está com sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('{:.1f} Você está com obesidade'.format(imc))
elif imc > 40:
    print('{:.1f} Você está com obesidade mórbida'.format(imc))
