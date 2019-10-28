def isCalled():
    global called
    called = True

def addPair(key, value):
    meat[key]=value
    meat = dict()

if __name__ == '__main__':
    meat = {'salami': 'cheese', 'bacon': 'eggs', 'peanut butter': 'jelly', 'seafood': 'sushi'}
    fruit = ["mango", "kiwi", "oranges", "apples", "starfruit"]
    prices = [1, 1.5, 10, 3, 713]


    zipObj = zip(fruit, prices)
    #for item in zipObj:
        #print(item)
    fruitPrice = dict(zipObj)
    print(fruitPrice)
