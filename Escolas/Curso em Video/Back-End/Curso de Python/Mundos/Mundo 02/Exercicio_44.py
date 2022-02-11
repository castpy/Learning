Vproduto = float(input('Valor do produto: '))
op = int(input('''
[1] Dinheiro/Cheque
[2] Cartão - à vista
[3] Cartão - até 2x
[4] Cartão - 3x ou mais

-> '''))

if op == 1:
    desconto = Vproduto - (Vproduto * 10 / 100)
    print('Com esse método de pagamento, o produto terá um desconto de 10%.')
    print('Total: R${:.2f}'.format(desconto))
elif op == 2:
    desconto = Vproduto - (Vproduto * 5 / 100)
    print('Com esse método de pagamento, o produto terá um desconto de 5%.')
    print('Total: R${:.2f}'.format(desconto))
elif op == 3:
    print('Com esse método de pagamento, o valor do produto será o mesmo.')
    print('Total: R${:.2f}'.format(Vproduto))
elif op == 4:
    juros = Vproduto + (Vproduto * 20 / 100)
    print('Com esse método de pagamento, o produto terá um juros de 20%.')
    print('Total: R${:.2f}'.format(juros))
    