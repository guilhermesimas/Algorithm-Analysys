import sys
import math

""" Classe para representar um item """
class Item():
    def __init__(self, num, value, weight, valueWt, selectedWt):
        self.value = value
        self.weight = weight
        self.valueWt = valueWt
        self.num = num
        self.selectedWt = selectedWt

    def __repr__(self):
        return "Item(num={3:6}, value={0:5}, weight={1:5}, valueWt={2:7}, selectedWt={4:5})".format(self.value, self.weight, self.valueWt, self.num, self.selectedWt)

""" Algoritmo do problema 2.1 """
def mochila_frac1(items, capacity):
    # ordena lista decrescentemente por valor/peso
    items = mergesort(items, inverse_valueWtComparison)
    sumWeight = 0
    sumValue = 0

    #adiona item a item se cabe na mochila
    for item in items:
        if sumWeight == capacity:
            return

        if item.weight + sumWeight < capacity:
            item.selectedWt = item.weight
            sumWeight += item.weight
        else:
            item.selectedWt = capacity - sumWeight
            sumWeight += (capacity - sumWeight)

    return

""" Algoritmo do problema 2.2 """
def mochila_frac2(items, capacity):
    mochila_frac2_rec(items, capacity)
    return

def mochila_frac2_rec(items, capacity):
    # condicao de parada
    if len(items) == 1:
        if items[0].weight >= capacity:
            items[0].selectedWt = capacity
        else:
            items[0].selectedWt = items[0].weight
        return

    # determina item mediano e particiona ao redor dele
    middle = math.ceil(len(items)/2)
    medianValueWtItem = kthValue(items, middle, valueWtComparison)
    medianValueWtIdx = items.index(medianValueWtItem)
    partitionIdx = partition(items, medianValueWtIdx, inverse_valueWtComparison)

    # calcula peso da metade mais valiosa
    sumWeight = sum([x.weight for x in items[:middle]])

    # se nao cabe tudo, repete-se algoritmo na metade mais valiosa
    if sumWeight > capacity:
        mochila_frac2_rec(items[:middle], capacity)
    # se cabe tudo, poe metade mais valiosa na mochila e repete-se algoritmo na 
    # metade menos valiosa
    else:
        for i in range(middle):
            items[i].selectedWt = items[i].weight
        mochila_frac2_rec(items[middle:], capacity-sumWeight)

    return

""" Algoritmo do problema 2.3 """
def mochila_frac3(items, capacity):
    mochila_frac3_rec(items, capacity)
    return
        
def mochila_frac3_rec(items, capacity):
    # condicao de parada
    if len(items) == 1:
        if items[0].weight >= capacity:
            items[0].selectedWt = capacity
        else:
            items[0].selectedWt = items[0].weight
        return

    # calcula-se media do valor/peso e particiona-se ao redor desse valor
    # particionamento poe maiores na primeira metade
    averageValueWt = sum(x.valueWt for x in items) / len(items)
    firstSmallerIndx = inverse_partitionByValue(items, averageValueWt)

    # calcula-se peso da metade mais valiosa
    sumWeight = sum([x.weight for x in items[:firstSmallerIndx]])

    # se nao cabe tudo, repete-se algoritmo na metade mais valiosa
    if sumWeight > capacity:
        mochila_frac3_rec(items[:firstSmallerIndx], capacity)
    # se cabe tudo, poe metade mais valiosa na mochila e repete-se algoritmo na 
    # metade menos valiosa
    else:
        for i in range(firstSmallerIndx):
            items[i].selectedWt = items[i].weight
        mochila_frac3_rec(items[firstSmallerIndx:], capacity-sumWeight)

    return


""" Achar o kesimo objeto de uma lista de acordo com uma funcao de comparacao
Retorna o objeto correspondete ao kesimo valor """
def kthValue(items, k, comparisonFunction):
    # a partir de tamanho 5, ordenar e retornar valor do meio
    if len(items) <= 5:
        sortedSubArray = mergesort(items,comparisonFunction)
        return sortedSubArray[k-1]

    # dividir em subListas de tamanho 5, ordenalas e retornar sua mediana
    medians = []
    for i in range(0, len(items), 5):
        sortedSubArray = mergesort(items[i:i+5],comparisonFunction)
        medians.append(sortedSubArray[int(len(sortedSubArray)/2)])

    # achar mediana das medianas e particionar ao redor desse valor
    pivot = kthValue(medians,int(len(medians)/2), comparisonFunction)
    pivotIdx = items.index(pivot)
    pivotIdx = partition(items, pivotIdx, comparisonFunction)
    p = pivotIdx+1

    # terminar ou continuar busca em uma das metades
    if k == p:
        return items[pivotIdx]
    if k < p:
        return kthValue(items[0:pivotIdx], k, comparisonFunction)
    if k > p:
        return kthValue(items[pivotIdx+1:len(items)], k-p, comparisonFunction)


