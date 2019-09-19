def koch(t, length):
    if(length < 3):
        t.fd(length)
        return
    else:
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
def snowflake(t, length):
    if(length < 3):
        t.fd(length)
        return
    else:
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)



if __name__ == '__main__':
    import turtle
    bob = turtle.Turtle()
    bob.speed(0)
    snowflake(bob, 150)
    turtle.mainloop()
