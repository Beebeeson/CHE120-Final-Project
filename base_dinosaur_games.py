#BQ: Benson Qiu, TL: Taixi Liu
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400 # BQ: set size for game window
#BQ: colors set as tuples that correspond to RGB values of the color. 0 ~ 255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DINO_COLOR = (0, 128, 0)
OBSTACLE_COLOR = (128, 0, 0)
# BQ: variables assigned for jumping physics, positive sign is downwards so an upwards velocity need to be negative
JUMP_VELOCITY = -15
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dinosaur Game")

# Dinosaur class
class Dinosaur:
    def __init__(self): #BQ: an ibnitialize statement creates new values that will be refernced, which is exclusive and is local to this class and its methods
        self.width = 40
        self.height = 60
        self.x = 50
        self.y = HEIGHT - self.height - 10 #BQ:y position need to be represented as dino's-height-pixels away from bottom of the screen (HEIGHT). add 10 pixels from floor to make sure dino does not collide with the floor and causes game to be over
        self.vel_y = 0 #BQ only y-component velocity is needed since teh dino is actually not moving horizontally reletive to the screen, only obstacles are!
        self.is_jumping = False

    def draw(self):
        pygame.draw.rect(screen, DINO_COLOR, (self.x, self.y, self.width, self.height)) # BQ: draw the dino character, represented by a simple rectangle

    def update(self): # BQ: update velocity of dino by adding value of gravity as acceleration to the velocity, causing dino to decrease in vertical velcoty and eventually fall back down during a jump
        if self.is_jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            if self.y >= HEIGHT - self.height - 10: # BQ: checking collision with ground, if dino has fell beyond ground height, reset its position to the default hight (10 pixels above ground level)
                self.y = HEIGHT - self.height - 10
                self.is_jumping = False
                self.vel_y = 0 # BQ: turn off jumping and reset its velocity so dino doesnt accelerate through the floor

    def jump(self):# BQ: initiate jumping by setting vertical velocity to jump velocity and enables gravity acceleration
        if not self.is_jumping:
            self.is_jumping = True
            self.vel_y = JUMP_VELOCITY

# Obstacle class
class Obstacle:
    def __init__(self):
        self.width = 20
        self.height = 40
        self.x = WIDTH
        self.y = HEIGHT - self.height - 10

    def draw(self):
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))

    def update(self): 
        self.x -= 5
        if self.x < 0: 
            self.x = WIDTH
            self.height = random.randint(20, 40)

# Main game function
def main():
    clock = pygame.time.Clock() # BQ: creates a clock to help set the framerate
    dino = Dinosaur() # BQ: craetes instance in class
    obstacles = [Obstacle()] # BQ: since there will be multiple obstacles, the variable will be a list of all objects on the screen
    score = 0 # BQ: initialize score

    while True: # BQ: a loop that runs forver to check for user key inputs
        screen.fill(WHITE) #BQ: fill in background layer
        for event in pygame.event.get(): #BQ: if a QUIT event is detected, deactivate pygame library and quits the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #BQ: mapping inputs to jump
                dino.jump()

        # Update dinosaur
        dino.update()

        # Update obstacles
        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw()

            # Check for collision
            if (dino.x + dino.width > obstacle.x and dino.x < obstacle.x + obstacle.width and
                    dino.y + dino.height > obstacle.y): # BQ: if dinosaur is inside the obtable, game over, quits game window and displays score
                print("Game Over! Your score was:", score)
                pygame.quit()
                sys.exit()

        # Add new obstacles
        if obstacles[-1].x < WIDTH - 300:
            obstacles.append(Obstacle())

        # Remove off-screen obstacles
        obstacles = [ob for ob in obstacles if ob.x > 0]

        # Draw dinosaur
        dino.draw() #BQ: updates dinosaur position every game frame

        # Score (simplified)
        score += 1 # BQ: score is acculuated per frame while the game runs. 
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)  # 60 FPS

# Run the game
if __name__ == "__main__":
    main()
