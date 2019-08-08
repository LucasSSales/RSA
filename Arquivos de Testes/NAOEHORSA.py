# int isPrime(unsigned long long int v){
# 	int i;
# 	if(v < 25){
# 		if(v==2 || v==3 || v==5 || v==7 || v==11 || v==17 || v==19 || v==23){
# 			return 1;
# 		}else{
# 			return 0;
# 		}
# 	}
# 	for(i = 3; i <= sqrt(v); i += 2){
# 		if(v%i == 0){
# 			return 0;
# 		}
# 	}
# 	return 1;
# }

def isPrime(n):
	for i in range(2, n):
		if(n%i==0):
			return 0
	return 1



def mdc(a, b):
	if(a%b == 0):
		return b
	return mdc(b, a%b)

def generatePublicKey():
	p = int(input("Insira o p: "))
	if(not isPrime(p)):
		print("p nao eh primo")
	
	q = int(input("Insira o q: "))
	if(not isPrime(q)):
		print("q nao eh primo")

	e = int(input("Insira o e: "))
	n = p*q
	print("(" + str(n) + "," + str(e)+")")
	if(mdc(e, (p-1)*(q-1)) != 1):
		print("e nao eh coprimo a (p-1)*(q-1)")




print("escolha uma opcao:\n1- Gerar chave publica\n2- Criptografar\n3- Descriptografar\n4- QUEBRAR A CRIPTOGRAFIA MUAHAHAHAHAHAHAHAH #HACKS")
try:
	opcao = int(input())
	if(opcao == 1):
		generatePublicKey()
except:
	print("digite um numero")



