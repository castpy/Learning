#               Variaveis compostas (tuplas)
# As tuplas servem básicamente para atribuir mais de um valor a uma única variável.
# Até então, tinhamos aprendido somente um tipo de atribuir valor a uma variável. Era com variável simples

# Variáveis simples:
lanche01 = 'café'

# Temos três formas de fazer uma variável composta... Através de (TUPLAS, LISTAS e DICIONÁRIOS)
# Vamos ver como criar uma TUPLA

# OBS: As tuplas são imutaveis, ou seja, elas não tem como mudar o seu valor!
# As tuplas são feitas com parenteses ()

lanche = ('Nescal', 'Coxinha', 'Pão', 'Ovo')
print(lanche)
print(lanche[0])
print(lanche[1:4])
print(lanche[0:4:2])
print(lanche[-1])

print('='*10)
for c in lanche:
    print(c)
print('='*10)
for cont in range(len(lanche)):
    print(lanche[cont])