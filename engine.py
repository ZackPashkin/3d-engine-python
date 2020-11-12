import pygame as pg

class Render:
    def __init__(self):
        pg.__init__
        self.resolution = self.width, self.height = 1280, 720
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        
    def draw(self):
        self.screen.fill(pg.Color('black'))
    
    def run(self):
        while True:
            self.draw()
            [exit() for _ in pg.event.get() if _.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = Render()
    app.run()