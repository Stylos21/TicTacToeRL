import pygame

# import gym

pygame.init()
pygame.display.set_caption("REEEEEEEEEEEEEEEEEEEE")
board = pygame.display.set_mode((500, 500))
isRunning = True

image_x = pygame.image.load("x.png")
image_o = pygame.image.load("o.png")

image_x = pygame.transform.scale(image_x, (100, 100))
image_o = pygame.transform.scale(image_o, (100, 100))
square_pos = [
    [0.2, 0.4, 0.2, 0.4],
    [0.4, 0.6, 0.2, 0.4],
    [0.6, 0.8, 0.2, 0.4],
    [0.2, 0.4, 0.4, 0.6],
    [0.4, 0.6, 0.4, 0.6],
    [0.6, 0.8, 0.4, 0.6],
    [0.2, 0.4, 0.6, 0.8],
    [0.4, 0.6, 0.6, 0.8],
    [0.6, 0.8, 0.6, 0.8],
]

moveHistory = []
vector_board = [[None for _ in range(3)] for __ in range(3)]
currentMove = 0

def draw_rects(surface, history):
    for move in history:
        if history.index(move) % 2:
            surface.blit(image_o, (square_pos[move][0] * 500, square_pos[move][2] * 500))

        else:
            surface.blit(image_x, (square_pos[move][0] * 500, square_pos[move][2] * 500))

    pygame.display.update()


def check_winner(state):
    ind = 0
    ind_diag = 0
    winnerExists = False
    # while not winnerExists:
    while not winnerExists and ind < 3:
        verticalCheck = state[0][ind] == state[1][ind] == state[2][ind] and state[0][ind] != '' and state[1][ind] != '' and state[2][ind] != ''
        horizontalCheck = state[ind] == ['x', 'x', 'x'] or state[ind] == ['o', 'o', 'o']
        hasDiagonalFilled = False
        print(verticalCheck or horizontalCheck)
        if verticalCheck or horizontalCheck:
            return state[0][ind] if verticalCheck else state[ind][0]

        else:ind += 1

        if state[0][0] == state[1][1] == state[2][2] and state[0][0] is not None and state[1][1] is not None and  state[0][0] is not None or state[0][2] == state[1][1] == state[2][0] and state[0][2] is not None and state[1][1] is not None and  state[2][0] is not None:
            return state[1][1]




board.fill((0, 0, 0))

while isRunning:

    pos = pygame.mouse.get_pos()
    x = pos[0] / 500
    y = pos[1] / 500
    n = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        pygame.draw.line(board, (255, 255, 255), (500 * 0.4, 500 * 0.2), (500 * .4, 500 * .8))
        pygame.draw.line(board, (255, 255, 255), (500 * 0.6, 500 * 0.2), (500 * .6, 500 * .8))

        pygame.draw.line(board, (255, 255, 255), (500 * 0.2, 500 * 0.4), (500 * .8, 500 * .4))
        pygame.draw.line(board, (255, 255, 255), (500 * 0.2, 500 * 0.6), (500 * .8, 500 * .6))
        # pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for p, i in enumerate(square_pos):
                row = p // 3
                col = p % 3
                if i[0] < x < i[1] and i[2] < y < i[3] and not vector_board[row][col]:
                    moveHistory.append(p)
                    currentPiece = 'o' if len(moveHistory) % 2 == 0 else 'x'
                    vector_board[row][col] = currentPiece
                    currentMove += 1

                    draw_rects(board, moveHistory)
                    winner = check_winner(vector_board)
                    print(winner)
        pygame.display.update()
