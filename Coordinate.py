'''пока что не используется'''


class Coordinate(tuple): 
        
    def __new__(cls, *args):
        return tuple([*args])

    def __add__(self, other):
        return Coordinate(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Coordinate(self[0] - other[0], self[1] - other[1])
