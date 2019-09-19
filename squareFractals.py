def hilbert(t, reverse, depth):
    if(reverse == true):
        t.lt(90)
        hilbert(t, reverse, depth - 1)
        t.fd(50)
        t.rt(90):
        
    if(depth < 0):
        return
