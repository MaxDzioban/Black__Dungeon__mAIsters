"""The lines"""

class Point:
    '''The point'''
    def __init__(self, x, y) -> None:
        """Initializing the attributes"""
        self.x = x
        self.y = y

class Line:
    """The line"""
    def __init__(self, point1, point2) -> None:
        """INitializing the attributes"""
        if not (isinstance(point1, Point) or isinstance(point2, Point)):
            raise ValueError('Ok')
        self.point1 = point1
        self.point2 = point2
        self.k = (point2.y - point1.y) / (point2.x - point1.x) if point2.x - point1.x != 0 \
            else 'Foo'
        self.l = point1.y - self.k*point1.x if self.k != "Foo" else "Foo"


    def intersect(self, otehr):
        """Intersection"""
        if self.k == 'Foo' and otehr.k == "Foo":
            return Line(self.point1, self.point2) if self.point1.x == otehr.point1.x else None
        if self.k == 'Foo' or otehr.k == "Foo":
            return Point(otehr.point1.x, self.k * otehr.point1.x + self.l) if otehr.k == "Foo" else\
                          Point(self.point1.x, otehr.k * self.point1.x + otehr.l)
        if self.k == otehr.k:
            if self.l == otehr.l:
                return Line(self.point1, self.point2)
            return
        pointx = (otehr.l - self.l) / (self.k  - otehr.k)
        return Point(pointx, (self.k * pointx) + self.l)
