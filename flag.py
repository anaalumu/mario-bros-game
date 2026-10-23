class Flag:
    """This class contain all the functions related to the flag"""
    def __init__(self, x: int):
        """This init methods has the coordinates x and y for the flag
                @ param x : x coordinate of the flag
                the coordinate y is a constant during all the game"""
        self.x = x
        self.y = 160
        self.sprite = (0, 48, 88, 24, 16*4)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) != int:
            raise TypeError("The x coordinate must be an integer")
        else:
            self.__x = x

    def move_right(self):
        """This method moves the flag when mario moves forward"""
        self.x -= 3
