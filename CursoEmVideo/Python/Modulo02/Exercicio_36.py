print('=' * 30)
print('Minha casa, sua vida! :)')
print('=' * 30)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
tempo = int(input('Quantidade de anos que deseja pagar: '))

prestacao = casa / (tempo * 12) 
porcentagem = (salario * 30 / 100)

if prestacao < porcentagem:
    print('Parabéns, sua compra foi aprovada.')
elif prestacao > porcentagem:
    print('Sinto muito, mas sua compra foi negada.')
else:
    print('Algo deu errado!')
    