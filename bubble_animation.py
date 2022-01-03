import pygame
import random
import constants

class Bubble:
    speed = 1 # define speed\
    color = constants.COLORS["Bubble"]

    def __init__(self, master, x, y, v, r):
        self.master = master
        self.x = x # x-axis
        self.y = y # y-axis
        self.v = v # constants.NUMBER
        self.r = r # r

        self.bubble = pygame.image.load("images/bubble1.png")
        self.bubble = pygame.transform.scale(self.bubble, (self.r * 2, self.r * 2))
        self.selected_bubble = pygame.image.load("images/bubble2.png")
        self.selected_bubble = pygame.transform.scale(self.selected_bubble, (self.r * 2, self.r * 2))

    def go_up(self):
        self.y -= constants.DR

    def go_down(self):
        self.y += constants.DR

    def draw(self, current=False):
        text = constants.font.render(str(self.v), 1, constants.COLORS["text"])
        if current:
            pygame.draw.circle(self.master, constants.COLORS["select"], (self.x, self.y), self.r)
        else:
            pygame.draw.circle(self.master, self.color, (self.x, self.y), self.r)
        text_width = text.get_width()
        text_height = text.get_height()
        self.master.blit(text, (self.x - text_width // 2, self.y - text_height // 2))
    
    def draw_picture(self, current = False):
        text = constants.font.render(str(self.v), 1, constants.COLORS["text"])
        if current:
            self.master.blit(self.selected_bubble, (self.x - self.r, self.y -self.r))
        else:
            self.master.blit(self.bubble, (self.x - self.r, self.y -self.r))
        text_width = text.get_width()
        text_height = text.get_height()
        self.master.blit(text, (self.x - text_width // 2, self.y - text_height // 2))
        
class BubbleManager:
    def __init__(self, master, x, height, arr=[]):
        self._master = master  # win
        self.bubblelist = []  # bubble list
        
        if arr:
            self.arr = arr
        else:
            self.arr = [i for i in range(1, constants.NUMBER)]
            random.shuffle(self.arr)

        for i in range(constants.NUMBER-1):
            v = self.arr[i]
            vr = constants.INIT_R + v * constants.DR  # raidus due to different numbers
            center_h = top_h + constants.BUBBLE_SPACE + vr  # height between the bubble's center to the bottom
            top_h = center_h + vr  # height between the bubble's toppest point to the bottom

            bubble_i = Bubble(master, x, constants.WIN_HEIGHT - center_h, v, vr)
            self.bubblelist.append(bubble_i)

        self.i = 0
        self.j = 0

        self.bubbling = False

        self.count = 0

    def draw(self):
        for j in range(len(self.bubblelist)):
            db = self.bubblelist[j]
            db.draw(j==self.j)

    def bubble_done(self):
        return self.i >= constants.NUMBER - 1

    def bubble_j(self):
        if not self.bubbling:
            return

        dbj0 = self.bubblelist[self.j]
        dbj1 = self.bubblelist[self.j+1]

        if dbj0.y - dbj0.r > dbj1.y + dbj1.r:
            #j bubble underneath
            dbj0.up()
            dbj1.down()
        elif dbj0.y > dbj1.y:
            # bubble intersect
            cy0 = dbj0.y
            dbj0.y = dbj1.y - dbj1.r + dbj0.r
            dbj1.y = cy0 - dbj1.r + dbj0.r
        elif (dbj1.y - dbj1.r) - (dbj0.y + dbj0.r) < constants.BUBBLE_SPACE:
            dbj0.up()
            dbj1.down()
        else:
            self.bubblelist[self.j] = dbj1
            self.bubblelist[self.j+1] = dbj0
            self.bubbling = False
            self.j += 1
            return

    def bubble_once(self):
        if self.j >= constants.NUMBER - self.i - 2:
            self.i += 1
            self.j = 0
        else:
            if self.arr[self.j] > self.arr[self.j + 1]:
                if self.count > 5:
                    self.count = 0
                else:
                    self.count += 1
                    return
                self.bubbling = True
                self.arr[self.j], self.arr[self.j + 1] = self.arr[self.j + 1], self.arr[self.j]
                self.bubble_j()
            else:
                if self.count > 10:
                    self.count = 0
                    self.j += 1
                else:
                    self.count += 1

    def draw_pic(self):
        for j in range(len(self.bubblelist)):
            db = self.bubblelist[j]
            db.draw_pic(j==self.j)


class Gui:
    def __init__(self, width, height, count, fps=constants.FPS, arr=[]):
        self.win = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        pygame.display.set_caption("Bubble sort animation")

        self.bmlist = []
        for i in range(1, count):
            x = constants.WIN_WIDTH // count * i
            bm = BubbleManager(self.win, x, constants.WIN_HEIGHT)
            self.bmlist .append(bm)

        self.start = False

    def start(self):
        while True:
            # Get all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # determine whether quit
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    # press any key and start
                    self.start = True

            if self.start:
                for bm in self.bmlist :
                    if bm.bubbling:
                        bm.bubble_j()
                    elif not bm.bubble_done():
                        bm.bubble_once()
                    else:
                        bm.j = -1

            self.win.fill(constants.COLORS["bg"])
            for bm in self.bmlist:
                bm.draw_pic()

            self.clock.tick(self.fps)
            pygame.display.update()


if __name__ == '__main__':
    gui = Gui(constants.WIN_WIDTH, constants.WIN_HEIGHT, 2)
    gui.start()      

