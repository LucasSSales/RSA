#a^b mod m
def expModRapida(a, b, m):
	if(b%2==0):
		print("ver dps")
	else:
		binario = (bin(b)[2:])[::-1]
		expo = []
		for i in range(len(binario)):
			if(binario[i]=='1'):
				expo.append(2**i)
		

