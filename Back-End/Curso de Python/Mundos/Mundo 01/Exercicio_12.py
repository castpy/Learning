n1 = float(input('Qual o preço do produto? R$:'))
desconto = n1 - (n1 * 5 / 100)
print('O produto custava {0} e com desconto de 5%, ele custará {1:.2f}'.format(n1, desconto))