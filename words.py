'''
fin = open("words.txt", r)

for line in fin:
    print(line.strip())

print(fin.readline())

fin.close()

fin = open("lunch.txt", 'w')
'''
'''
fin.write("Things I want for lunch this week: \n")
fin.write("Lasagna \n")
fin.write("Mixed Fruit ")
fin.write("Oreo Bars (freshly Made)")

thisFile = open("words.py", 'w')
thisFile.close()
fin.close()
'''
'''
fin = open("lunch.txt", 'a')
fin.write("Friday's Lunch:")
fin.write("Leftovers: pizza, barbeque, casserole, all of the vegetables.")

fin.close()
'''

def hasNoE(string):
    '''
    This function checks to see if there is no 'e'. It returns True if there is
    no 'e' and false if there is an 'e' in the string.
    '''

    for char in string:
        if char == 'e':
            return False

    return True

def hasNoEAlt(string):
        return not('e' in string)

print(hasNoEAlt("Have you has a Japanese eggplant on your sushi?"))

fin = open("words.txt")
for line in fin:
    if hasNoE(line):
        print(line.strip())
