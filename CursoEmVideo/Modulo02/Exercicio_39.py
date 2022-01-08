import datetime

suaIdade = int(input('Digite sua idade: '))
data = datetime.date.today()
anoAtual = data.year
anoAlistamento = anoAtual - suaIdade + 18

if anoAlistamento == anoAtual:
    print('Está na hora de você se alistar ao Exercito Brasileiro!')
elif anoAlistamento < anoAtual:
    print('Você já passou da hora de se alistar!')
    print('Passou {} anos do tempo.'.format(anoAlistamento))
elif anoAlistamento > anoAtual:
    print('Você ainda não tem idade suficiente para se alistao ao Exercito Brasileiro!')
else:
    print('Algo deu errado!')