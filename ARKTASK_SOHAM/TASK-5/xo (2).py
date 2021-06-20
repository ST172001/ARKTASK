from typing import Tuple
import pygame
import sys
import time



class Const:
    dim = 3
    num_win = 3
    # state of the cell in the broad
    Undefined = 0
    X = 1
    O = -1
    # define for draw
    cell_dim = 100
    line_width = 4
    x_width = 15
    x_margin = 15
    o_width = 10
    o_rad = 35
    font_size = 40
    line_color = (180, 250, 255)
    x_color = (255, 0, 0)
    o_color = (0, 255, 0)


class Mouse:
    left = 1
    middle = 2
    right = 3
    scroll_up = 4
    scroll_down = 5


def create_broad(size: int) -> list:
    broad = [[0 for r in range(size)] for c in range(size)]
    return broad


def draw_broad(broad: list):
    num = len(broad)
    broad_dim = num * Const.cell_dim
    pygame.init()
    screen = pygame.display.set_mode([broad_dim, broad_dim])
    pygame.display.set_caption("TICTACTOE")
    screen.fill(pygame.Color("Gray"))
    for line in range(1, num):
        pygame.draw.line(screen, Const.line_color, (0, line * Const.cell_dim), (broad_dim, line * Const.cell_dim),
                         Const.line_width)
        pygame.draw.line(screen, Const.line_color, (line * Const.cell_dim, 0), (line * Const.cell_dim, broad_dim),
                         Const.line_width)
    return screen


def draw_xo(screen, broad: list):
    l = len(broad)
    for row in range(l):
        for col in range(l):
            if broad[row][col] == Const.X:
                pygame.draw.line(screen, Const.x_color,
                                 (row * Const.cell_dim + Const.x_margin, col * Const.cell_dim + Const.x_margin),
                                 (row * Const.cell_dim + (Const.cell_dim - Const.x_margin), col * Const.cell_dim + (Const.cell_dim - Const.x_margin)),
                                 Const.x_width)
                pygame.draw.line(screen, Const.x_color,
                                 (row * Const.cell_dim + (Const.cell_dim - Const.x_margin), col * Const.cell_dim + Const.x_margin),
                                 (row * Const.cell_dim + Const.x_margin, col * Const.cell_dim + (Const.cell_dim - Const.x_margin)),
                                 Const.x_width)
            elif broad[row][col] == Const.O:
                pygame.draw.circle(screen, Const.o_color, (row * Const.cell_dim + Const.cell_dim / 2, col * Const.cell_dim + Const.cell_dim / 2),
                                   Const.o_rad, Const.o_width)


def xy_to_row_col(pos: tuple) -> Tuple[int, int]:
    row = pos[0] // Const.cell_dim
    col = pos[1] // Const.cell_dim
    return row, col


def check_win(broad: list, row, col):
    num = len(broad) - 1
    player = broad[row][col]
    # check vertical
    conti = 1
    x = row
    while x > 0:
        x -= 1
        if broad[x][col] == player:
            conti += 1
        else:
            break
    x = row
    while x < num:
        x += 1
        if broad[x][col] == player:
            conti += 1
        else:
            break
    if conti == Const.num_win:
        return player
    # check horizontal
    conti = 1
    y = col
    while y > 0:
        y -= 1
        if broad[row][y] == player:
            conti += 1
        else:
            break
    y = col
    while y < num:
        y += 1
        if broad[row][y] == player:
            conti += 1
        else:
            break
    if conti == Const.num_win:
        return player
    # check diagonal 1
    conti = 1
    x = row
    y = col
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if broad[x][y] == player:
            conti += 1
        else:
            break
    x = row
    y = col
    while x < num and y < num:
        x += 1
        y += 1
        if broad[x][y] == player:
            conti += 1
        else:
            break
    if conti == Const.num_win:
        return player
    # check diagonal 1
    conti = 1
    x = row
    y = col
    while x > 0 and y < num:
        x -= 1
        y += 1
        if broad[x][y] == player:
            conti += 1
        else:
            break
    x = row
    y = col
    while x < num and y > 0:
        x += 1
        y -= 1
        if broad[x][y] == player:
            conti += 1
        else:
            break
    if conti == Const.num_win:
        return player
    return Const.Undefined

