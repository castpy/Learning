n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
n3 = int(input('Digite o 3º numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor número é {}'.format(menor))
