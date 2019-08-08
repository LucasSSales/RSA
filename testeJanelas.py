#!/usr/bin/env python3

import tkinter as tk
from funcs import *
from functools import partial
from gerarChavePublica import PageOne
from criptografar import PageTwo
from descriptografar import option03

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        print(isinstance(new_frame, StartPage))
        
        if(not isinstance(new_frame, StartPage)):
            retbtn = tk.Button(self, text="Voltar",
                  command=lambda: self.switch_frame(StartPage))
            retbtn.pack()
            retbtn.place(x=280, y=200)
        


class StartPage(tk.Frame):
    def __init__(self, master):
        h = 100
        tk.Frame.__init__(self, master)

        lb = tk.Label(self, text="Criptografia RSA",
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="Projeto de Matematica Discreta", 
            font =('Verdana', 11)).pack(side="top", fill="x")   
        tk.Label(self, text="EQUIPE: Lucas Sales, Jadson Crislan, Kelly Bianca, Thiago Henrique", 
            font =('Verdana', 8)).pack(side="top", fill="x")         
        lb = tk.Label(self, text="", font =('Verdana', 80)).pack(side="top", fill="x")
        lb = tk.Label(self, text="", font =('Verdana', 22)).pack(side="top", fill="x")
        lb = tk.Label(self, text="", font =('Verdana', 22)).pack(side="top", fill="x")
        
        #Botao "gerar chave publica"
        btn01 = tk.Button(self, text="Gerar chave publica",
                  command=lambda: master.switch_frame(PageOne))
        btn01.pack()
        btn01.place(x = 35, y = h)

        #Botao "Criptografar"
        btn02 = tk.Button(self, text="Criptografar",
                  command=lambda: master.switch_frame(PageTwo))
        btn02.pack()
        btn02.place(x = 165, y = h)

        #Botao "Descriptografar"
        btn03 = tk.Button(self, text="Descriptografar",
                  command=lambda: master.switch_frame(option03))
        btn03.pack()
        btn03.place(x = 260, y = h)

        #Botao "Botão Misterioso"
        btn04 = tk.Button(self, text="Botão Misterioso",
                  command=lambda: master.switch_frame(option04))
        btn04.pack()
        btn04.place(x=150, y = h+50)





        






class option04(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Em desenvolvimento", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 10)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")
        tk.Label(self, text="", 
            font =('Verdana', 22)).pack(side="top", fill="x")

        # retbtn = tk.Button(self, text="Voltar",
        #           command=lambda: master.switch_frame(StartPage))
        # retbtn.pack()
        # retbtn.place(x=190, y=145)
        



if __name__ == "__main__":
    app = SampleApp()
    app.title("RSA")
    app.geometry("500x250")
    app.mainloop()
