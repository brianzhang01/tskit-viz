import tskit
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ts = tskit.load('example.trees')

print(ts.draw_text())

pygame.init()
width=1000
height=750
linewidth=3

screen = pygame.display.set_mode((width, height))
# background = pygame.Surface(screen.get_size(), 0, screen)
genome = pygame.Surface((width, 100), 0)
genome_offset = ((0, height-100))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    # background.fill((255, 255, 255))
    genome.fill(GREEN)
    # screen.blit(background, (0, 0))
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
