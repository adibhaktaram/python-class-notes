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


class nPoint:
    ''' Represents a point in n-space

        Attributes:
            point - tuple; the coordinates of that Point
            numCords - int; The number of coordinates that the point has.
    '''

    def __init__(self, *args):
        self.numCords = len(args)
        self.point = args

    def __str__(self):
        return str(self.point)

    def __add__(self, other):
        t = list()

        for i in range(self.numCords):
            t.append(self.point[i] + other.point[i])

        return Point(*t)


if __name__ == '__main__':
    p = nPoint(-2, 7, 9)
    q = nPoint(2, 3, 1)
    print(p+q)
