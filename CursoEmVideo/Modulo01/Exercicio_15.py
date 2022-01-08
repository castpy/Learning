km = float(input('Quantos KM/h foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
soma = (dias * 60) + (km * 0.15)
print('O carro foi alugado por {} dias e percorreu um total de {} KM/h.'.format(dias, km))
print('O total a ser pago é R${:.2f}'.format(soma))

