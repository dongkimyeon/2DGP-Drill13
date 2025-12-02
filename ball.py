from pico2d import *
import game_world
import game_framework
import random
import common
class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(50,  common.court.w - 50)
        self.y = random.randint(50, common.court.w - 50)

    def draw(self):
        sx, sy = common.court.to_screen(self.x, self.y)
        self.image.draw(sx, sy)


    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)

