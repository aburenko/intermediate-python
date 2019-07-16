import pygame
from OOP.Blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 10


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


def draw_environment(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_index in blob_dict:
            blob = blob_dict[blob_index]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    pygame.display.update()


def main():
    red_blobs = dict(enumerate([Blob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    blue_blobs = dict(enumerate([Blob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([red_blobs, blue_blobs])
        clock.tick(60)


if __name__ == '__main__':
    main()

