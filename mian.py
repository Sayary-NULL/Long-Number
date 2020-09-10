import math

def readArray():
    N = int(input("N: "))
    number = []
    for i in range(0, N):
        number.append(int(input()))
    return number

def Del(x):
    out = []
    while x > 0:
        out.append(x % 10)
        x = x // 10
    out.reverse()
    return out

def sort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(0, n-1):
            if not Comp(array[j], array[j+1]):
                t = array[j]
                array[j] = array[j+1]
                array[j+1] = t
    return array

def Comp(x, y):
    lx = int(math.log10(x))
    ly = int(math.log10(y))
    if lx == ly:
        return x > y
    elif lx > ly:
        outx = Del(x)
        outy = Del(y)
        lenx = len(outx)
        leny = len(outy)
        for i in range(0, leny):
            if outx[i] > outy[i]:
                return True
    else:
        outx = Del(x)
        outy = Del(y)
        lenx = len(outx)
        leny = len(outy)
        for i in range(0, lenx):
            if outx[i] > outy[i]:
                return True
    return False

def printArray(arr):
    lenn = int(len(arr))
    for i in range(0, lenn):
        print(arr[i], end="")

if __name__ == "__main__":
    array = readArray()
    #array = [9, 515, 4, 2, 7]
    array = sort(array)
    printArray(array)