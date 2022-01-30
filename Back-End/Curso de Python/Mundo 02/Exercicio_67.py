c = 0
while True:
    n1 = int(input('Digite um número para saber sua tabuada: '))
    if n1 < 0:
        break
    for i in range(1, 11):
        c += 1
        print(f'{n1} * {c} = {n1*c}')
        if c == 10:
            c = 0
print('Programa encerrado')