def fac(n):
    '''
    Description: Compute n!

    Parameters: n -int; the integer to use for n!

    Returns: n!
    '''

    if(n==1):
        return 1

    return n*fac(n-1)

def fib(n):
    if(n <= 2):
        return 1

    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    num = 50

    result = fib(num)
    print(result)
