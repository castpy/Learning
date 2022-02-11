num = (
    int(input('Digite um número: ')), 
    int(input('Digite outro número: ')), 
    int(input('Digite mais um número: ')), 
    int(input('Digite o ultimo número: '))
)

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'A primeira aparição do valor 3 foi na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi achado em nenhuma posição.')
print('Os numeros pares são: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')