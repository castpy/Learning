n1 = float(input('Qual seu salario? R$:'))
reajuste = n1 + (n1 * 15 / 100)
print('O seu salario é de R${0:.2f} e com o reajuste será R${1:.2f}'.format(n1, reajuste))