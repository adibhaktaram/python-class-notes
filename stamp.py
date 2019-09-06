def stamper(t, size):
    '''

    '''

    for _ in range(30):
        t.stamp()
        size = size + 3
        t.fd(size)
        t.rt(24)

def drawColors(t):

    for _ in range(30):
        myColor = random.choice(colorList)
        t.color(myColor)
        t.fd(50)
        t.lt(24)


if __name__ == '__main__':
    import turtle

    myTurtle = turtle.Turtle()
    myTurtle.shape("classic")
    stamper(myTurtle, 20)

    turtle.mainloop()
