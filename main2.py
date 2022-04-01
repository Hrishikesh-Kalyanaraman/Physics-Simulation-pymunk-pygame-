import pygame
import sys
import pymunk

static_size = 50
dynamic_size = 40

def create_apple(pos):  # Creating a physical body
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)  # Creating the object that experiences physics.
    body.position = pos  # Position of the above object
    shape = pymunk.Circle(body, dynamic_size) # We are surrounding the above object with an invisible circle so that the object
    shape.elasticity = 1
    body.velocity = (100, 0)
    body.torque = 200
    # reacts to stuff as if it's a circle. This makes calculations much easier. Note this is an invisible circle only
    # for pymunk. It has nothing to do with the visual output. Just used for calculations.
    space.add(body, shape)
    return shape


def draw_apples(apples):  # Visualising the body
    for apple in apples:
        pygame.draw.circle(screen, (255, 255, 255), apple.body.position, dynamic_size)
    '''x = apple.body.position
    if int(x[1]) >= 120:
        pygame.draw.circle(screen, (0, 0, 0), apple.body.position, 80)'''


def create_static_ball(pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # No mass, inertia as it won't move.
    body.position = pos
    shape = pymunk.Circle(body, static_size)
    shape.elasticity = 1.0
    space.add(body, shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:
        pygame.draw.circle(screen, [179, 196, 54], ball.body.position, static_size)

def create_lines(pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # No mass, inertia as it won't move.
    body.position = pos
    shape = pymunk.Segment(body, static_size)
    shape.elasticity = 1.0
    space.add(body, shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pygame.draw.circle(screen, [179, 196, 54], ball.body.position, static_size)

pygame.init()  # Initiates the entire thing
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))  # (Width , Height)
space = pymunk.Space()  # Creating the "universe" where the entire simulation takes place.
space.gravity = (0, 0)
apples = []
balls = []
balls.append(create_static_ball((200, 500)))
balls.append(create_static_ball((500, 300)))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Where QUIT refers to the X button that closes the program.
            pygame.quit()  # Opposite of the init thing. Closes the program
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            apples.append(create_apple(event.pos))
    screen.fill((235, 0, 0))  # red, green, blue colouration from 0-255. This line MUST ALWAYS BE IN THE LOOP.
    # The background has to be constantly updated as the ball is constantly moving. When screen.fill is applied,
    # the entire screen INCLUDING any objects (ie: the ball) is made into the background.
    draw_static_ball(balls)
    """for apple in apples:
        print(apple.surface_velocity) """
    draw_apples(apples)  # Drawing the apple is in a loop cause only the non-visual apple
    # (ie: the apple in create_apple) keeps moving. After the screen wipes everything, we draw the visual representation
    # of the ball. This cycle continues (ball gets erased, then redrawn in the new position of the non-visual ball.)
    space.step(1/50)
    vertical_wall1 = pymunk.Segment(space.static_body, (-10, 0), (-10, 10000), 15)
    vertical_wall2 = pymunk.Segment(space.static_body, (1014, 0), (1014, 10000), 15)
    vertical_wall3 = pymunk.Segment(space.static_body, (-10, 615), (1014, 615), 15)
    vertical_wall4 = pymunk.Segment(space.static_body, (-10, -10), (1014, -10), 15)
    #vertical_wall.body.position = 100, 100
    vertical_wall1.elasticity = 1.0
    vertical_wall2.elasticity = 1.0
    vertical_wall3.elasticity = 1.0
    vertical_wall4.elasticity = 1.0
    space.add(vertical_wall1)
    space.add(vertical_wall2)
    space.add(vertical_wall3)
    space.add(vertical_wall4)
    #pygame.draw.line(screen, (255, 255, 255), (0, 200), (1000, 200), 15)
    pygame.display.update()
    clock.tick(120)