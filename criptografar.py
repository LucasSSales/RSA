import tkinter as tk
from funcoesAux import *
import tkinter.messagebox
import os

class Option02(tk.Frame):
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

        def cripto():
            #log de erros e lista de substrings para validacao
            err, val = "", mensagem.get("1.0",'end-1c').split() 
            #verificando se a mensagem inserida e valida
            for m in val:
                if(not m.isalpha()):
                    err+= "Mensagem Inválida!\n"
                    break
            #validacao da chave inserida
            pk = pubKey.get().split()
            if(len(pk)!=2 or not str(pk[0]).isnumeric() or not str(pk[1]).isnumeric()):
                err+="Chave pública Inválida"
            #caso nenhum erro tenha sido detectado
            if err=="" :
                m = mensagem.get("1.0",'end-1c') #string da mensagem
                #caso ja exista o arquivo, remove
                if os.path.exists("mensagemCriptografada.txt"):
                    os.remove("mensagemCriptografada.txt")
                #cria o arquivo para a mensagem
                file = open("mensagemCriptografada.txt", "a")
                #percorre a mensagem e encripta cada letra
                for l in m:
                    c = ""
                    if(l == ' '):
                        c = ((26)**int(pk[1])%int(pk[0])) #aplicar a expo mod rapida
                    else:
                        c = ((ord(l.upper())-65)**int(pk[1])%int(pk[0])) #aplicar a expo mod rapida
                    file.write(str(c)  + " ")
                file.close()
                #alerta de sucesso
                tkinter.messagebox.showinfo("Concluído!", "Mensagem Criptografada")
            else:
                #alerta de falha
                tkinter.messagebox.showinfo("ERRO!", err)

        okbtn = tk.Button(self, text="Criptografar", command=cripto)
        okbtn.pack()
        okbtn.place(x=65, y=200)