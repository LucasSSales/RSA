import tkinter as tk
from funcoesAux import *
from Inverso import inversoModular
import tkinter.messagebox
import os

class Option04(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Opção Misteriosa", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 10)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")   

        pubKeylb = tk.Label(self, text="Chave Publica:")
        pubKeylb.pack(side="top", fill="x")
        pubKeylb.place(x = 10, y = 60)

        pubKey = tk.Entry(self)
        pubKey.pack()
        pubKey.place(x = 100, y = 60)
        

        def breaker():
            #log de erros e lista de substrings para validacao
            err, titulo = "", "ERRO!"
            #validacao da chave inserida
            pk = pubKey.get().split()
            if(len(pk)!=2 or not str(pk[0]).isnumeric() or not str(pk[1]).isnumeric()):
                err+="Chave pública Inválida"
            if(err == ""):
                #lendo a mensagem encriptada caso exista
                if os.path.exists("mensagemCriptografada.txt"):
                    file = open("mensagemCriptografada.txt", "r")
                    crip = file.read().split()
                    file.close()
                else:
                    tkinter.messagebox.showinfo("ERRO!", "Não há mensagem para ser descriptografada")
                    return
                #caso ja exista o arquivo, remove
                if os.path.exists("hacks.txt"):
                    os.remove("hacks.txt")
                #criando novo arquivo para mensagem
                desenc = open("hacks.txt", "w")
                desenc.write(breaking_rsa(int(pk[0]), int(pk[1]), crip))
                desenc.close()
                err = "CRIPTOGRAFIA QUEBRADA MUAHAHAHAHA"
                titulo = "#hacks"
            tkinter.messagebox.showinfo(titulo, err) #alerta de sucesso ou falha

        okbtn = tk.Button(self, text="CLIQUE E DESCUBRA :)", command=breaker)
        okbtn.pack(); okbtn.place(x=65, y=100)