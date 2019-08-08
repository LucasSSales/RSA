import tkinter as tk
from funcs import *
import tkinter.messagebox

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



        def cripto():
            err= "" #log de erros
            val = mensagem.get("1.0",'end-1c').split() #lista de substrings para validacao


            for m in val:
                if(not m.isalpha()):
                    err+= "Mensagem Inválida!\n"
                    break


            pk = pubKey.get().split()
            if(len(pk)!=2 or not str(pk[0]).isnumeric() or not str(pk[1]).isnumeric()):
                err+="Chave pública Inválida"
            

            if err=="" :
                m = mensagem.get("1.0",'end-1c') #string da mensagem
                file = open("mensagemCriptografada.txt", "w")
                #para cada letra na mensagem
                j = 
                for l in m:
                    if(l == ' '):
                        c = ((26)**int(pk[1])%int(pk[0]))
                    else:
                        c = ((ord(c.upper())-65)**int(pk[1])%int(pk[0]))

                    file.write(str(c)  + " ")
                    
                    #(char**publicKey[1])%publicKey[0]


                tkinter.messagebox.showinfo("Concluído!", "Mensagem Criptografada")
            else:
                tkinter.messagebox.showinfo("ERRO!", err)



        okbtn = tk.Button(self, text="Criptografar", command=cripto)
        okbtn.pack()
        okbtn.place(x=65, y=200)

        # retbtn = tk.Button(self, text="Voltar",
        #           command=lambda: master.switch_frame(StartPage))
        # retbtn.pack()
        # retbtn.place(x=160, y=200)