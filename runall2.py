# from __future__ import print_function
import os
import copy
import num2
import re
import time

PATH = "Mochila-Insts\instancias\\"
filenames = []
times = [[],[],[]]

def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]


for file in os.listdir(PATH):
    if file.endswith(".in"):
        filenames.append(file)
filenames.sort(key=natural_key)

print("{0:11}: {1:10.7} | {2:10.7} | {3:10.7}".format("file", "algo1", "algo2", "algo3"))
for name in filenames:
    items1, capacity = num2.readFile(PATH + name)
    items2 = copy.deepcopy(items1)
    items3 = copy.deepcopy(items1)

    start = time.process_time()
    num2.mochila_frac1(items1, capacity)
    end = time.process_time()
    times[0].append(end - start)


    start = time.process_time()
    num2.mochila_frac2(items2, capacity)
    end = time.process_time()
    times[1].append(end - start)


    start = time.process_time()
    num2.mochila_frac3(items3, capacity)
    end = time.process_time()
    times[2].append(end - start)

    items1.sort(key=lambda item: item.num)
    items2.sort(key=lambda item: item.num)
    items3.sort(key=lambda item: item.num)

    for i in range(len(items1)):
        if items1[i].num != items2[i].num or items1[i].num != items3[i].num:
            print("lista de items nao ordenada corretamente")
            break
        if items1[i].selectedWt != items2[i].selectedWt or items1[i].selectedWt != items3[i].selectedWt:
            print("Peso selecionado diferente pra item {0}, no arquivo {1}".format(items1[i].num, name), end="")
            # print("algo1: {0}, algo2: {1}, algo3: {2}".format(items1[i].selectedWt, items2[i].selectedWt, items3[i].selectedWt))
            print("\nalgo1: {0}".format(items1[i]))
            print("algo2: {0}".format(items2[i]))
            print("algo3: {0}".format(items3[i]))


    print("{0:11}: {1:10.7} | {2:10.7} | {3:10.7}".format(name, times[0][-1], times[1][-1], times[2][-1]))

print("Algoritmos rodados para todos os arquivos")
