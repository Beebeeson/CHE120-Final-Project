import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DINO_COLOR = (0, 128, 0)
OBSTACLE_COLOR = (128, 0, 0)
JUMP_VELOCITY = -15
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dinosaur Game")

# Dinosaur class
class Dinosaur:
    def __init__(self):
        self.width = 40
        self.height = 60
        self.x = 50
        self.y = HEIGHT - self.height - 10
        self.vel_y = 0
        self.is_jumping = False

    def draw(self):
        pygame.draw.rect(screen, DINO_COLOR, (self.x, self.y, self.width, self.height))

    def update(self):
        if self.is_jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            if self.y >= HEIGHT - self.height - 10:
                self.y = HEIGHT - self.height - 10
                self.is_jumping = False
                self.vel_y = 0

    def jump(self):
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
    clock = pygame.time.Clock()
    dino = Dinosaur()
    obstacles = [Obstacle()]
    score = 0

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.jump()

        # Update dinosaur
        dino.update()

        # Update obstacles
        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw()

            # Check for collision
            if (dino.x + dino.width > obstacle.x and dino.x < obstacle.x + obstacle.width and
                    dino.y + dino.height > obstacle.y):
                print("Game Over! Your score was:", score)
                pygame.quit()
                sys.exit()

        # Add new obstacles
        if obstacles[-1].x < WIDTH - 300:
            obstacles.append(Obstacle())

        # Remove off-screen obstacles
        obstacles = [ob for ob in obstacles if ob.x > 0]

        # Draw dinosaur
        dino.draw()

        # Score (simplified)
        score += 1
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)  # 60 FPS

# Run the game
if __name__ == "__main__":
    main()
