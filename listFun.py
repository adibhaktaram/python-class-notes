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

def cumsum(i):
    sums = []
    cumSum = 0
    for num in range(len(i)-1):
        cumSum = cumSum + num
        sums.append(cumSum)
    

t = [1,2,3]
cumsum(t)
