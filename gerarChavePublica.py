import tkinter as tk
from funcs import *
import tkinter.messagebox
from RSAopcoes import *

class PageOne(tk.Frame):
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
        
        plb = tk.Label(self, text="p:")
        plb.pack(side="top", fill="x")
        plb.place(x = 80, y = 65)

        p = tk.Entry(self)
        p.pack()
        p.place(x = 100, y = 65)

        qlb = tk.Label(self, text="q:")
        qlb.pack(side="top", fill="x")
        qlb.place(x = 80, y = 90)

        q = tk.Entry(self)
        q.pack()
        q.place(x = 100, y = 90)

        elb = tk.Label(self, text="e:")
        elb.pack(side="top", fill="x")
        elb.place(x = 80, y = 115)

        e = tk.Entry(self)
        e.pack()
        e.place(x = 100, y = 115)


        def gerar():
            if(not str(p.get()).isnumeric() or not str(q.get()).isnumeric() or not str(e.get()).isnumeric()):
                tkinter.messagebox.showinfo("teste", "por favor, insira valores numericos inteiros")
            else:
                err =  ""
                titulo = "ERRO!"
                print(int(p.get()), int(q.get()), int(e.get()))
                if(not isPrime(int(p.get()))):
                    err += "p não é primo\n"
                if(not isPrime(int(q.get()))):
                    err += "q não é primo\n"
                if(not mdc(int(e.get()), (int(p.get())-1)* (int(q.get()) -1)  ) == 1):
                    err += "e nao é coprimo a (p-1)(q-1)\n"

                if(err == ""):
                    err = "Chave Gerada com Sucesso!"
                    titulo = "Concluido"
                    file = open("chavePublica.txt", "w")
                    file.write(str(gerarChavePublica(int(p.get()), int(q.get()), int(e.get()))))
                    file.close()
                
                tkinter.messagebox.showinfo(titulo, err)


        okbtn = tk.Button(self, text="Gerar chave", command=gerar)
        okbtn.pack()
        okbtn.place(x=95, y=145)

        # retbtn = tk.Button(self, text="Voltar",
        #           command=lambda: master.switch_frame(StartPage))
        # retbtn.pack()
        # retbtn.place(x=190, y=145)