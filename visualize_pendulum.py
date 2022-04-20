import glob
import re
import sys
import time

import numpy as np
import pygame

from coordinates1 import coordinate1_filepaths

if __name__ == '__main__':
    coord_paths_iter = coordinate1_filepaths.values().__iter__()

    # Doing pygame stuff!
    pygame.init()
    surface = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Random starting position generator")

    surface.fill((255, 255, 255))
    pygame.display.update()

    frame_index = -1
    green_coords = []
    purple_coords = []

    while True:
        time.sleep(0.01)

        if len(green_coords) and len(purple_coords) and 0 <= frame_index < green_coords.shape[1]:
            # print('hi', green_coords)
            surface.fill((255, 255, 255))

            green_pos = np.flip(green_coords[:, frame_index])
            purple_pos = np.flip(purple_coords[:, frame_index])

            pygame.draw.circle(surface, color='green', center=green_pos, radius=5)
            pygame.draw.circle(surface, color='purple', center=purple_pos, radius=5)
            frame_index += 1

            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    coord_paths = coord_paths_iter.__next__()
                    if coord_paths:
                        green_coords = np.load(coord_paths['green'])
                        purple_coords = np.load(coord_paths['purple'])
                        print(green_coords)
                        print(green_coords.shape)
                        frame_index = 0
