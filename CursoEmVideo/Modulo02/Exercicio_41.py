idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade >= 10 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
elif idade > 20:
    print('Sua categoria é MASTER')
