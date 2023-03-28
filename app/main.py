import pygame


BG_COLOR = 255, 255, 200

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([500, 500])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Jogo da Velha")
        self.running = True
        self.markers = [[0] * 3 for _ in range(3)]
        self.pos = None
        self.clicks = 0
        self.player = 1

    def create_board(self):
        self.screen.fill(BG_COLOR)
        for line in range(0, 2):
            pygame.draw.line(
                self.screen,
                'black',
                [50, 166+(line * 166)], [450, 166+(line * 166)], 6
            )
            pygame.draw.line(
                self.screen,
                'black',
                [166 + (line * 166), 50], [166 + (line * 166), 450], 6
            )

    def draw_marks(self):
        pos_x = 0
        for x in self.markers:
            pos_y = 0
            for y in x:
                if y == 1:
                    self.mark1(pos_x, pos_y)
                elif y == -1:
                    self.mark2(pos_x, pos_y)
                pos_y += 1
            pos_x += 1

    def check_victory(self):
        print('verificando vencedor')
        for line in self.markers:
            if sum(line) == 3:
                print("player 1 Wins!")
                # self.running = False
                break
            elif sum(line) == -3:
                print("player 2 Wins!")
                # self.running = False
                break

    def run(self):
        self.create_board()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3)[0]:
                        self.pos = pygame.mouse.get_pos()
                        p_x, p_y = self.pos
                        if self.markers[p_x//166][p_y//166] == 0:
                            if self.player == 1:
                                self.markers[p_x // 166][p_y // 166] = 1
                                self.player = 2
                            else:
                                self.markers[p_x // 166][p_y // 166] = -1
                                self.player = 1
                            self.draw_marks()
                            self.clicks += 1
                        else:
                            pass
                        if self.clicks >= 5:
                            self.check_victory()
            self.clock.tick(60)
            pygame.display.update()

    def mark1(self, p_x, p_y):
        pygame.draw.line(
            self.screen,
            'blue',
            [(p_x * 166) + 34, 34 + (p_y * 166)],
            [(p_x * 166) + 132, (p_y * 166) + 132],
            4
        )
        pygame.draw.line(
            self.screen,
            'blue',
            [(p_x * 166) + 34, (p_y * 166) + 132],
            [(p_x * 166) + 132, (p_y * 166) + 34],
            4
        )

    def mark2(self, p_x, p_y):
        pygame.draw.circle(
            self.screen, 'green', [166 * p_x + 83, 166 * p_y + 83], 66, 4
        )


Game().run()
pygame.quit()
