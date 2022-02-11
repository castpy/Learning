from random import randint
num = (randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6))
print('Os números sorteados foram ', end="")
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número é {max(num)}\nO menor número é {min(num)}')