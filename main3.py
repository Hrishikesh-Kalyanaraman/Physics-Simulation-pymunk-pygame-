import pygame
import sys

# General Setting
pygame.init()  # Initiates the entire thing
clock = pygame.time.Clock()
# Main display
screen = pygame.display.set_mode((1000, 600))  # (Width , Height)
screen.fill((255, 255, 255))  # red, green, blue colouration from 0-255.
second_surface = pygame.Surface([100, 200])
second_surface.fill([0, 0, 255])
building = pygame.image.load('building.JPG')
building_rect = building.get_rect(topleft=[200, 259])
#  print(building_rect.w, where w shows the width of the image. Can also use h to find height.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Where QUIT refers to the X button that closes the program.
            pygame.quit()  # Opposite of the init thing. Closes the program
            sys.exit()
    screen.fill((255, 255, 255))  # red, green, blue colouration from 0-255.
    screen.blit(second_surface, (0, 50))
    screen.blit(building, building_rect)
    building_rect.right += 5
    print(building_rect.right)
    pygame.display.flip()  # Keeps updating the screen so that the new screen isn't super-imposed on the old screen.
    # Same as display.flip(), except in update you can choose to update only certain screens.
    # flip always updates entire output.
    clock.tick(60)