def degrau_2_frascos (x,n):
	raiz_n = pow(n,1.0/2)
	i = 0
	while i<n:		
		if i>=x :
			j = i-raiz_n
			while j<i:
				if j == x:
					return j
				j+=1
		i += int(raiz_n)
	return -1

def degrau_k_frascos(x,n,k):
	raiz_k = pow(n,1.0/k)
	inicio = 0
	fim = n
	incremento = pow(raiz_k,k-1)
	for i in range(k):
		j = inicio
		while j<fim:
			if j>=x:
				if incremento==1:
					return j
				inicio = j-incremento
				fim = j
				incremento = incremento / raiz_k
				break
			j+=incremento

nBits,nNumeros = input().split()
nBits = int(nBits)
nNumeros = int(nNumeros)
n = 2**nBits
for i in range(0,nNumeros,1):
	number = int(input(),2)
	print(str(number))
	resposta = degrau_k_frascos(number,n,8)
	if resposta != number:
		print ("Erro for ",str(number))


