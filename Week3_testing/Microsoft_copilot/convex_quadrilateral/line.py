# import matplotlib.pyplot as plt
# from random import random
from typing import Union

class Point:
    '''class for creating points with x and y coordinates'''
    def __init__(self, x: int, y: int) -> None:
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

class Line:
    '''class for creating lines with two points and finding intersecion'''
    def __init__(self, point1: 'Point', point2: 'Point') -> None:
        if point1 == point2:
            raise ValueError("Can't create the line from equal points")
        self.point1 = point1
        self.point2 = point2

    def intersect(self, other: 'Line') -> Union['Point', 'Line']:
        '''
        returns None if lines don't intersect
        returns Point if lines intersect in one point
        returns Line if lines are the same
        '''
        if self.point2.x - self.point1.x == 0 and other.point2.x - other.point1.x == 0:
            if self.point2.x == other.point2.x:
                return self
            return None
        if self.point2.x - self.point1.x == 0:
            k2 = (other.point2.y - other.point1.y) / (other.point2.x - other.point1.x)
            return Point(self.point2.x, other.point2.y + (self.point2.x - other.point2.x) * k2)
        if other.point2.x - other.point1.x == 0:
            k1 = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
            return Point(other.point2.x, self.point2.y + (other.point2.x - self.point2.x) * k1)
        k1 = (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        k2 = (other.point2.y - other.point1.y) / (other.point2.x - other.point1.x)
        b1 = self.point2.y - k1 * self.point2.x
        b2 = other.point2.y - k2 * other.point2.x
        if k1 == k2:
            if b1 == b2:
                return self
            return None
        x = (b2 - b1) / (k1 - k2)
        return Point(round(x, 2), round(k1 * x + b1, 2))
