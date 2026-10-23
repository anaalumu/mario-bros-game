class Koopa:
    """This class contain all the functions related to the koopas"""
    def __init__(self, x: int):
        """This init methods has the coordinates x and y for each koopa
                @ param x : x coordinate of each koopa
                the coordinate y is a constant during all the game"""
        self.x = x
        self.y = 208
        self.distance = 45
        self.walked = 0
        self.sprite = (0, 16, 32, 16, 16)
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
        """This method controls the movements of the koopas. They moved on a fixed
        are from one side to the other"""
        if self.direction and self.walked <= self.distance:
            self.x -= 1
            self.walked += 1
        if self.walked == 45:
            if self.direction:
                self.direction = False
                self.sprite = (0, 0, 32, 16, 16)
            else:
                self.direction = True
                self.sprite = (0, 16, 32, 16, 16)
            self.walked = 0

        if not self.direction and self.walked <= self.distance:
            self.x += 1
            self.walked += 1

    def move_right(self):
        """This method moves the koopas when mario moves forward"""
        self.x -= 3

    def collision_right(self, element):
        """This method checks when the koopa is going forward and find an obstacle
        @ param : element, a list of two integer numbers corresponding to the coordinates
        of the element"""
        if self.x in range(element.x - 20, element.x) and self.y == element.y:
            return True
        return False

    def collision_left(self, element):
        """This method checks when the koopas is going backwards and find an obstacle"""
        if self.x in range(element.x + 16, element.x + 20) and self.y == element.y:
            return True
        return False
