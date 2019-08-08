import tkinter as tk
from funcs import *

class option03(tk.Frame):
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
        
        plb = tk.Label(self, text="p:")
        plb.pack(side="top", fill="x")
        plb.place(x = 60, y = 65)

        p = tk.Entry(self)
        p.pack()
        p.place(x = 80, y = 65)

        qlb = tk.Label(self, text="q:")
        qlb.pack(side="top", fill="x")
        qlb.place(x = 60, y = 90)

        q = tk.Entry(self)
        q.pack()
        q.place(x = 80, y = 90)

        elb = tk.Label(self, text="e:")
        elb.pack(side="top", fill="x")
        elb.place(x = 60, y = 115)

        e = tk.Entry(self)
        e.pack()
        e.place(x = 80, y = 115)


        def descrip():
            print(p.get(), q.get(), e.get())

        okbtn = tk.Button(self, text="Descriptografar", command=descrip)
        okbtn.pack()
        okbtn.place(x=65, y=145)

        # retbtn = tk.Button(self, text="Voltar",
        #           command=lambda: master.switch_frame(StartPage))
        # retbtn.pack()
        # retbtn.place(x=170, y=145)