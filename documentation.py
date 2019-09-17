def stamper(t, size = 25):
    '''
    Description: This function creates stamps along a path in a spiral pattern.

    Parameters: t - Turtle object; does the drawing
                size - integer; the initial size of the first part of the path.

    Return Values: None

    Example:
    >>> myTurtle = turtle.Turtle()
    >>> stamper(myTurtle, 30)
    '''

    for _ in range(30):
        t.stamp()
        size = size + 3
        t.fd(size)
        t.rt(24)

def drawColors(t):
    '''
    Description: Choose a random color and then draw a length of the spiral in
    that color

    Parameters: t - turtle object; does the drawing

    Return Values: None

    Examples:
    >>> myTurtle = turtle.Turtle()
    >>> drawColors(myTurtle)
    '''

    for _ in range(30):
        myColor = random.choice(colorList)
        t.color(myColor)
        t.fd(50)
        t.lt(24)


if __name__ == '__main__':
    import turtle
    import random

    colorList = ["red", "green", "yellow", "orange", "firebrick"]

    myTurtle = turtle.Turtle()
    stamper(myTurtle)
    
    turtle.mainloop()
