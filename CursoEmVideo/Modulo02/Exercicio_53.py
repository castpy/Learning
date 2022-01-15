frase = str(input('Digite uma frase: ')).strip().upper()
sep = frase.split()
jun = ''.join(sep)
inv = ''
for letras in range(len(jun) - 1, -1, -1):
    inv += jun[letras]
if inv == jun:
    print(jun, inv)
    print('Temos um PALINDROMO!')
else:
    print(jun, inv)
    print('Não é um palindromo')