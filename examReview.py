class Lunch:
    '''This is my lunch'''
    def __init__(self, protein, carbs, vegetables, dessert):
        self.protein = protein
        self.carbs = carbs
        self.vegetables = vegetables
        self.dessert = dessert

    def __str__(self):
        return "Menu: %s, %s, %s, and %s" %(self.protein, self.carbs, self.vegetables, self.dessert)

mine = Lunch("Chicken Strips", "mac & cheese", None,  "Cake" )
print(mine)

class Toybox:
    '''my toybox'''

class Book:
    '''favorite books Dad reads'''

class Truck:
    '''my truck'''

box = Toybox()
box.favBook = Book()
box.favBook.title = "The Giving Tree"
box.bigTruck = Truck()
box.bigTruck.name = "Crane"
