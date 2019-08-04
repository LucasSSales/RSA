def gerarChavePublica(p, q, e):
	return (p*q, e)

def gerarChavePrivada(p, q, d):
	return (p*q, d)

def criptografar(char, publicKey):
	return (char**publicKey[1])%publicKey[0]

def descriptografar(char, privateKey):
	return (char**privateKey[1])%privateKey[0]