def remain_move(board):
    num = len(broad)
    for r in range(num):
        for c in range(num):
            if board[r][c] == Const.Undefined:
                return True
    return False

class Bot:
    MAX = 10
    MIN = -10
    DRAW = 0
    MAXINT = 1000

    def __init__(self, player, broad):
        self.player = player
        self.broad = broad

    def minimax(self, row, col, depth, player):
        winner = check_win(self.broad, row, col)
        if winner == self.player:
            return Bot.MAX - depth
        if winner == -self.player:
            return Bot.MIN + depth
        if not remain_move(self.broad):
            return Bot.DRAW
        num = len(self.broad)
        if player == self.player: # case MAX
            best = -Bot.MAXINT
            for r in range(num):
                for c in range(num):
                    if self.broad[r][c] == Const.Undefined:
                        self.broad[r][c] = player
                        value = self.minimax(r, c, depth+1, -player)
                        best = max(best, value)
                        self.broad[r][c] = Const.Undefined
        else:   # case MIN
            best = Bot.MAXINT
            for r in range(num):
                for c in range(num):
                    if self.broad[r][c] == Const.Undefined:
                        self.broad[r][c] = player
                        value = self.minimax(r, c, depth+1, -player)
                        best = min(best, value)
                        self.broad[r][c] = Const.Undefined
        return best

    def find_best_cell(self):
        row = None
        col = None
        best_score = -Bot.MAXINT
        num = len(self.broad)
        for r in range(num):
            for c in range(num):
                if self.broad[r][c] == Const.Undefined:
                    self.broad[r][c] = self.player
                    score = self.minimax(r, c, 0, -self.player)
                    self.broad[r][c] = Const.Undefined
                    if score > best_score:
                        row = r
                        col = c
                        best_score = score
        return row, col


if __name__ == "__main__":
    pygame.init()
    size = Const.dim
    screen = None
    font = None
    broad = None

    argv = sys.argv
    if len(argv) > 1:
        size = int(argv[1])

    broad = create_broad(size=size)
    font = pygame.font.SysFont(None, Const.font_size)
    bot = Bot(Const.Undefined, broad)

    img = font.render("Select X or O", True, (0, 255, 0))
    screen = pygame.display.set_mode((300, 200))
    screen.fill("AliceBlue")
    screen.blit(img, (20, 50))
    pygame.draw.rect(screen, "gray", (50, 100, 50, 50))
    img = font.render("X", False, (255, 0, 0))
    screen.blit(img, (65, 115))
    pygame.draw.rect(screen, "gray", (200, 100, 50, 50))
    img = font.render("O", False, (0, 255, 0))
    screen.blit(img, (215, 115))
    pygame.display.update()
    while bot.player == Const.Undefined:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == Mouse.left:
            x, y = pygame.mouse.get_pos()
            if 50 < x < 100 and 100 < y < 150: # player choose X
                bot.player = Const.O
            elif 200 < x < 250 and 100 < y < 150: # player choose O
                bot.player = Const.X

    screen = draw_broad(broad=broad)
    pygame.display.update()
    running = True
    player = Const.X
    winner = Const.Undefined
    while running:
        if player == bot.player:
            row, col = bot.find_best_cell()
            broad[row][col] = player
            player = Const.X if player == Const.O else Const.O
        else:
            pygame.event.clear()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    running = False
                    break

                if winner == Const.Undefined:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == Mouse.left:
                        pos = pygame.mouse.get_pos()
                        row, col = xy_to_row_col(pos)
                        if broad[row][col] == 0:
                            broad[row][col] = player
                            player = Const.X if player == Const.O else Const.O
                            break

        draw_xo(screen=screen, broad=broad)
        winner = check_win(broad=broad, row=row, col=col)
        if winner != Const.Undefined:
            text = "Player {} wins!".format("x" if winner == Const.X else "O")
            img = font.render(text, True, (0, 255, 0))
            pygame.draw.rect(screen, (120, 130, 0), (80, 120, 200, 40))
            screen.blit(img, (80, 130))
            running = False
        elif not remain_move(broad):
            text = "Draw!!!"
            img = font.render(text, True, (0, 255, 0))
            pygame.draw.rect(screen, (120, 130, 0), (80, 120, 200, 40))
            screen.blit(img, (80, 130))
            running = False
        pygame.display.update()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            break
    exit(0)
