import pygame
import sys

# Initialize Pygame
pygame.init()


WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE


BACKGROUND_COLOR = (240, 240, 240)
LINE_COLOR = (0, 0, 0)
HOVER_COLOR = (200, 200, 200)
X_COLOR = (128, 0, 128)  # Purple
O_COLOR = (255, 255, 0)  # Yellow


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def draw_board():
    screen.fill(BACKGROUND_COLOR)

    
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

   
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    # X and O
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            draw_cell(row, col)


def draw_cell(row, col):
    x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
    cell_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

    if board[row][col] == 'X':
        pygame.draw.line(screen, X_COLOR, cell_rect.topleft, cell_rect.bottomright, LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, cell_rect.bottomleft, cell_rect.topright, LINE_WIDTH)
    elif board[row][col] == 'O':
        pygame.draw.circle(screen, O_COLOR, cell_rect.center, SQUARE_SIZE // 2 - LINE_WIDTH // 2, LINE_WIDTH)


def check_win():
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def check_tie():
    return all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Main game loop
turn = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = turn
                if check_win():
                    print(f"{turn} wins!")
                    running = False
                elif check_tie():
                    print("It's a tie!")
                    running = False
                else:
                    turn = 'O' if turn == 'X' else 'X'

    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    hover_row, hover_col = mouse_y // SQUARE_SIZE, mouse_x // SQUARE_SIZE
    if 0 <= hover_row < BOARD_SIZE and 0 <= hover_col < BOARD_SIZE:
        pygame.draw.rect(screen, HOVER_COLOR, (hover_col * SQUARE_SIZE, hover_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    draw_board()
    pygame.display.flip()


pygame.time.delay(2000)
pygame.quit()
