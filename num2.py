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
    mochila_frac2_rec(items, capacity, 0, len(items))
    return

def mochila_frac2_rec(items, capacity, start, end):
    # if start > end:
    #     return
    # if start == end:
    #     items[start].selectedWt = capacity
    #     return
    if len(items) == 1:
        items[0].selectedWt = capacity
        return

    middle = len(items)/2
    middleValueWtIdx = kthValue(items, middle, valueWtExtractor)

    return

def mochila_frac3(items, capacity):
    return
        

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
        print("num2.py {filename} {numero algoritmo}")
        return
    
    script, filename, algorithm = sys.argv
    items, capacity = readFile(filename)

    algorithm = int(algorithm)
    # print(items)
    # print(capacity)

    if algorithm == 1:
        mochila_frac1(items, capacity)
        # print([x for x in items if x.selectedWt != 0])
        # print(sum([x.selectedWt for x in items]))
        # print(sum([x.weight for x in items]))
    elif algorithm == 2:
        mochila_frac2(items, capacity)
    elif algorithm == 3:
        mochila_frac3(items, capacity)
    # else:
    #     mochila_frac1(items, capacity)
    #     mochila_frac2(items, capacity)
    #     mochila_frac3(items, capacity)

def valueWtExtractor(x):
    return x.valueWt

def valueWtComparison(a, b):
    return a.valueWt < b.valueWt 

def inverse_valueWtComparison(a, b):
    return not valueWtComparison(a, b)

def merge(a,b, comparisonFunction):
    c = []
    while len(a) != 0 and len(b) != 0:
        if comparisonFunction(a[0], b[0]):
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