class Point:
    ''' Represents a point in 2-space'''


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' %(self.x, self.y)

    def __add__(self,other):
        temp = Point(self.x + other.x, self.y + other.y)
        return temp

    def __eq__(self, other):
        if (self.x != other.x):
            return False
        else:
            return self.y == other.y

    def draw(self):
        pyplot.plot(self.x, self.y, "bo")


class nPoint():
    ''' Represents a point in n-space

        Attributes:
            point - tuple; the coordinates of that Point
            numCoords - int; The number of coordinates that the point has.
    '''

    def __init__(self, *args):
        self.numCoords = len(args)
        self.point = args

    def __str__(self):
        return str(self.point)

    def __add__(self, other):
        t = list()

        if self.numCoords != other.numCoords:
            raise NumCoordsException("The Number of Coordinates do NOT match!")

        for i in range(self.numCoords):
            t.append(self.point[i] + other.point[i])
        return nPoint(*t)

    class NumCoordsException(Exception):
        '''THis exception is raised when the number of coordinates do not match'''


if __name__ == '__main__':
    import matplotlib.pyplot as pyplot

    p = nPoint(-2, 7, 9)
    q = nPoint(2, 3, 1)

    lp = Point(-7, 1)
    lq = Point(3, 1)
    lr = Point(-2, 15)
    ls = Point(-13, 35)

    '''
    pyplot.plot([lp.x, lq.x, lr.x, ls.x], [lp.y, lq.y, lr.y, ls.y], "rx")
    pyplot.plot([lp.x, lq.x], [lp.y, lq.y], "go-", label = "line", linewidth = 1)
    '''

    lp.draw()
    pyplot.show()
