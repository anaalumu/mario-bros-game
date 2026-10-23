class Castle:
    """This class contain all the functions related to the final castle"""

    def __init__(self, x: int):
        """This init methods has the coordinates x and y for each castle
                @ param x : x coordinate of each castle
                the coordinate y is a constant during all the game"""
        self.x = x
        self.y = 160-16
        self.sprite = (1, 0, 64, 16*4, 16 * 5)

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
        """This method moves the castle when mario moves forward"""
        self.x -= 3
