import tskit
import pygame
from pygame.locals import *
import time

# TODO: change this to an Enum
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ts = tskit.load('example.trees')
breakpoints = list(ts.breakpoints())
# print(ts.draw_text())
ready_for_press = True

pygame.init()
width=1000
height=750
linewidth=3
genome_height = 100 # showing genome, positioned at bottom
tree_index = 0 # starting tree index

screen = pygame.display.set_mode((width, height))
genome = pygame.Surface((width, genome_height), 0)
margin = genome_height // 2

genome_offset = ((0, height-genome_height))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    if ready_for_press:
        if pressed_keys[K_LEFT]:
            ready_for_press = False
            tree_index -= 1
            if tree_index < 0:
                tree_index = 0
            print(tree_index)
        if pressed_keys[K_RIGHT]:
            ready_for_press = False
            tree_index += 1
            if tree_index >= len(breakpoints) - 1:
                tree_index = len(breakpoints) - 2
            print(tree_index)
    if not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
        ready_for_press = True

    # time.sleep(0.1)

    screen.fill(WHITE)
#    genome.fill(GREEN)
    pygame.draw.line(genome, BLACK, (margin, margin), (width - margin, margin), linewidth)
    genome_extent = width - 2*margin
    for i, b in enumerate(breakpoints):
        x = int(margin + genome_extent * (b / breakpoints[-1]))
        if i == tree_index or i == tree_index + 1:
            vertical_color = RED
        else:
            vertical_color = BLACK
        pygame.draw.line(
            genome, vertical_color, (x, margin // 2), (x, genome_height - margin // 2), linewidth)
    tree_start = int(margin + genome_extent * (breakpoints[tree_index] / breakpoints[-1]))
    tree_end = int(margin + genome_extent * (breakpoints[tree_index + 1] / breakpoints[-1]))
    pygame.draw.line(genome, RED, (tree_start, margin), (tree_end, margin), linewidth)

    screen.blit(genome, genome_offset)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()




# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#         elif event.type == QUIT:
#             running = False
#         elif(event.type == ADDENEMY):
#             new_enemy = Enemy()
#             enemies.add(new_enemy)
#             all_sprites.add(new_enemy)
#     screen.blit(background, (0, 0))
#     pressed_keys = pygame.key.get_pressed()
#     player.update(pressed_keys)
#     enemies.update()
#     for entity in all_sprites:
#         screen.blit(entity.surf, entity.rect)

#     if pygame.sprite.spritecollideany(player, enemies):
#         player.kill()

#     pygame.display.flip()
