#               Variaveis compostas com Listas
# Como vimos anteriormente, as tuplas são feitas com ()
# Mas as listas são feitas com []

#   As listas são mutaveis!!!!!!
# Ex:
lanche = ['Pizza', 'Suco', 'Pudin'] #Definimos uma lista que vamos mudar o valor 1
#         Valor:0 |Valor:1| Valor:2

lanche[1]='Pastel' #Indicamos que na posição 1, o valor será mudado para PASTEL
print(lanche)

# Para adicionar um valor na lista, podemos usa o comando .append() para adicionar elemento no final da lista

lanche.append('Misto quente')
print('Veja que adicionamos mais um valor à lista {}'.format(lanche))


# Se eu quiser adicionar um valor em qualquer posição da lista, basta usar o .insert()
lanche.insert(0, 'Pão') # Adicionamos o objeto PÃO antes de PIZZA
#           Poss | Lanche

print(f'Veja que a lista recebeu o valo PÃO antes de PIZZA\n{lanche}')

# Para remover um objeto pelo valor dado na lista, por exemplo: PASTEL está no indice 2
# Você pode usar o método del lanche[3]
# Ou usar o método lanche.pop(3)

# Para remover um objeto pelo nome na lista, por exemplo PASTEL
# Você pode usar o método lanche.remove('Pastel')

lanche.remove('Pastel')
print(lanche)

# Há uma função chamada list() que podemos usar no range() para gerar uma lista com os valores definidos
# Ex:
# valores = list(range(4,11)) -> Isso irá gerar uma lista com os valores 4...10, cada um com os indices de 0..6

valores = [0,1,2,3]

for c, v in enumerate(valores):
    print(f'Achei o valor {c} no indice {v}!')