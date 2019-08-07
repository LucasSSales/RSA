# Multi-frame tkinter application v2.3
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

        #janela.title("RSA")
        #janela["bg"] = "red"
        #Label(janela, text="hello world!").pack()
        #LarguraxAltura+Esquerda+Topo
        #janela.geometry("800x500")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        #self._frame["bg"] = "red"

class StartPage(tk.Frame):
    def __init__(self, master):
        h = 100
        tk.Frame.__init__(self, master, {"bg": "blue"})
        #tk.Frame.geometry("800x500")
        #tk.Frame["height"] = 500

        lb = tk.Label(self, text="Projeto de Matematica Discreta",
            font =('Verdana', 22)).pack(side="top", fill="x")
        lb = tk.Label(self, text="",
            font =('Verdana', 22)).pack(side="top", fill="x")
        lb = tk.Label(self, text="",
            font =('Verdana', 22)).pack(side="top", fill="x")
        lb = tk.Label(self, text="",
            font =('Verdana', 22)).pack(side="top", fill="x")
        
        #Botao "gerar chave publica"
        btn01 = tk.Button(self, text="Gerar chave publica",
                  command=lambda: master.switch_frame(PageOne))
        btn01.pack()
        btn01.place(x = 10, y = h)
        #btn01.grid(row=1, column=0)

        #Botao "Criptografar"
        btn02 = tk.Button(self, text="Criptografar",
                  command=lambda: master.switch_frame(PageTwo))
        btn02.pack()
        btn02.place(x = 140, y = h)

        #Botao "Descriptografar"
        btn03 = tk.Button(self, text="Descriptografar",
                  command=lambda: master.switch_frame(option03))
        btn03.pack()
        btn03.place(x = 230, y = h)

        #Botao "Botão Misterioso"
        btn04 = tk.Button(self, text="Botão Misterioso",
                  command=lambda: master.switch_frame(PageTwo))
        btn04.pack()
        btn04.place(x=350, y = h)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Gerar Chave Pública", 
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


        def teste():
            print("teste")

        okbtn = tk.Button(self, text="Gerar chave",
                  command=lambda: master.switch_frame(StartPage))
        okbtn.pack()
        okbtn.place(x=95, y=145)

        retbtn = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage))
        retbtn.pack()
        retbtn.place(x=190, y=145)

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
        

        mensagem = tk.Entry(self)
        mensagem.pack(fill="x")
        mensagem.place(x = 100, y = 65)
        '''
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


        def teste():
            print("teste")
        '''

        okbtn = tk.Button(self, text="Criptografar",
                  command=lambda: master.switch_frame(StartPage))
        okbtn.pack()
        okbtn.place(x=95, y=145)

        retbtn = tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage))
        retbtn.pack()
        retbtn.place(x=190, y=145)

class option03(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Descriptografar").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.title("RSA")
    app.geometry("500x200")
    app.mainloop()