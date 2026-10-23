class Clouds:
    """This class contain all the functions related to the clouds"""
    def __init__(self, x: int, y: int):
        """This init methods has the coordinates x and y for each cloud
                and the sprite that is constant during all the game
                @ param x : x coordinate of each cloud
                @ param y : y coordinate of each cloud"""
        self.x = x
        self.y = y
        self.sprite = (0, 0, 80, 32, 32)

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
        self.x -= 3
