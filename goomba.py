class Goomba:
    """This class contain all the functions related to the goombas"""
    def __init__(self, x: int):
        """This init methods has the coordinates x and y for each goomba
                @ param x : x coordinate of each goomba
                the coordinate y is a constant during all the game"""
        self.x = x
        self.y = 256 - 48
        self.sprite = (0, 48, 16, 16, 16)
        self.direction = True

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) != int:
            raise TypeError("The x coordinate must be an integer")
        else:
            self.__x = x

    def move(self):
        """This method moves goomba from the right side of the screen to the
        left side"""
        if self.direction:
            self.x -= 1
        else:
            self.x += 1

    def move_right(self):
        """This method moves the goombas when mario moves forward"""
        self.x -= 3

    def collision_right(self, element):
        """This method checks when goomba is going forward and find an obstacle
        @ param : element, a list of two integer numbers corresponding to the coordinates
        of the element"""
        if self.x in range(element.x - 20, element.x) and self.y == element.y:
            return True
        return False

    def collision_left(self, element):
        """This method checks when goomba is going backwards and find an obstacle"""
        if self.x in range(element.x + 16, element.x + 20) and self.y == element.y:
            return True
        return False
