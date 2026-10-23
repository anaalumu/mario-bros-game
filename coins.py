class Coins:
    """This class contains all the functions related to the coins """
    def __init__(self, x: int, y: int):
        """This init methods has the coordinates x and y for each coin
        @param x: the x coordinate of a coin
        @param y: the y coordinate of a coin"""
        self.x = x
        self.y = y
        self.sprite = (0, 48, 32, 16, 16)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) != int:
            raise TypeError("The x coordinate must be an integer")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if type(y) != int:
            raise TypeError("The y coordinate must be an integer")
        else:
            self.__y = y

    def move_right(self):
        """This method moves the coins when mario moves forward"""
        self.x -= 3
