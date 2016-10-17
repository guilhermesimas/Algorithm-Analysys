#!/bin/bash
# Script para o T1 de Compiladores
clear
echo "T1-Compiladores	Guilherme Simas - 1311812"
echo ""
echo "Compiling program"
cd src
make
echo "Done"
echo ""
echo "--Testing correct cases--"
cd ..
for file in input/*.in; do
	name=`basename $file`
	name="${name%%.*}"
	echo "Running for $name"
	src/out <input/$name.in >output
	if [ -f gab/error.log ]; then
		echo "in file $file">>gab/error.log
	fi
	diff gab/$name.gab output > /dev/null
	if [ $? -ne 0 ]; then
		echo "FAILED, WRONG OUTPUT:"
		diff gab/$name.gab output
		break
	fi
	echo "SUCCESS"
	echo ""
done
echo "--Testing error cases--"
for file in input/*.errin; do
	name=`basename $file`
	name="${name%%.*}"
	echo "Running for $name"
	src/out <input/$name.errin 2>errout >output
	diff gab/$name.errgab errout > /dev/null
	if [ $? -ne 0 ]; then
		echo "FAILED, WRONG ERROR OUTPUT:"
		diff gab/$name.errgab errout
		break
	fi
	diff gab/$name.gab output > /dev/null
	if [ $? -ne 0 ]; then
		echo "FAILED, WRONG OUTPUT:"
		diff gab/$name.gab output
		break
	fi
	echo "SUCCESS"
	echo ""
done

echo "Cleaning up"
echo "."
cd src
make clean
echo "."
cd ..
rm output
echo "."
rm errout
echo "Done"

