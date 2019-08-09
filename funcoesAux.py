#funcao para averiguar primalidade de n
def isPrime(n):
	for i in range(2, n):
		if(n%i==0):
			return 0
	return 1

#calculo do mdc utilizando algoritmo de euclides
def mdc(a, b):
	if(a%b == 0):
		return b
	return mdc(b, a%b)

#validacao das entradas p, q, e nas telas de gerar chave publica e descriptografia
def pqeValidacao(p, q, e):
	if(not str(p).isnumeric() or not str(q).isnumeric() or not str(e).isnumeric()):
		return "Por favor, insira APENAS valores numericos"
	else:
		err =  ""
		titulo = "ERRO!"
		if(not isPrime(int(p))):
			err += "p não é primo\n"
		if(not isPrime(int(q))):
			err += "q não é primo\n"
		if(not mdc( int(e), (int(p)-1)*(int(q)-1) ) == 1):
			err += "e nao é coprimo a (p-1)(q-1)\n"
		return err