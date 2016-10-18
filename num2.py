# from __future__ import print_function
import sys
import math

class Item():
    def __init__(self, num, value, weight, valueWt, selectedWt):
        self.value = value
        self.weight = weight
        self.valueWt = valueWt
        self.num = num
        self.selectedWt = selectedWt

    def __repr__(self):
        return "Item(num={3:6}, value={0:5}, weight={1:5}, valueWt={2:7}, selectedWt={4:5})".format(self.value, self.weight, self.valueWt, self.num, self.selectedWt)

def mochila_frac1(items, capacity):
    items = mergesort(items, inverse_valueWtComparison)
    sumWeight = 0
    sumValue = 0

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

def mochila_frac2(items, capacity):
    mochila_frac2_rec(items, capacity)
    return

def mochila_frac2_rec(items, capacity):
    if len(items) == 1:
        if items[0].weight >= capacity:
            items[0].selectedWt = capacity
        else:
            items[0].selectedWt = items[0].weight
        return

    middle = math.ceil(len(items)/2)
    # middle = int(len(items)/2)
    medianValueWtItem = kthValue(items, middle, valueWtComparison)
    medianValueWtIdx = items.index(medianValueWtItem)
    partitionIdx = partition(items, medianValueWtIdx, inverse_valueWtComparison)

    # print(medianValueWtItem)
    # print("len(items): {}".format(len(items)))
    # print("partitionIdx: {}".format(partitionIdx))
    # print("middle: {}".format(middle))
    # print (items)
    # print("\n\n")

    sumWeight = sum([x.weight for x in items[:middle]])

    if sumWeight > capacity:
        mochila_frac2_rec(items[:middle], capacity)
    else:
        for i in range(middle):
            items[i].selectedWt = items[i].weight
        mochila_frac2_rec(items[middle:], capacity-sumWeight)

    return

def mochila_frac3(items, capacity):
    mochila_frac3_rec(items, capacity)
    return
        
def mochila_frac3_rec(items, capacity):
    if len(items) == 1:
        if items[0].weight >= capacity:
            items[0].selectedWt = capacity
        else:
            items[0].selectedWt = items[0].weight
        return

    # print("len(items): {}".format(len(items)))
    # sumValueWt = sum(x.valueWt for x in items)
    # print("sumValueWt: {}".format(sumValueWt))
    # print(items)

    averageValueWt = sum(x.valueWt for x in items) / len(items)
    firstSmallerIndx = inverse_partitionByValue(items, averageValueWt)


    
    # print("firstSmallerIndx: {}".format(firstSmallerIndx))
    # print("averageValueWt: {}".format(averageValueWt))
  
    

    sumWeight = sum([x.weight for x in items[:firstSmallerIndx]])

    # print("sumWeight: {}".format(sumWeight))
    # print("capacity: {}".format(capacity))
    # print("\n\n")

    if sumWeight > capacity:
        mochila_frac3_rec(items[:firstSmallerIndx], capacity)
    else:
        for i in range(firstSmallerIndx):
            items[i].selectedWt = items[i].weight
        mochila_frac3_rec(items[firstSmallerIndx:], capacity-sumWeight)

    return


def kthValue(items, k, comparisonFunction):
    if len(items) <= 5:
        sortedSubArray = mergesort(items,comparisonFunction)
        return sortedSubArray[k-1]

    medians = []
    for i in range(0, len(items), 5):
        sortedSubArray = mergesort(items[i:i+5],comparisonFunction)
        medians.append(sortedSubArray[int(len(sortedSubArray)/2)])

    pivot = kthValue(medians,int(len(medians)/2), comparisonFunction)
    pivotIdx = items.index(pivot)
    pivotIdx = partition(items, pivotIdx, comparisonFunction)
    p = pivotIdx+1

    if k == p:
        return items[pivotIdx]
    if k < p:
        return kthValue(items[0:pivotIdx], k, comparisonFunction)
    if k > p:
        return kthValue(items[pivotIdx+1:len(items)], k-p, comparisonFunction)

def select(items, k, comparisonFunction):
    return

def intcomparison (a, b):
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

def inverse_intcomparison (a, b):
    return -1 * intcomparison (a, b)

def partition(items, pivotIdx, comparisonFunction):
    i = 0

    pivotObj = items[pivotIdx]
    items[pivotIdx] = items[len(items)-1]
    items[len(items)-1] = pivotObj

    for j in range(len(items)-1):
        if comparisonFunction(items[j], pivotObj) <= 0:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1

    temp = items[i]
    items[i] = pivotObj
    items[len(items)-1] = temp

    return i

def inverse_partitionByValue(items, averageValueWt):
    sameValue = 0
    i = 0

    for j in range(len(items)):
        if items[j].valueWt > averageValueWt:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1
        elif abs(items[j].valueWt - averageValueWt) <= .5e-10:
            if sameValue%2 == 0:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
                i += 1
            sameValue += 1


    return i

def valueWtExtractor(x):
    return x.valueWt

def valueWtComparison(a, b):
    if abs(a.valueWt - b.valueWt) <=  .5e-10:
        return 0
    if a.valueWt > b.valueWt:
        return 1
    if a.valueWt < b.valueWt:
        return -1

def inverse_valueWtComparison(a, b):
    return -1 * valueWtComparison(a, b)

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


def mergesort(x, comparisonFunction):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle], comparisonFunction)
        b = mergesort(x[middle:], comparisonFunction)
        return merge(a,b, comparisonFunction)


def readFile(filename):
    f = open(filename)
    nItems = int(f.readline())

    items = []

    for i in range(nItems):
        num, value, weight = f.readline().split()
        items.append(Item(int(num), int(value), int(weight), float(value)/float(weight), 0))

    capacity = int(f.readline())

    return items, capacity

def main():
    if len(sys.argv) != 3:
        print("num2.py {filepath} {numero algoritmo}")
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