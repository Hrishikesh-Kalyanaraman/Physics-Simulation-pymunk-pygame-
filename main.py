import pygame
import sys
import pymunk
import random




"""def create_apple(pos, collision_type):  # Creating a physical body
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)  # Creating the object that experiences physics.
    body.position = pos  # Position of the above object
    shape = pymunk.Circle(body, 30)  # We are surrounding the above object with an invisible circle so that the object
    # reacts to stuff as if it's a circle. This makes calculations much easier. Note this is an invisible circle only
    # for pymunk. It has nothing to do with the visual output. Just used for calculations.
    body.velocity = (0, random.uniform(-400, 400))
    shape.elasticity = 1
    shape.density = 1
    shape.collision_type = collision_type
    space.add(body, shape)
    return shape


def draw_apples(a):  # Visualising the body
    global apples
    for apple in a:
        if apple.collision_type != 1:
            pygame.draw.circle(screen, (0, 0, 0), apple.body.position, 30)
        else:
            pygame.draw.circle(screen, (0, 0, 255), apple.body.position, 30)


def collide(arbiter, space, data):
    print("hello")


def change_to_blue(arbiter, space, data):
    for apple in apples:
        apple.collision_type = 1


pygame.init()  # Initiates the entire thing
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))  # (Width , Height)
space = pymunk.Space()  # Creating the "universe" where the entire simulation takes place.
# space.gravity = (0, 200)
apples = []
for i in range(100):
    apples.append(create_apple((random.randint(0, 600), random.randint(0, 600)), i+2))
apples.append(create_apple((400, 400), 1))

'''handler = space.add_collision_handler(2, 1)
handler.separate = collide'''
handlers = [space.add_collision_handler(2, i+2) for i in range(100)]
for i, handler in enumerate(handlers):
    handler.separate = apples[i]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Where QUIT refers to the X button that closes the program.
            pygame.quit()  # Opposite of the init thing. Closes the program
            sys.exit()
    screen.fill((255, 255, 255))  # red, green, blue colouration from 0-255. This line MUST ALWAYS BE IN THE LOOP.
    # The background has to be constantly updated as the ball is constantly moving. When screen.fill is applied,
    # the entire screen INCLUDING any objects (ie: the ball) is made into the background.
    # draw_static_ball(balls)
    draw_apples(apples)  # Drawing the apple is in a loop cause only the non-visual apple
    # (ie: the apple in create_apple) keeps moving. After the screen wipes everything, we draw the visual representation
    # of the ball. This cycle continues (ball gets erased, then redrawn in the new position of the non-visual ball.)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120) """