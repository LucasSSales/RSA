from tkinter import *
import tkinter.messagebox

def pqe(p, q, e):
	print(p,q,e)
	try:
		p1 = int(p)
	except:
		tkinter.messagebox.showinfo("teste", "Valores invalidos inseridos")