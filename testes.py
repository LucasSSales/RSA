#coding: utf-8

from Inverso import inversoModular
from functools import partial
import tkinter
import RSAopcoes as rsa

state = 0

'''def bt():
	print("funcao do bt")
	lb["text"] = "BT"
	lb["bg"] = "green"
'''

def teste(op):
	print("vai mudar para opcao " + str(op))
	lb["text"] = et.get()
	print(str(et.get()).isnumeric())

janela = tkinter.Tk()
janela.title("RSA")
janela["bg"] = "red"
#Label(janela, text="hello world!").pack()
#LarguraxAltura+Esquerda+Topo
janela.geometry("800x500")

op01 = tkinter.Button(janela, width=20, text="Gerar Chave Pública")
op01["command"] = partial(teste, 1)
op01.place(x="300", y="120")

op01 = tkinter.Button(janela, width=20, text="Gerar Chave Pública")
op01["command"] = partial(teste, 2)
op01.place(x="300", y="180")

et = tkinter.Entry(janela)
et.place(x="300", y="150")


lb = tkinter.Label(janela, text="Criptografia RSA")
lb.place(x="300", y="10")



janela.mainloop()

'''print("gggh")
n = int(input("n = "))
m = int(input("m = "))
print(inversoModular(n, m))'''