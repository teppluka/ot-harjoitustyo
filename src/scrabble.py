import pygame


class Scrabble:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((700, 700))

        self.create_tiles()
        self.loop()

    def loop(self):
        while True:
            self.input()
            self.render()

    def render(self):
        self.window.fill((120, 160, 160))

        for i in range(15*15):
            pygame.draw.rect(self.window, (200, 200, 200), (self.tilelist[i][0], self.tilelist[i][1], self.tilesize, self.tilesize))

        pygame.display.flip()
    
    def create_tiles(self):
        self.tilelist = []
        self.tilesize = 40
        self.gap = 5
        y = 15

        for i in range(15):
            x = 15
            for j in range(15):
                self.tilelist.append([x, y])
                x += self.tilesize + self.gap
            y += self.tilesize + self.gap
        
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()



if __name__ == "__main__":
    Scrabble()