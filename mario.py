
class Mario:
    """This class contains all the actions related to Mario"""
    def __init__(self, x: int, y: int, sprite: tuple):
        """
        @param x: the x coordinate of mario in the screen
        @param y: the y coordinate of mario in the screen
        @param sprite: tuple of five elements that represents: [0] 0, 1, 2 for the screens,
        [1] for the x coordinate in the resources, [2] for the y coordinate in the resources,
        [3] for the size of x, [4] for the size of y"""
        self.x = x
        self.y = y
        self.sprite = sprite

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

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: tuple):
        if type(sprite) != tuple:
            raise TypeError("The sprite must be a tuple")
        elif len(sprite) != 5:
            raise ValueError("The sprite must have five elements")
        else:
            self.__sprite = sprite

    def move(self, direction: str, size: int):
        """This function moves Mario,
        @param direction: left, or right
        @param size: the size of the game, constant during all of it"""
        mario_x_size = self.sprite[3]
        if direction == "right" and self.x < size - mario_x_size:
            self.x += 4
            # when mario arrives to the middle of the screen, it stays there:
            if self.x >= 128:
                self.x = 128
        elif direction == "left" and self.x > 0:
            self.x -= 4
            # I am assuming that if it is not right it will be left

    def collision_down(self, element):
        """This method check if mario is on top of an element
        @param: element, a list of two integer numbers corresponding to the coordinates
        of an element in the game: floor, blocks or pipes"""
        mario_height = self.y + 15
        for x in range(self.x, self.x + 16):
            if x in range(element.x, element.x + 16) and mario_height == element.y - 1:
                return True

        return False

    def collision_up(self, element):
        """This method check if mario is bellow an element
        @ param : element, a list of two integer numbers corresponding to the coordinates
        of blocks"""
        for x in range(self.x, self.x + 16):
            if x in range(element.x - 3, element.x + 13) and self.y in range(element.y + 16, element.y + 24):
                return True
        return False

    def collision_right(self, element):
        """This method checks when mario is going forward and find an obstacle
        @ param : element, a list of two integer numbers corresponding to the coordinates
        of the element"""
        if self.x in range(element.x - 20, element.x) and self.y == element.y:
            return True
        return False

    def collision_left(self, element):
        """This method checks when mario is going backwards and find an obstacle
        @ param : element, a list of two integer numbers corresponding to the coordinates
        of the element"""
        if self.x in range(element.x + 16, element.x + 20) and self.y == element.y:
            return True
        return False
