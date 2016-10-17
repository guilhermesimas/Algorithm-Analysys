#!/bin/bash
# Script para o T1 de Compiladores

rm log.txt
echo -e "T1-AA\tGuilherme Simas\t1311812" >>log.txt
echo -e "\tLucas Borges\t1311812" >>log.txt
echo -e "\tClara Szwarcman\t1311812" >>log.txt
echo "" >>log.txt
echo "========= 32 bits ==========">>log.txt
for file in ../input/bignum_32*; do
	python3 num1.py $file 1 >>log.txt
	python3 num1.py $file 2 >>log.txt
	python3 num1.py $file 4 >>log.txt
	python3 num1.py $file 8 >>log.txt
	python3 num1.py $file 16 >>log.txt
	python3 num1.py $file 32 >>log.txt
done
echo "========= 64 bits ==========">>log.txt
for file in ../input/bignum_64*; do
	python3 num1.py $file 2 >>log.txt
	python3 num1.py $file 4 >>log.txt
	python3 num1.py $file 8 >>log.txt
	python3 num1.py $file 16 >>log.txt
	python3 num1.py $file 32 >>log.txt
done
echo "========= 128 bits ==========">>log.txt
for file in ../input/bignum_128*; do
	python3 num1.py $file 4 >>log.txt
	python3 num1.py $file 8 >>log.txt
	python3 num1.py $file 16 >>log.txt
	python3 num1.py $file 32 >>log.txt
done
echo "========= 192 bits ==========">>log.txt
for file in ../input/bignum_192*; do
	python3 num1.py $file 8 >>log.txt
	python3 num1.py $file 16 >>log.txt
	python3 num1.py $file 32 >>log.txt
done
echo "========= 256 bits ==========">>log.txt
for file in ../input/bignum_256*; do
	python3 num1.py $file 8 >>log.txt
	python3 num1.py $file 16 >>log.txt
	python3 num1.py $file 32 >>log.txt
done

