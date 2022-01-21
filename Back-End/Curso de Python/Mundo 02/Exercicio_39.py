import datetime
data = datetime.date.today()

suaIdade = int(input('Digite sua idade: '))
anoAtual = data.year
anoAlistamento = anoAtual - suaIdade + 18

if anoAlistamento == anoAtual:
    print('Está na hora de você se alistar ao Exercito Brasileiro!')
elif anoAlistamento < anoAtual:
    print('Você já passou da hora de se alistar!')
    print('Passou {} anos do tempo.'.format(suaIdade - 18))
elif anoAlistamento > anoAtual:
    print('Você ainda não tem idade suficiente para se alistao ao Exercito Brasileiro!')
    print('Faltam {} anos para você se alistar'.format(18 - suaIdade))
else:
    print('Algo deu errado!')
    