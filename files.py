fout = open("storage.txt", "w")

line = "It is early morning, I am sitll asleep. I can'tbelieve I made it to school."

fout.write(line)

x = 52
fout.write(str(x))

line = "I have %d pinapples and no knives. \n" %x
fout.write(line)

numTrees = 8
fruit = "pineapples"
cost = 3.5
years = 6

newLine = "In %d years, I will have %d %s trees, that cost %g" % (years, numTrees, fruit, cost)
fout.write(newLine)

fout.close()
