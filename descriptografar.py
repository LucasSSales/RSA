import tkinter as tk
from funcoesAux import *
from Inverso import inversoModular
import tkinter.messagebox
import os

class Option03(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Descriptografar", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="Insira os valores abaixo", 
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
        
        #labels p, q, e
        plb = tk.Label(self, text="p:")
        plb.pack(); plb.place(x = 60, y = 65)
        qlb = tk.Label(self, text="q:")
        qlb.pack(); qlb.place(x = 60, y = 90)
        elb = tk.Label(self, text="e:")
        elb.pack(); elb.place(x = 60, y = 115)
        #campos para entrada dos valores d p, q, e
        p = tk.Entry(self)
        p.pack(); p.place(x = 80, y = 65)
        q = tk.Entry(self)
        q.pack(); q.place(x = 80, y = 90)
        e = tk.Entry(self)
        e.pack(); e.place(x = 80, y = 115)

        def descrip():
            err, titulo = pqeValidacao(p.get(), q.get(), e.get()), "ERRO!"
            if(err == ""):
                #calculando d para gerar a chave privada (n, d)
                d = inversoModular(int(e.get()), (int(p.get())-1)* (int(q.get()) -1))
                #lendo a mensagem encriptada caso exista
                if os.path.exists("mensagemCriptografada.txt"):
                    file = open("mensagemCriptografada.txt", "r")
                    crip = file.read().split()
                    file.close()
                else:
                    tkinter.messagebox.showinfo("ERRO!", "Não há mensagem para ser descriptografada")
                    return
                #caso ja exista o arquivo, remove
                if os.path.exists("mensagemDescriptografada.txt"):
                    os.remove("mensagemDescriptografada.txt")
                #criando novo arquivo para mensagem
                desenc = open("mensagemDescriptografada.txt", "a")
                #para cada letra na mensagem encriptada
                for l in crip:
                    n = int(p.get())*int(q.get())
                    m = fast_modular_exponentiation(int(l), d, n) #aplicar a expo mod rapida

                    if(m == 26):
                        desenc.write(' ')
                    else:
                        desenc.write(chr(m+65))
                desenc.close()
                err = "Mensagem Descriptografada"
                titulo = "Concluido"
            tkinter.messagebox.showinfo(titulo, err) #alerta de sucesso ou falha

        okbtn = tk.Button(self, text="Descriptografar", command=descrip)
        okbtn.pack(); okbtn.place(x=65, y=145)