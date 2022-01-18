from datetime import datetime
dataAtual = datetime.today().year

contMaior = 0
contMenor = 0

for i in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    maiorIdade = dataAtual - nascimento
    if maiorIdade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print('''
Ao todo tivemos {} pessoas de maior idade
E tambem tivemos {} pessoas de menor idade
'''.format(contMaior, contMenor))
