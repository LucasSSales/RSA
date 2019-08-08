import tkinter as tk
from funcs import *

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Criptografar", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="Insira a mensagem no campo abaixo", 
            font =('Verdana', 10)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        

        mensagem = tk.Text(self, height=6, width=30)
        mensagem.pack(fill="x")
        mensagem.place(x = 1, y = 65)

        pubKeylb = tk.Label(self, text="Chave Publica:")
        pubKeylb.pack(side="top", fill="x")
        pubKeylb.place(x = 10, y = 175)

        pubKey = tk.Entry(self)
        pubKey.pack()
        pubKey.place(x = 100, y = 175)



        def teste():
            m = mensagem.get("1.0",'end-1c')
            pk = pubKey.get()
            print(m, pk)

        okbtn = tk.Button(self, text="Criptografar", command=teste)
        okbtn.pack()
        okbtn.place(x=65, y=200)

        # retbtn = tk.Button(self, text="Voltar",
        #           command=lambda: master.switch_frame(StartPage))
        # retbtn.pack()
        # retbtn.place(x=160, y=200)