from tkinter import *
import tkinter.messagebox

def pqe(p, q, e):
	print(p,q,e)
	try:
		p1 = int(p)
	except:
		tkinter.messagebox.showinfo("teste", "Valores invalidos inseridos")



def isPrime(n):
	for i in range(2, n):
		if(n%i==0):
			return 0
	return 1


def mdc(a, b):
	if(a%b == 0):
		return b
	return mdc(b, a%b)