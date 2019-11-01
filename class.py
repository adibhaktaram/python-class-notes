class Triangle:
    ''' Represents a triangle'''

class EquiTriangle(Triangle):
    '''Represents an equilateral triangle'''

class Point:
    '''Represents a point'''

class RegularPolygon:
    '''Represents a regular polygon'''

def drawTri(turtleObj, triObj):
    turtleObj.pu()
    turtleObj.goto(triObj.vertex.x, triObj.vertex.y)
    turtleObj.pd()

    for _ in range(3):
        turtleObj.fd(triObj.length)
        turtleObj.rt(180 - triObj.angle)

def drawPolly(turtleObj, polygonObj, value):
    turtleObj.pu()
    turtleObj.goto(polygonObj.vertex.x, polygonObj.vertex.y)
    turtleObj.pd()
    turtleObj.color(polygonObj.color)

    if value == True:
        turtleObj.begin_fill()
        for _ in range(polygonObj.sides):
            turtleObj.fd(polygonObj.length)
            turtleObj.lt(360 / polygonObj.sides)
        turtleObj.end_fill()
    else:
        for _ in range(polygonObj.sides):
            turtleObj.fd(polygonObj.length)
            turtleObj.lt(360 / polygonObj.sides)



if __name__ == '__main__':
    import turtle
    myTurtle = turtle.Turtle()

    p = Point()
    p.x = 15
    p.y = 23

    tim = EquiTriangle()
    tim.length = 20
    tim.angle = 60
    tim.vertex = p

    polly = RegularPolygon()
    polly.length = 100
    polly.sides = 5
    polly.color = 'blue'
    polly.vertex = p

    drawPolly(myTurtle, polly, True)

    turtle.mainloop()
