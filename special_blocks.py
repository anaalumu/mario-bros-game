class SpecialBlocks:
    """This class contain all the functions related to the special blocks"""
    def __init__(self, x: int, y: int, block_type: int):
        """This init method has the coordinates x and y for each special block
                and the sprite that is constant during all the game
                @ param x : x coordinate of each block
                @ param y : y coordinate of each block
                @ param block_type:
                0 -> Question blocks: Blocks that contain coins or special objects.
                1 -> Brick blocks with coins: Brick blocks that give coins several times when hit by Mario.
                    Their outside appearance is exactly the same as breakable brick blocks."""

        self.x = x
        self.y = y
        self.block_type = block_type
        if block_type == 0:
            self.sprite = (0, 0, 0, 16, 16)
        elif block_type == 1:
            self.sprite = (0, 16, 0, 16, 16)

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
    def block_type(self):
        return self.__block_type

    @block_type.setter
    def block_type(self, block_type: int):
        if type(block_type) != int:
            raise TypeError("The block type must be an integer")
        else:
            self.__block_type = block_type

    def move_right(self):
        """This method moves the block when mario moves forward"""
        self.x -= 3
