total = maisDeMil = maisBarato = cont = 0
nomeMaisBarato = ''

while True:
    print('-'*30)
    print(' '*5, '\033[32mLOJÃO SUPER BARATO\033[m')
    print('-'*30)

    produto = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço do Produto: R$: '))
    cont += 1
    total += preco
    if preco > 1000:
        maisDeMil += 1 
    if cont == 1:
        maisBarato = preco
        nomeMaisBarato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeMaisBarato = produto

    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break

print('\n#'*30, 'Caixa Final', "#"*30)
print(f'O total da compra foi {total:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa {maisBarato:.2f}')