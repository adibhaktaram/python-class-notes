
'''
x = 7
y = 4

z = x

]
#swap
x = y
y = z

#swap using tuples
x,y = y,x
print(x,y)
'''


#Exercise: Write a function called small which takes any number of arguments
# and returns their sum.

def sumall(*args):
    counter = 0
    accum = 0
    while counter <= len(args):
        accum = accum +sum(args[counter: counter+2])
        counter += 2
    return accum

if __name__ == '__main__':
    print(sumall(2, 7, 11, 9))
