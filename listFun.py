fruit = ['oranges', 'kiwi', 'pineapple', 'apples']
cost = [3, 5, 7,5, 1]
number = [2, 3, 1, 8]

data = [fruit, cost, number]

myList = ["wreck", "yellow", 7, 8.5, "wrangled"]

empty = list()
orange = list("orange")
yellow = list("yellow")
colorList = orange + yellow
this = colorList[3:5]

def allUpper(myList):
    '''
    Description: Turns all strings in the list to capital letters

    Parameters: myList - list; the list containing the thins to be capitalized.

    Returns: 7
    '''

    for index in range(len(myList)):
        if isinstance(myList[index], str):
            myList[index] = myList[index].upper()

def removeNumbers(myList):
    '''
    for index in range(len(myList)):
        if isinstance(myList[index], int):
            del myList[index]
    '''

    for item in myList:
        if isinstance(item, str):
            myList.remove(item)




coloredBirds = ["yellow", "parakeets", 5, "red", "cardinals", 9]
removeNumbers(coloredBirds)
print(coloredBirds)


'''
def cumsum(i):
    sums = []
    cumSum = 0
    for num in range(len(i)-1):
        cumSum = cumSum + num
        sums.append(cumSum)


t = [1,2,3]
cumsum(t)
'''
