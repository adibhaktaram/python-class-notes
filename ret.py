from math import sqrt

def boxArea(length, width):
    area = length * width
    return area

def distance(x1, y1, x2, y2):
    dSquared = (x2-x1)**2 + (y2-y1)**2
    dist = sqrt(dSquared)

    return dist

def absValue(n):
    if (isinstance(n, int) or isinstance(n, float)):
        if n>= 0:
            return n
        else:
            return -n
    print("n must be a number")

def myFunction(string):
    return
    print(string)

def isDivisible(x, n):
    '''
    if(x%n == 0):
        return True
    else:
        return False
    '''
    return (x%n == 0)

if __name__ == '__main__':
    print(isDivisible(6, 3))
