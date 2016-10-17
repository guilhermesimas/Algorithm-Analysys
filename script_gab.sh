#!/bin/bash
# Script para gerar os gabaritos
for file in input/*.in; do
	name=`basename $file`
	name="${name%%.*}"
	./src/out <$file >gab/$name.gab
done 
for file in input/*.errin; do
	name=`basename $file`
	name="${name%%.*}"
	./src/out <$file 2>gab/$name.errgab >gab/$name.gab
done 