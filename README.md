# Super Mario Bros — Pyxel Edition

A side-scrolling platformer inspired by the original *Super Mario Bros.*, written in Python with the [Pyxel](https://github.com/kitao/pyxel) retro game engine. It was built as a first-year university Programming project to practise object-oriented design: every element on screen (Mario, enemies, blocks, pipes, coins…) is its own class, and a central `Board` class handles the game loop, collisions and scoring.

![Mario](assets/mario.png)

## Features

- **A full scrolling level** (about 2,300 px wide) with pipes, gaps, staircases, floating platforms and a flag and castle at the end.
- **Jumping and collisions**: Mario jumps up to 3 blocks high and lands on the floor, pipes and blocks.
- **Enemies**: Goombas and Koopas spawn at random (at most 4 at once) and turn around when they hit an obstacle. Jump on them to defeat them.
- **Special blocks**:
  - `?` blocks give up to 5 coins, then turn into empty blocks.
  - Brick blocks give one coin and break.
- **Collectable coins** spread across the level.
- **HUD** showing score, lives, coins and a countdown timer.
- **Background music** that loops during the game.
- **Win and game-over screens**.

## Controls

| Key         | Action           |
|-------------|------------------|
| `→`         | Move right       |
| `←`         | Move left        |
| `Space`     | Jump             |
| `E`         | Quit the game    |

## Rules and scoring

| Event                      | Points |
|----------------------------|--------|
| Collect a coin             | +100   |
| Hit a `?` block            | +100   |
| Break a brick block        | +150   |
| Stomp on an enemy          | +200   |

- You start with **3 lives** and **400 seconds**.
- Touching an enemy from the side costs a life.
- You **lose** if you run out of lives, run out of time, or fall into a gap.
- You **win** when you reach the castle at the end of the level.

## Requirements

- Python 3
- Pyxel **1.4.x or older**. The game calls `pyxel.init(..., caption=...)`, which newer Pyxel versions renamed to `title=`.

```bash
pip install "pyxel<1.5"
```

## How to run

From the project root (the game loads its assets through relative paths):

```bash
python main.py
```

## Project structure

```
mario-bros-game/
├── main.py            # Entry point: sets up Pyxel, loads assets and music, starts the loop
├── board.py           # Board class: level layout, game loop, collisions, HUD, win/lose logic
├── mario.py           # Mario: position, sprite, movement and collision checks
├── goomba.py          # Goomba enemy
├── koopa.py           # Koopa enemy (walks back and forth over a fixed distance)
├── special_blocks.py  # "?" blocks and brick blocks
├── coins.py           # Collectable coins
├── floor.py           # Ground tiles
├── pipes.py           # Pipes
├── bushes.py          # Decorative bushes
├── clouds.py          # Decorative clouds
├── flag.py            # Goal flag
├── castle.py          # Final castle
└── assets/
    ├── resources.pyxres   # Sprites, tilemaps and music used by the game
    └── ...                # Other images and Pyxel resource files
```

### How it works

- `main.py` creates a 256×256 `Board`, loads `assets/resources.pyxres`, starts the music and hands `Board.update` and `Board.draw` to `pyxel.run`.
- Mario moves freely until he reaches the middle of the screen. After that, the level scrolls: every other object moves left through its `move_right()` method.
- Each game object stores its sprite as a tuple `(image_bank, u, v, width, height)` that points into the Pyxel resource file.
- Classes use properties with setters to validate their attributes (for example, coordinates must be integers).

## Credits

This is a fan-made educational project. *Super Mario Bros.* and its characters are trademarks of Nintendo.
