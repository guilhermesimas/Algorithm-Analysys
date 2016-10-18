import os
import copy
import num2
import re
import time
import math

""" PARAMETROS """
PATH = "Mochila-Insts\instancias\\"
N_EXECUTIONS_FACTOR = 1e5

""" Listas de dados """
filenames = []
nExecutions = {}
times = [[],[],[]]

""" Chave para ordernar por ordem natural """
def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

""" Econcontra arquivos de dados (m*.in) na PATH """
for file in os.listdir(PATH):
    if file.endswith(".in"):
        filenames.append(file)
filenames.sort(key=natural_key)

""" Determina quantas vezes rodar cada tamanho """
for name in filenames:
    a, b = name.split('.')
    nItems = int(a[1:])
    nExecutions[name] = math.ceil(N_EXECUTIONS_FACTOR/nItems)

""" Executa os 3 algoritmos guardando tempo de execucao em cada arquivo """
print("{0:11} ({4:^7} ) | {1:^16} | {2:^16} | {3:^16}".format("file", "cpu / algo1", "cpu / algo2", "cpu / algo3", "nExec"))
for name in filenames:
    n = nExecutions[name]
    items, capacity = num2.readFile(PATH + name)
    

    """ Tomada de tempo para algoritmo1 """
    # cria n copias dos dados lidos
    itemsV = []
    for i in range(n):
        itemsV.append(copy.deepcopy(items))

    # executa algorimo n vezes sobre cada copia dos dados lidos originalmente
    start = time.process_time()
    for i in range(n):
        num2.mochila_frac1(itemsV[i], capacity)
    end = time.process_time()

    times[0].append(end - start)
    value1 = sum(x.valueWt * x.selectedWt for x in itemsV[0] if x.selectedWt != 0)


    """ Tomada de tempo para algoritmo2 """
    # cria n copias dos dados lidos
    itemsV = []
    for i in range(n):
        itemsV.append(copy.deepcopy(items))

    # executa algorimo n vezes sobre cada copia dos dados lidos originalmente
    start = time.process_time()
    for i in range(n):
        num2.mochila_frac2(itemsV[i], capacity)
    end = time.process_time()

    times[1].append(end - start)
    value2 = sum(x.valueWt * x.selectedWt for x in itemsV[0] if x.selectedWt != 0)


    """ Tomada de tempo para algoritmo3 """
    # cria n copias dos dados lidos
    itemsV = []
    for i in range(n):
        itemsV.append(copy.deepcopy(items))

    # executa algorimo n vezes sobre cada copia dos dados lidos originalmente
    start = time.process_time()
    for i in range(n):
        num2.mochila_frac3(itemsV[i], capacity)
    end = time.process_time()

    times[2].append(end - start)
    value3 = sum(x.valueWt * x.selectedWt for x in itemsV[0] if x.selectedWt != 0)


    """ Confere se o valor contido na mochila e o mesmo para cada algoritmo """
    if value1 != value2 or value1 != value3:
            print("Valor da mochila diferente para arquivo {}".format(name))
            print("  algo1: {0}".format(value1))
            print("  algo2: {0}".format(value2))
            print("  algo3: {0}".format(value3))

    """ Imprime tempo por chamada para cada algoritmo """
    print("{0:11} ({4:7} ) | {1:^16.8f} | {2:^16.8f} | {3:^16.8f}".format(name, times[0][-1]/n, times[1][-1]/n, times[2][-1]/n, n))

print("Algoritmos executados sobre todos os arquivos")