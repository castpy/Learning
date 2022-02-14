valores = list()
for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {max(valores)} e está na posição {...}')
print(f'O menor valor é {min(valores)} e está na posição {...}')