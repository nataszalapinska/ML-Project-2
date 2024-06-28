import pygame
import sys

pygame.init()

# Constants: sizes of elements
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (224, 224, 224)
LINE_COLOR = (255, 255, 0)
CIRCLE_COLOR = (25, 0, 51)
CROSS_COLOR = (102, 0, 204)

# Display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board settings
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]

# Functions
def draw_lines():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_winning_line(row, 0, row, 2)
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_winning_line(0, col, 2, col)
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_winning_line(0, 0, 2, 2)
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        draw_winning_line(0, 2, 2, 0)
        return True

    return False

def draw_winning_line(row1, col1, row2, col2):
    pygame.draw.line(screen, (255, 0, 0), (col1 * SQUARE_SIZE + SQUARE_SIZE // 2, row1 * SQUARE_SIZE + SQUARE_SIZE // 2),
                     (col2 * SQUARE_SIZE + SQUARE_SIZE // 2, row2 * SQUARE_SIZE + SQUARE_SIZE // 2), 4)

# Game loop
player = 'X'
running = True
game_over = False

while running:
    draw_lines()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = 'O' if player == 'X' else 'X'

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                player = 'X'

    draw_figures()

    pygame.display.update()

    if game_over and is_board_full():
        pygame.time.wait(300)
        game_over = False
        player = 'X'

    clock = pygame.time.Clock()
    clock.tick(60)

pygame.quit()
