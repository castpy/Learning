n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos a cima PODEM formar triangulo')
else:
    print('Os segmentos a cima NÃO PODEM formar triangulo')
    