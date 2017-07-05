import random
# game options/settings
TITLE = "A pretty cool jumping game"
WIDTH = 960
HEIGHT = 680
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 1.25
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 25
# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 100, WIDTH, 100),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20),
                 (175, 100, 60, 20)]
#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
RANDOMCOLORBG = (random.randrange(0, 225),random.randrange(0, 225),random.randrange(0, 225))
RANDOMCOLORPLATFORM = (random.randrange(0, 225),random.randrange(0, 225),random.randrange(0, 225))
RANDOMCOLORSPRITE = (random.randrange(0, 225),random.randrange(0, 225),random.randrange(0, 225))

