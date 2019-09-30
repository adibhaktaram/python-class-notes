def print_n(s,n):
    if( n<= 0):
        return
    print(s)
    print_n(s,n-1)

def print_nw(s,n):
    while n != 0:
        print(s)
        n = n-1


def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:           # n is odd
            n = n*3 + 1     # n is now

def getInput():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print("Done!")

def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            print("Done!")
            break
        else:
            n = eval(line)
            print(n)

if __name__ == '__main__':
    eval_loop()
