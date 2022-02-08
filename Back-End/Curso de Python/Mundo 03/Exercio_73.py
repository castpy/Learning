times = ("América-MG", "Athletico", "Atlético-GO", "Atlético-MG", "Avaí", "Botafogo", "Bragantino", "Ceará", "Corinthians", "Coritiba", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Juventude", "Internacional", "Palmeiras", "Santos", "São Paulo")


print('-'*50)
print(f'\033[34mLista de times do Brasileirão:\033[m\033[3m {times}\n')
print('-'*50)
print(f'\033[34mOs 5 primeiros são:\033[m {times[0:6]}\n')
print('-'*50)
print(f'\033[34mOs 4 ultimos são:\033[m {times[-4:]}\n')
print('-'*50)
print(f'\033[34mOs times na ordem alfabetica são:\033[m {sorted(times)}')