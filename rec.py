def printN(string, n):
    if n<= 0:
        return
    print(string)

    printN(string, n-1)


def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def draw(t, length, n):
    if n  == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-2)
    t.lt(angle)
    t.bk(length*n)

if __name__ == '__main__':
    import turtle
    bob = turtle.Turtle()
    draw(bob, 5, 5)
    turtle.mainloop()
