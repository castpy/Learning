from time import sleep
import datetime
data = datetime.date.today()
ano = data.year
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Bem vindo ao ano novo! Feliz {}'.format(ano))
