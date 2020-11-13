import pygame

# import gym

pygame.init()
pygame.display.set_caption("REEEEEEEEEEEEEEEEEEEE")
board = pygame.display.set_mode((500, 500))
isRunning = True
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

while isRunning:
    board.fill((0, 0, 0))
    pygame.draw.line(board, (255, 255, 255), (500*0.4, 500*0.2), (500*.4, 500*.8))
    pygame.draw.line(board, (255, 255, 255), (500*0.6, 500*0.2), (500*.6, 500*.8))

    pygame.draw.line(board, (255, 255, 255), (500 * 0.2, 500 * 0.4), (500 * .8, 500 * .4))
    pygame.draw.line(board, (255, 255, 255), (500 * 0.2, 500 * 0.6), (500 * .8, 500 * .6))

    pygame.display.update()


    pos = pygame.mouse.get_pos()
    x = pos[0] / 500
    y = pos[1] / 500
    n = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for p, i in enumerate(square_pos):
                if i[0] < x < i[1] and i[2] < y < i[3]:
                    print(p)
