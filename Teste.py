from tkinter import *
#=========================
#Configurações da tela
tela = Tk()
tela.geometry('250x250')
tela.title('IMC')
#==========================
#Função de calculo
def imc():
    peso = float(ed1.get())
    altura = float(ed2.get())
    imc = peso / (altura ** 2)
    lb['text'] = imc

    if imc < 18.5:
        print('{:.1f} Você está a baixo do peso!'.format(imc))
    elif imc >= 18.5 and imc <= 25:
        print('{:.1f} Você está com o peso ideal!'.format(imc))
    elif imc >= 25 and imc <= 30:
        print('{:.1f} Você está com sobrepeso'.format(imc))
    elif imc >= 30 and imc <= 40:
        print('{:.1f} Você está com obesidade'.format(imc))
    elif imc > 40:
        print('{:.1f} Você está com obesidade mórbida'.format(imc))
#==========================
#Conteúdo da tela
ed1 = Entry(tela)
ed1.place(x=60, y=25)
ed2 = Entry(tela)
ed2.place(x=60, y=90)

bt = Button(tela, text='SOMAR', width=20, command=imc)
bt.place(x=45, y=130)

lb = Label(tela, text='Label1')
lb.place(x=20, y=180)
#============================
tela.mainloop()