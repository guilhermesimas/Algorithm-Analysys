from __future__ import print_function
import sys

class Item():
    def __init__(self, num, value, weight, valueWt, selectedWt):
        self.value = value
        self.weight = weight
        self.valueWt = valueWt
        self.num = num
        self.selectedWt = selectedWt

    def __repr__(self):
        return "Item(num={3}, value={0}, weight={1}, valueWt={2}, selectedWt={4})".format(self.value, self.weight, self.valueWt, self.num, self.selectedWt)

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
    # mochila_frac2_rec(items, capacity, 0, len(items))
    mochila_frac2_rec(items, capacity)
    return

# def mochila_frac2_rec(items, capacity, start, end):
#     print(start)
#     print(end)
#     print("   ")
#     # if sum([x.weight for x in items]) < capacity:
#     #     for i in xrange(len(items)):
#     #         items[i].selectedWt = items[i].weight
#     #     return
#     if start > end:
#         return
#     if start == end:
#         items[start].selectedWt = capacity
#         return

#     middle = (start+end)/2
#     medianValueWtItem = kthValue(items, middle, valueWtComparison)
#     medianValueWtIdx = items.index(medianValueWtItem)
#     partition(items, medianValueWtIdx, inverse_valueWtComparison)

#     sumWeight = sum([x.weight for x in items[start:middle]]) //se start==middle retorn vazio e entao 0!

#     if sumWeight > capacity:
#         mochila_frac2_rec(items, capacity, start, middle)
#     else:
#         for i in xrange(start, middle):
#             items[i].selectedWt = items[i].weight
#         mochila_frac2_rec(items, capacity-sumWeight, middle, end)

#     return

def mochila_frac2_rec(items, capacity):
    # if sum([x.weight for x in items]) < capacity:
    #     for i in xrange(len(items)):
    #         items[i].selectedWt = items[i].weight
    #     return
    if len(items) == 1:
        items[0].selectedWt = capacity
        return

    middle = len(items)/2
    medianValueWtItem = kthValue(items, middle, valueWtComparison)
    medianValueWtIdx = items.index(medianValueWtItem)
    partition(items, medianValueWtIdx, inverse_valueWtComparison)

    sumWeight = sum([x.weight for x in items[:middle]])

    if sumWeight > capacity:
        mochila_frac2_rec(items[:middle], capacity)
    else:
        for i in xrange(middle):
            items[i].selectedWt = items[i].weight
        mochila_frac2_rec(items[middle:], capacity-sumWeight)

    return

def mochila_frac3(items, capacity):
    mochila_frac3_rec(items, capacity)
    return
        
def mochila_frac3_rec(items, capacity):
    if len(items) == 1:
        items[0].selectedWt = capacity
        return

    averageValueWt = sum(x.valueWt for x in items) / len(items)
    firstSmallerIndx = inverse_partitionByValue(items, averageValueWt)

    sumWeight = sum([x.weight for x in items[:firstSmallerIndx]])

    if sumWeight > capacity:
        mochila_frac2_rec(items[:firstSmallerIndx], capacity)
    else:
        for i in xrange(firstSmallerIndx):
            items[i].selectedWt = items[i].weight
        mochila_frac2_rec(items[firstSmallerIndx:], capacity-sumWeight)

    return


def readFile(filename):
    f = open(filename)
    nItems = int(f.readline())

    items = []

    for i in xrange(nItems):
        num, value, weight = f.readline().split()
        items.append(Item(int(num), int(value), int(weight), float(value)/float(weight), 0))

    capacity = int(f.readline())

    return items, capacity


def main():
    if len(sys.argv) != 3:
        print("num2.py {filename} {numero algoritmo}")
        return
    
    script, filename, algorithm = sys.argv
    items, capacity = readFile(filename)

    algorithm = int(algorithm)
    # print(items)
    # print(capacity)

    if algorithm == 1:
        mochila_frac1(items, capacity)
        
    elif algorithm == 2:
        mochila_frac2(items, capacity)
    elif algorithm == 3:
        mochila_frac3(items, capacity)
    # else:
    #     mochila_frac1(items, capacity)
    #     mochila_frac2(items, capacity)
    #     mochila_frac3(items, capacity)

    print([x for x in items if x.selectedWt != 0])
    print("selectedWt: {0}".format(sum([x.selectedWt for x in items])))
    print("totalWt: {0}".format(sum([x.weight for x in items])))
    print("capacity: {0}".format(capacity))

def kthValue(items, k, comparisonFunction):
    if len(items) <= 5:
        sortedSubArray = mergesort(items,comparisonFunction)
        return sortedSubArray[k-1]

    medians = []
    for i in xrange(0, len(items), 5):
        sortedSubArray = mergesort(items[i:i+5],comparisonFunction)
        medians.append(sortedSubArray[len(sortedSubArray)/2])

    pivot = kthValue(medians,len(medians)/2, comparisonFunction)
    pivotIdx = items.index(pivot)
    pivotIdx = partition(items, pivotIdx, comparisonFunction)
    p = pivotIdx+1

    if k == p:
        return items[pivotIdx]
    if k < p:
        return kthValue(items[0:pivotIdx], k, comparisonFunction)
    if k > p:
        return kthValue(items[pivotIdx+1:len(items)], k-p, comparisonFunction)

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

    for j in xrange(len(items)-1):
        if comparisonFunction(items[j], pivotObj) <= 0:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1

    temp = items[i]
    items[i] = pivotObj
    items[len(items)-1] = temp

    return i

    #     while(comparisonFunction(items[p], pivotObj))
    #         p++
    #      while(valueWtExtractor(items[]) < pivot_value)
    #         q--

    #     if (p<q)
    #         temp = items[p]
    #         items[p] = items[q]
    #         items[q] = temp
    #     else
    #         for i in xrange(q)
    #             left[i] = items[i]

    #         for i in xrange(q,len(items))
    #             right[i] = items[i] 

    # return left,right

def inverse_partitionByValue(items, averageValueWt):
    i = 0

    for j in xrange(len(items)-1):
        if items[j].valueWt > averageValueWt:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
            i += 1

    return i

def valueWtExtractor(x):
    return x.valueWt

def valueWtComparison(a, b):
    if a.valueWt == b.valueWt:
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
        middle = len(x)/2
        a = mergesort(x[:middle], comparisonFunction)
        b = mergesort(x[middle:], comparisonFunction)
        return merge(a,b, comparisonFunction)


if __name__ == "__main__":
    main()