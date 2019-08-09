import tkinter as tk
from funcoesAux import *
import tkinter.messagebox
import os

class Option01(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Gerar chave publica", 
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
        plb.pack(); plb.place(x = 80, y = 65)
        qlb = tk.Label(self, text="q:")
        qlb.pack(); qlb.place(x = 80, y = 90)
        elb = tk.Label(self, text="e:")
        elb.pack(); elb.place(x = 80, y = 115)
        #campos para entrada dos valores d p, q, e
        p = tk.Entry(self)
        p.pack(); p.place(x = 100, y = 65)
        q = tk.Entry(self)
        q.pack(); q.place(x = 100, y = 90)
        e = tk.Entry(self)
        e.pack(); e.place(x = 100, y = 115)

        def gerar():
            #validando se as entradas sao numericas
            err, titulo = pqeValidacao(p.get(), q.get(), e.get()), "ERRO!"
            #se nenhum erro foi encontrado
            if(err == ""):
                #caso ja exista o arquivo, remove
                if os.path.exists("chavePublica.txt"):
                    os.remove("chavePublica.txt")
                #escrevendo em um arquivo a chave publica
                file = open("chavePublica.txt", "w")
                file.write(str( (int(p.get())*int(q.get()), int(e.get())) ))
                file.close()
                err = "Chave Gerada com Sucesso!"
                titulo = "Concluido"
            tkinter.messagebox.showinfo(titulo, err) #alerta que indica sucesso ou falha

        okbtn = tk.Button(self, text="Gerar chave", command=gerar)
        okbtn.pack()
        okbtn.place(x=95, y=145)