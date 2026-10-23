from mario import Mario
from floor import Floor
from clouds import Clouds
from pipes import Pipes
from bushes import Bushes
from special_blocks import SpecialBlocks
from goomba import Goomba
from koopa import Koopa
from coins import Coins
from flag import Flag
from castle import Castle
import random
import time
import pyxel


class Board:
    """This class contained all the elements that appear on the screen"""
    def __init__(self, width: int, height: int):
        """The width and the height represent the size of the main screen
        @param width : width of the screen
        @param height: height of the screen"""
        self.width = width
        self.height = height
        self.mario = Mario(10, 208, (0, 0, 48, 16, 16))
        # the total number of pixels of the level:
        self.py_width = 9*16*16
        # the y coordinate for all elements od size 16 that are in the floor:
        self.level_floor = 208
        # points of mario during the game, it starts at zero:
        self.points = 0
        # the number of lives of lives, it starts with 3:
        self.number_lives = 3
        # the number of coins, it starts with zero:
        self.number_coins = 0
        # the starting time:
        self.starting_time = time.time()
        # the time left(it starts with the maximum time) and the time of the game:
        self.max_time = self.time_left = 400
        # the maximum height mario reaches in a jump (3 blocks):
        self.height_max_jump = 48
        # the distance mario is from the floor when jumping:
        self.height_jump = 0
        # when mario is jumping is True, when not is False:
        self.is_jumping = False
        # when jumping, when mario is going up is True, when not is False:
        self.jump_up = True
        # counter for the coins that mario has already obtained from the "?" block
        self.counter = 1
        # special blocks, are the ones with bricks, with the question mark, and the clear blocks
        # we create them along the game when necessary
        self.special_blocks = []

        # floor:
        self.floor = []
        for f in range(int(self.py_width/16)):
            flo = Floor(f*16, 240)
            self.floor.append(flo)
        for f in range(int(self.py_width/16)):
            flo = Floor(f*16, 224)
            self.floor.append(flo)

        # pipes:
        self.pipes = []
        y = self.level_floor
        x = 300
        while x < self.py_width:
            n = Pipes(x, y)
            self.pipes.append(n)
            x += 300

        # bushes:
        self.bush = []
        y = self.level_floor
        x = 50
        while x < self.py_width:
            n = Bushes(x, y)
            self.bush.append(n)
            x += 100

        # clouds:
        self.clouds = []
        x = 0
        while x < self.py_width:
            y = random.randint(20, 100)
            n = Clouds(x, y)
            self.clouds.append(n)
            x += 100
        # list of enemies:
        self.enemies = []

        # list of coins:
        self.coins = []

        # screen 1:
        self.coins.append(Coins(120, 180))
        self.coins.append(Coins(120 + 40, 180))
        self.coins.append(Coins(120 + 80, 180))

        # screen 2:
        self.special_blocks.append(SpecialBlocks(375, 160, 1))
        self.special_blocks.append(SpecialBlocks(375 + 16, 160, 0))
        self.special_blocks.append(SpecialBlocks(375 + 16 + 16, 160, 1))
        self.coins.append(Coins(300, 150))

        # screen 3:
        self.pipes.append(Pipes(600 - 60, self.level_floor))
        self.pipes.append(Pipes(600 + 60, self.level_floor))
        self.special_blocks.append(SpecialBlocks(600, 145, 0))

        # screen 4:
        for n in range(2):
            self.remove_tiles(752 + 16*n)
        self.coins.append(Coins(760, 170))
        self.remove_bush(750)

        # screen 5:
        for n in range(2):
            self.floor.append(Floor(944 + 16*n, 208))
            self.floor.append(Floor(1008, 208 - 16*n))
            self.floor.append(Floor(1008 + 16, 208 - 16*n))
        for n in range(3):
            self.floor.append(Floor(1072, 208 - 16*n))
            self.floor.append(Floor(1072, 208 - 16*n))
            self.floor.append(Floor(1072 + 16, 208 - 16*n))
        for n in range(2, 4):
            self.remove_tiles(944 + 16*n)
            self.remove_tiles(1008 + 16*n)
            self.remove_tiles(1072 + 16*n)
        self.special_blocks.append(SpecialBlocks(1072, 208 - 100, 1))
        self.special_blocks.append(SpecialBlocks(1072 + 16, 208 - 100, 1))
        self.remove_bush(850)
        self.remove_bush(950)
        self.remove_bush(1050)

        # screen 5:
        self.pipes.append(Pipes(1250, self.level_floor))
        for n in range(8):
            self.floor.append(Floor(1300 + n*16, 200))
        for n in range(5):
            self.floor.append(Floor(1324 + n*16, 184))
            self.floor.append(Floor(1324 + n * 16, 168))
        for n in range(3):
            self.floor.append(Floor(1340 + n*16, 152))
        for n in range(11):
            self.remove_tiles(1280 + n*16)
        self.pipes.append(Pipes(1356, 152-16))
        self.special_blocks.append(SpecialBlocks(1356, 75, 0))
        self.remove_bush(1250)
        self.remove_bush(1350)

        # screen 7:
        self.floor.append(Floor(1530, 208 - 16))
        for n in range(4):
            self.special_blocks.append(SpecialBlocks(1546+16*n, 208 - 16, 1))
        self.floor.append(Floor(1610, 208 - 16))
        self.floor.append(Floor(1640, 208 - 16 - 24))
        for n in range(6):
            self.special_blocks.append(SpecialBlocks(1656 + 16*n, 208 - 16 - 24, 1))
        self.floor.append(Floor(1752, 208 - 16 - 24))
        for n in range(3):
            self.coins.append(Coins(1546 + 25 * n, 150-10*n))
            self.special_blocks.append(SpecialBlocks(1666 + 30 * n, 105, 0))

        # final screen:
        self.flag = Flag(1890)
        self.castle = Castle(1984)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if type(width) != int or width <= 0:
            raise TypeError("The width must be an integer bigger tha zero")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if type(height) != int or height <= 0:
            raise TypeError("The height must be an integer bigger tha zero")
        else:
            self.__height = height

    def show(self):
        """This method contains all the scoreboard: punctuation, lives, coins, ans time"""
        first_element = 30   # x coordinate of the first element in the scoreboard
        distance = 60        # distance between the elements in the scoreboard
        row1 = 10            # first row of elements
        row2 = 20            # second row of elements
        # punctuation:
        pyxel.text(first_element, row1, "MARIO", 0)
        p = str(self.points)
        pyxel.text(first_element, row2, p.zfill(6), 0)
        # lives
        pyxel.blt(first_element + distance * 1 - 7, row2 - 5, 0, 32, 32, 16, 16)
        pyxel.text(first_element + distance * 1 + 12, row2, "x" + str(self.number_lives).zfill(2), 0)
        # coins
        pyxel.blt(first_element + distance * 2 - 10, row2 - 5, 0, 48, 32, 16, 16)
        pyxel.text(first_element + distance * 2 + 10, row2, "x" + str(self.number_coins).zfill(2), 0)
        # time
        pyxel.text(first_element + distance * 3, row1, "TIME", 0)
        self.time_left = self.max_time - int(time.time() - self.starting_time)
        pyxel.text(first_element + distance * 3, row2, str(self.time_left).zfill(3), 0)

    def move_everything_right(self):
        """This method moves all the elements to the right when mario goes forward"""
        if not self.block_right():
            for n in self.clouds:
                n.move_right()
            for p in self.pipes:
                p.move_right()
            for b in self.bush:
                b.move_right()
            for f in self.floor:
                f.move_right()
            for b in self.special_blocks:
                b.move_right()
            for e in self.enemies:
                e.move_right()
            for c in self.coins:
                c.move_right()
            self.flag.move_right()
            self.castle.move_right()

    def update(self):
        """This method controls all the movements of mario, the other elements which interact with him"""
        if pyxel.btnp(pyxel.KEY_E):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT) and not self.block_right():
            self.mario.move("right", self.width)
            self.mario.sprite = (0, 0, 48, 16, 16)
            if self.mario.x == 128:
                self.move_everything_right()
        elif pyxel.btn(pyxel.KEY_LEFT) and not self.block_left():
            self.mario.move("left", self.width)
            self.mario.sprite = (1, 0, 48, 16, 16)
        if pyxel.btn(pyxel.KEY_SPACE):
            self.start_jump()
        self.mario_jump()
        if pyxel.btn(pyxel.KEY_SPACE) and pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.sprite = (0, 32, 48, 16, 16)
        if pyxel.btn(pyxel.KEY_SPACE) and pyxel.btn(pyxel.KEY_LEFT):
            self.mario.sprite = (0, 48, 48, 16, 16)
        for n in range(1, 4000, 5):
            if pyxel.frame_count == 60*n and len(self.enemies) < 4:
                self.create_enemies()
        for element in self.enemies:
            element.move()
            if element.x < -16:
                self.enemies.remove(element)
        self.mario_touch_enemies()
        self.enemies_change()
        self.mario_touches_coin()
        self.mario_touches_block()
        self.mario_loses_life()

    def draw(self):
        """This method draw Mario and the elements on the screen"""
        # we establish the color of the background
        pyxel.cls(6)
        for cloud in self.clouds:
            pyxel.blt(cloud.x, cloud.y, cloud.sprite[0], cloud.sprite[1],
                      cloud.sprite[2], cloud.sprite[3], cloud.sprite[4])
        for bush in self.bush:
            pyxel.blt(bush.x, bush.y, bush.sprite[0], bush.sprite[1],
                      bush.sprite[2], bush.sprite[3], bush.sprite[4])
        for pipe in self.pipes:
            pyxel.blt(pipe.x, pipe.y, pipe.sprite[0], pipe.sprite[1],
                      pipe.sprite[2], pipe.sprite[3], pipe.sprite[4])
        for element in self.floor:
            pyxel.blt(element.x, element.y, element.sprite[0], element.sprite[1],
                      element.sprite[2], element.sprite[3], element.sprite[4])

        for block in self.special_blocks:
            pyxel.blt(block.x, block.y, block.sprite[0], block.sprite[1], block.sprite[2],
                      block.sprite[3], block.sprite[4])
        for coin in self.coins:
            pyxel.blt(coin.x, coin.y, coin.sprite[0], coin.sprite[1], coin.sprite[2],
                      coin.sprite[3], coin.sprite[4])
        for enemy in self.enemies:
            pyxel.blt(enemy.x, enemy.y, enemy.sprite[0], enemy.sprite[1], enemy.sprite[2],
                      enemy.sprite[3], enemy.sprite[4], colkey=6)
        pyxel.blt(self.flag.x, self.flag.y, self.flag.sprite[0], self.flag.sprite[1],
                  self.flag.sprite[2], self.flag.sprite[3], self.flag.sprite[4], colkey=6)
        pyxel.blt(self.castle.x, self.castle.y, self.castle.sprite[0], self.castle.sprite[1],
                  self.castle.sprite[2], self.castle.sprite[3], self.castle.sprite[4], colkey=6)
        self.show()
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0], self.mario.sprite[1],
                  self.mario.sprite[2], self.mario.sprite[3], self.mario.sprite[4], colkey=6)
        # when mario loses the game a new screen appear:
        if self.game_over_lost():
            pyxel.cls(0)
            pyxel.text(100, 128, "GAME OVER", 7)
            pyxel.text(90, 150, "press E to exit", 7)
        # when mario wins, a new screen appear:
        elif self.game_over_win():
            pyxel.cls(0)
            pyxel.text(80, 120, "CONGRATULATIONS !!!!", pyxel.frame_count % 16)
            pyxel.text(60, 150, "you passed the game successfully", 7)
            pyxel.text(90, 200, "(press E to exit)", 7)

    def start_jump(self):
        """This method starts mario's jump when the key is pressed"""
        self.is_jumping = True

    def mario_jump(self):
        """This method defines mario's jump. When the key is pressed the attribute self.jumping is
        True and the attribute self.jump_up is True until mario reaches the max height, then it starts
        falling again until he arrives to the floor, a pipe or an other type of block"""
        if self.is_jumping:
            jump_speed = 8
            if self.jump_up:
                self.mario.y -= jump_speed
                self.height_jump += jump_speed
                if self.height_jump >= self.height_max_jump or self.check_block_in_obstacle_up():
                    self.jump_up = False
            else:
                self.mario.y += jump_speed
                if self.check_block_in_obstacle_down():
                    self.jump_up = True
                    self.is_jumping = False
                    self.height_jump = 0
        if not self.jump_up or not self.is_jumping and not self.check_block_in_obstacle_down():
            self.start_drop()

    def start_drop(self):
        """This method establish that when mario arrives to the maximum height in the
        jump, it starts falling"""
        self.is_jumping = True
        self.jump_up = False

    def check_block_in_obstacle_down(self):
        """This method checks if mario is at the top of the elements"""
        for b in self.floor:
            if self.mario.collision_down(b):
                return True
        for p in self.pipes:
            if self.mario.collision_down(p):
                return True
        for b in self.special_blocks:
            if self.mario.collision_down(b):
                return True
        return False

    def check_block_in_obstacle_up(self):
        """This method checks if mario is under a block"""
        for b in self.special_blocks:
            if self.mario.collision_up(b):
                return True
        return False

    def block_right(self):
        """This method checks when mario find an obstacle going forward"""
        for p in self.pipes:
            if self.mario.collision_right(p):
                return True
        for b in self.special_blocks:
            if self.mario.collision_right(b):
                return True
        for p in self.floor:
            if self.mario.collision_right(p):
                return True
        if self.mario.x + 15 in range(self.castle.x - 15, self.castle.x):
            return True
        return False

    def block_left(self):
        """This method checks when mario find an obstacle going backward"""
        for p in self.pipes:
            if self.mario.collision_left(p):
                return True
        for b in self.special_blocks:
            if self.mario.collision_left(b):
                return True
        return False

    def create_enemies(self):
        """This method creates the enemies randomly
         the program will create a random number between 0 and 3
         0 for creating a koopa
         1, 2, and 3 for creating a goomba"""
        enemy = random.randint(0, 3)
        if enemy == 0:
            self.enemies.append(Koopa(230))
        else:
            self.enemies.append(Goomba(230))

    def mario_touch_enemies(self):
        """This method study if mario touches an enemy"""
        for element in self.enemies:
            if self.mario.x in range(element.x-8, element.x) and element.y == self.mario.y:
                return True
            elif self.mario.x in range(element.x+16, element.x+24) and element.y == self.mario.y:
                return True
            if self.mario.collision_down(element):
                self.enemies.remove(element)
                self.points += 200

    def mario_loses_life(self):
        """This method takes mario a life out when he touches an enemy"""
        if self.mario_touch_enemies():
            self.number_lives -= 1
            self.mario.sprite = (0, 0, 64, 16, 16)

    def enemies_change(self):
        """This method change the direction of the enemies when they reach an obstacle"""
        for p in self.pipes:
            for element in self.enemies:
                if element.collision_right(p):
                    element.direction = True
                elif element.collision_left(p):
                    element.direction = False
        for b in self.special_blocks:
            for element in self.enemies:
                if element.collision_right(b):
                    element.direction = True
                elif element.collision_left(b):
                    element.direction = False
        for t in self.floor:
            for element in self.enemies:
                if element.collision_right(t):
                    element.direction = True
                elif element.collision_left(t):
                    element.direction = False
        # when an enemy touches mario, it change its direction:
        for element in self.enemies:
            if self.mario_touch_enemies():
                if element.direction:
                    element.direction = False
                else:
                    element.direction = True

    def mario_touches_coin(self):
        """This method study if mario touches a coin"""
        for c in self.coins:
            if self.mario.collision_up(c) or (c.x == self.mario.x - 16 and c.y == self.mario.y + 16):
                self.number_coins += 1
                self.points += 100
                self.coins.remove(c)

    def mario_touches_block(self):
        """This method establishes what happens when mario collides with a special block. """
        for b in self.special_blocks:
            if b.block_type == 0 and self.mario.collision_up(b):
                # for the "?" block, mario can obtain 5 coins,
                # then it will become a clear block
                if self.counter < 5:
                    self.number_coins += 1
                    self.counter += 1
                    self.points += 100
                if self.counter == 5:
                    b.sprite = (0, 32, 0, 16, 16)
                    self.counter = 0
                    b.block_type = 2
            if b.block_type == 1 and self.mario.collision_up(b):
                # with the bricks blocks mario can only obtain
                # one coin, then they disappear
                self.number_coins += 1
                self.special_blocks.remove(b)
                self.points += 150

    def remove_tiles(self, x):
        """This method removes the tiles we don't want when building the obstacles"""
        for tile in self.floor:
            if tile.x == x:
                self.floor.remove(tile)

    def remove_bush(self, x):
        """This method removes the bushes we don't want when building the obstacles"""
        for bush in self.bush:
            if bush.x == x:
                self.bush.remove(bush)

    def game_over_lost(self):
        """This method checks when Mario loses the game"""
        if self.mario.y > 500 or self.number_lives < 0 or self.time_left < 0:
            return True

    def game_over_win(self):
        """This method checks when Mario wins the game"""
        if self.mario.x + 15 in range(self.castle.x - 15, self.castle.x):
            return True
