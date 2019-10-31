class Point:
    '''Represents a point in 2-space'''

class Rectangle:
    '''
    Represents a reactangle and its lower left corner

    Attributes:
        length - length of the Rectangle
        width - width of the Rectangle
        lower - the lower left corner of the point object
    '''

class Triangle:
    '''
    Represents a Triangle

    Attributes:
        length - length of each side
    '''

def printPoint(point):
    pString = "(%d, %d)" % (point.x, point.y)
    return pString

def distance(thisPoint, otherPoint):

    dSquare = (thisPoint.x - otherPoint.x)**2 + (thisPoint.y - otherPoint.y)**2
    return sqrt(dSquare)

def drawRectangle(t, rect):
    t.pu()
    t.goto(rect.lower.x, rect.lower.y)
    t.pd()
    for _ in range(2):
        t.fd(rect.length)
        t.lt(90)
        t.fd(rect.width)
        t.lt(90)

def drawTriangle(t, triangle):
    for _ in range(3):
        t.fd(triangle.length)
        t.lt(120)


if __name__ == '__main__':
    import turtle
    from math import sqrt
    '''
    newPoint = Point()
    newPoint.x = 3
    newPoint.y = 18

    nextPoint = Point()
    nextPoint.x = -3
    nextPoint.y = 4

    print(distance(newPoint, nextPoint))
    '''

    myTurtle = turtle.Turtle()


    corner = Point()
    corner.x = -100
    corner.y = -20

    myRect = Rectangle()
    myRect.length = 60
    myRect.width = 90
    myRect.lower = corner

    myTriangle = Triangle()
    myTriangle.length = 100

    drawTriangle(myTurtle, myTriangle)
    turtle.mainloop()