""" Particionar lista ao redor de um indice usando funcao de comparacao
Particiona in-place
Retorna o indice em que o elemento pivo terminou """
def partition(items, pivotIdx, comparisonFunction):
    sameValue = 0
    i = 0

    # colocar pivot no final
    pivotObj = items[pivotIdx]
    items[pivotIdx] = items[len(items)-1]
    items[len(items)-1] = pivotObj

    # percorrer lista com 2 indices
    # i aponta para primeiro elemento do segundo grupo
    # j aponta para primeiro elemento do grupo desconhecido
    for j in range(len(items)-1):
        if comparisonFunction(items[j], pivotObj) < 0:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1

        # assegurar de nao desbalancear particionamento por valores iguais
        elif comparisonFunction(items[j], pivotObj) == 0:
            if sameValue%2 == 0:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
                i += 1
            sameValue += 1

    # por pivot no devido lugar
    temp = items[i]
    items[i] = pivotObj
    items[len(items)-1] = temp

    return i

""" Particiona lista ao redor de um valor nao necessariamente presente nela
Particiona in-place
Retorna indice em que se encontra o primeiro valor menor que o dado """
def inverse_partitionByValue(items, averageValueWt):
    sameValue = 0
    i = 0

    # percorrer lista com 2 indices
    # i aponta para primeiro elemento do segundo grupo
    # j aponta para primeiro elemento do grupo desconhecido
    for j in range(len(items)):
        # assegurar de nao desbalancear particionamento por valores iguais
        # evitar erro de precisao de floats
        if abs(items[j].valueWt - averageValueWt) <= .5e-9:
            if sameValue%2 == 0:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
                i += 1
            sameValue += 1

        elif items[j].valueWt > averageValueWt:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1
    return i

""" Funcao que dado Item A e B, realiza a comparacao do valor por peso desses """
def valueWtComparison(a, b):
    # evitar erro de precisao de floats
    if abs(a.valueWt - b.valueWt) <=  .5e-9:
        return 0
    if a.valueWt > b.valueWt:
        return 1
    if a.valueWt < b.valueWt:
        return -1

""" Compara dois Items por valor por peso ao inverso """
def inverse_valueWtComparison(a, b):
    return -1 * valueWtComparison(a, b)


""" Merge sorted
Retorna lista ordenada """
def mergesort(x, comparisonFunction):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle], comparisonFunction)
        b = mergesort(x[middle:], comparisonFunction)
        return merge(a,b, comparisonFunction)

""" Subrotina de merge """
def merge(a,b, comparisonFunction):
    c = []
    while len(a) != 0 and len(b) != 0:
        if comparisonFunction(a[0], b[0]) <= 0:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

""" Le um arquivo no formato de um problema da mochila especificado dado sua path
Retorna a lista de Items e a capacidade da mochila """
def readFile(filepath):
    f = open(filepath)
    nItems = int(f.readline())

    items = []

    for i in range(nItems):
        num, value, weight = f.readline().split()
        items.append(Item(int(num), int(value), int(weight), float(value)/float(weight), 0))

    capacity = int(f.readline())

    return items, capacity

""" Funcao main para rodar um algoritmo sobre um arquivo especificado
Argumentos sao passaos por linha de comando """
def main():
    if len(sys.argv) != 3:
        print("!Uso: problema_mochila.py {filepath} {numero algoritmo}")
        return
    
    script, filename, algorithm = sys.argv
    items, capacity = readFile(filename)

    algorithm = int(algorithm)

    if algorithm == 1:
        mochila_frac1(items, capacity)
    elif algorithm == 2:
        mochila_frac2(items, capacity)
    elif algorithm == 3:
        mochila_frac3(items, capacity)

    for item in [x for x in items if x.selectedWt != 0]:
        print("{}".format(item))
    print("selectedWt: {0}".format(sum([x.selectedWt for x in items])))
    print("capacity: {0}".format(capacity))
    print("totalWt: {0}".format(sum([x.weight for x in items])))
    

if __name__ == "__main__":
    main()


""" Funcoes para auxilio de debug """
def intcomparison (a, b):
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

def inverse_intcomparison (a, b):
    return -1 * intcomparison (a, b)