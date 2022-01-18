frase = str(input('Digite uma frase: ')).upper()
print('A letra "A" aparece {} na frase;'.format(frase.count('A')))
print('A letra "A" aparece primeiramente na posição {} da frase;'.format(frase.find("A")+1))
print('A letra "A" aparece por ultimo na posição {} da frase.'.format(frase.rfind("A")+1))