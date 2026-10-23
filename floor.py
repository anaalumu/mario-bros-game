class Floor:
    """This class contain all of the functions related to the floor"""
    def __init__(self, x: int, y: int):
        """This init methods has the coordinates x and y for each tile that forms the floor
        and the sprite that is constant during all the game
        @ param x : x coordinate of each tile
        @ param y : y coordinate of each tile"""
        self.x = x
        self.y = y
        self.sprite = (0, 16, 64, 16, 16)

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
