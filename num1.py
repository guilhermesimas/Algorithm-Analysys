from __future__ import print_function
import time
import ntpath
import sys

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
#Lembrar de mudar para abrir arquivo


def degrau_k_frascos(x,n,k):
	raiz_k = pow(n,1.0/k)
	inicio = 0
	fim = n
	incremento = int(pow(raiz_k,k-1))
	i=0
	while i<k:
		j = inicio	
		while j<=fim:
			if j>=x:				
				if incremento<2:
					return j
				inicio = j-incremento
				fim = j
				incremento = int(incremento / raiz_k)
				break
			j+=incremento
		i+=1
	return -1

def path_leaf(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def main():
	if len(sys.argv) != 3:
		print("num1.py {fileName} {nFrascos}")
		return
	script,fileName,nFrascos = sys.argv

	f = open(fileName)

	nFrascos = int(nFrascos)

	nBits,nNumeros = f.readline().split()
	nBits = int(nBits)
	nNumeros = int(nNumeros)

	print("===========================================================")

	print("Running for \""+path_leaf(fileName)+"\"")

	print("DEGRAUS<2^"+str(nBits)+">\t FRASCOS<"+str(nFrascos)+">")

	n = 2**nBits
	number = []
	#timing reading input
	timeInput = time.clock()
	for i in range(0,nNumeros,1):
		number.append( int(f.readline(),2) )
	#end timing reading input
	timeInput = time.clock() - timeInput
	timeLoop = time.clock()
	#timing algorithm
	for i in range(nNumeros):
		#number = int(input(),2)
		#print(str(i*100/nNumeros)+"%")
		resposta = degrau_k_frascos(number[i],n,nFrascos)
		if resposta != number[i]:
			print ("Erro: "+str(resposta))
	#end timing algorithm
	timeLoop = time.clock() - timeLoop
	print("Time reading input <"+str(timeInput*1000)+"ms>")
	print("Total time for algorithm <"+str(timeLoop*1000)+"ms>")
	print("Time per iteration <"+str(timeLoop*1000/nNumeros)+"ms>")

if __name__ == '__main__':
	main()


