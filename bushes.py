class Bushes:
    """This class contain all the functions related to the bushes"""

    def __init__(self, x: int, y: int):
        """This init methods has the coordinates x and y for each bush
                and the sprite that is constant during all the game
                @ param x : x coordinate of each bush
                @ param y : y coordinate of each bush"""
        self.x = x
        self.y = y
        self.sprite = (0, 0, 152, 32, 16)

    def move_right(self):
        """This method moves the bushes when mario moves forward"""
        self.x -= 3
