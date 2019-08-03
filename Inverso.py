#!/usr/bin/env python3

#dicionario com as equacoes de resto
restos = {} 

#mdc por euclides
def mdc(a, b):
	if(a%b == 0):
		return b
	if(a%b != a):
		#preenchendo o dicionario
		restos[a%b] = [1, a, -(a//b), b]
	return mdc(b, a%b)

#funcao de calcula o inverso de n mod m
#parametros: n (de quem eh o inverso) m (o valor do modulo)
def inversoModular(n, m):
	r = mdc(n, m)
	#caso os numeros sejam multiplos
	if(len(restos)==0):
		return
	#percorrendo tds itens do dicionario 
	for i in range(len(restos)):
		print(restos[r])
		#vendo se o ultimo item da lista eh uma chave
		if restos[r][3] in restos:
			#realizando a "substituicao" onde o ultimo item eh um dos restos
			#assim substituindo ele pela sua equacao e desenvolvendo
			#ate chegar numa combinacao de n e m
			restos[restos[r][3]][0] *= restos[r][2]
			restos[restos[r][3]][2] *= restos[r][2]
			add = restos[r][0]
			restos[r][0] = restos[restos[r][3]][0]
			restos[r][1] = restos[restos[r][3]][1]
			restos[r][2] = restos[restos[r][3]][2] + add
			restos[r][3] = restos[restos[r][3]][3]

	#retornando o coef do valor
	if(restos[r][1] == n):
		return  restos[r][0]%m
	if(restos[r][3] == n):
		return  restos[r][2]%m