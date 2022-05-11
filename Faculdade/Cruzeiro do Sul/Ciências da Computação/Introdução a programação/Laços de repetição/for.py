

for cont in range(10): #definimos apenas um numero limite no range
    cont += 1 #adicionamos 1 a cada vez que a linha é interpretadad
    print(f"Olá, mundo! {cont}") #mostramos na tela  

print('='*10)

for cont in range(1,11,2): #definimos o INICIO - FIM - PASSO (ou seja, de dois em dois)
    cont += 1 #adicionamos 1 a cada vez que a linha é interpretadad
    print(f"Olá, mundo! {cont}") #mostramos na tela 

print('=' * 5,'Desafio','=' * 5)

print('''
Faça um programa que imprima os números de 0 a 10 
em ordem decrescente. Use como base o primeiro exemplo.
''')

for cont in range(10, 0, -1): 
    #Definimos o inicio em 10, e o fim em 1, e tiramos 1 de 10 a cada vez executado, até chegar em 1. (O indice 0 é o 1ª objeto, no caso de uma sequencia numérica, o nosso indice 0 é o número 1).
    cont +1
    print(f'Decrescente {cont}')