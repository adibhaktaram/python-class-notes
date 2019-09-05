def example(myVar):
    x = myVar

def numTabs(n):
    print('\t')*n, end = ''

def concatTwo(string1, string2):
    concat = string1+string2
    numTabs(3)
    print(concat)

if __name == '__main__':
    import math

    x = math.sqrt(2)
    print(x)

def approxsqrt2(x):
    approx = 1+1/(2+1/(2+x))
    print(approx)
