#!/usr/bin/env python3
#codigo de base para interface retirado do stack overflow
#creditar caso encontre o link

import tkinter as tk
from gerarChavePublica import Option01
from criptografar import Option02
from descriptografar import Option03
from botaoMisterioso import Option04


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
        #para nao exibir o botao voltar na pagina de inicio
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
                  command=lambda: master.switch_frame(Option01))
        btn01.pack(); btn01.place(x = 35, y = h)
        #Botao "Criptografar"
        btn02 = tk.Button(self, text="Criptografar",
                  command=lambda: master.switch_frame(Option02))
        btn02.pack(); btn02.place(x = 165, y = h)
        #Botao "Descriptografar"
        btn03 = tk.Button(self, text="Descriptografar",
                  command=lambda: master.switch_frame(Option03))
        btn03.pack(); btn03.place(x = 260, y = h)
        #Botao "Botão Misterioso"
        btn04 = tk.Button(self, text="Botão Misterioso",
                  command=lambda: master.switch_frame(Option04))
        btn04.pack(); btn04.place(x=150, y = h+50)


if __name__ == "__main__":
    app = SampleApp()
    app.title("RSA")
    app.geometry("500x250")
    app.mainloop()
