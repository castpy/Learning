soma = cont = 0
while True:
    n1 = int(input('Digite um número [999 para parar]: '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
