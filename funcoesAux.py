from sympy.ntheory import isprime
import numpy as np

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
		if(not isprime(int(p))):
			err += "p não é primo\n"
		if(not isprime(int(q))):
			err += "q não é primo\n"
		if(not mdc( int(e), (int(p)-1)*(int(q)-1) ) == 1):
			err += "e nao é coprimo a (p-1)(q-1)\n"
		return err


def extended_euclidean_algorithm(a, b, c=1):
    r = b % a

    if r == 0:
        return (c/a) % (b/a)

    return (extended_euclidean_algorithm(r, a, -c) * b + c) / (a % b)


def fast_modular_exponentiation(n, exp, mod):
	print("esperado o valor: " + str((n**exp)%mod))
	binary = []
	result = 1

	while exp > 0:
		binary.append(exp & 1)
		exp = exp >> 1

	array = np.zeros(len(binary),dtype='int64')
	array[0] = n%mod
	print(binary)
	for i in range(len(array)):
		if array[i] == 0:
			array[i] = (array[i-1]*array[i-1])%mod
	print(array)
	for i in range(len(binary)):
		if binary[i] == 1:
			result = result*array[i]
	print(result)
	return result%mod


def prime_factorization(n, idx):
	print(idx)
	result = []
	if n%2 == 0:
		result.append(2)
		if n/2 == 1:
			return result
		else:
			return result + prime_factorization(n / 2, idx+1)
	else:
		tmp = int(n)+1
		for i in range(3, tmp, 2):
			print(859832243-i)
			if n%i == 0:
				if isprime(i):
					result.append(i)
					if n/i == 1:
						return result
					else:
						return result + prime_factorization(n / i, idx+1)


def breaking_rsa(n, e, crypto):
	print("crypto: ", end="")
	print(crypto)
	decrypt = ""
	x = prime_factorization(n, 0)
	print("ffff")
	fi = (x[0]-1)*(x[1]-1)
	print("ffff")
	key = int(extended_euclidean_algorithm(e, fi))
	print("ffff")
	for i in crypto:
		c = chr(fast_modular_exponentiation(int(i), key, n) + 65)
		if(c == '['):
			decrypt += ' '
		else:
			decrypt += c
	print(decrypt)
	'''
    for l in crip:
    m = (int(l)**d)%( int(p.get())*int(q.get()) ) #aplicar a expo mod rapida
    if(m == 26):
        desenc.write(' ')
    else:
        desenc.write(chr(m+65))
    '''

	return decrypt