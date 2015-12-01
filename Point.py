class Point:
    def __init__(self, x, y, str=(0,0)):
        str=input().split(',')
        self.x = int(str[0])
        self.y = int(str[1])
    def __str__(self):
        return '(' + self.x + ';' + self.y + ')'
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    def __lt__(self, other):
        if int(self.x**2+self.y**2) < int(other.x**2+other.y**2):
            return True
        else:
            return False
    def __le__(self, other):
        if int(self.x**2+self.y**2) <= int(other.x**2+other.y**2):
            return True
        else:
            return False
    def __eq__(self, other):
        if int(self.x**2+self.y**2) == int(other.x**2+other.y**2):
            return True
        else:
            return False
    def __ne__(self, other):
        if int(self.x**2+self.y**2) != int(other.x**2+other.y**2):
            return True
        else:
            return False
    def __gt__(self, other):
        if int(self.x**2+self.y**2) > int(other.x**2+other.y**2):
            return True
        else:
            return False
    def __ge__(self, other):
        if int(self.x**2+self.y**2) >= int(other.x**2+other.y**2):
            return True
        else:
            return False

