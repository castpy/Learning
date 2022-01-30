n1 = cont = soma = 0
n1 = int(input('Digite um número [999 para parar]: '))
while n1 != 999:
    cont += 1
    soma += n1
    n1 = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
