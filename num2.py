from __future__ import print_function
import sys
from collections import namedtuple

Item = namedtuple("Item", ["value", "weight", "valueWt", "num"])
# items = None
# capacity = None
        

def readFile (filename):
    f = open(filename)
    nItems = int(f.readline())

    items = [None] * nItems

    for i in range(nItems):
        num, value, weight = f.readline().split()
        items[i] = Item(int(value), int(weight), float(value)/float(weight), int(num))

    capacity = int(f.readline())

    return items, capacity


def main ():
    if len(sys.argv) != 3:
        print("num2.py {filename} {numero algoritmo}")
        return
    
    script, filename, algorithm = sys.argv
    items, capacity = readFile(filename)

    algorithm = int(algorithm)

    if algorithm == 1:
        mochila_frac_1()
    elif algorithm == 2:
        mochila_frac_2()
    elif algorithm == 3:
        mochila_frac_3()
    else:
        mochila_frac_1()
        mochila_frac_2()
        mochila_frac_3()




if __name__ == "__main__":
    main()