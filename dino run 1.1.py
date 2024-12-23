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
DOUBLE_JUMP_VELOCITY = -12  # Velocity for the second jump
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
        self.jump_count = 0  # 0 for no jump (walking), 1 for single jump, 2 for double jump

    def draw(self):
        pygame.draw.rect(screen, DINO_COLOR, (self.x, self.y, self.width, self.height))

    def update(self):
        if self.is_jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            if self.y >= HEIGHT - self.height - 10:  # Ensure the dinosaur is at above the ground
                self.y = HEIGHT - self.height - 10
                self.is_jumping = False
                self.vel_y = 0
                self.jump_count = 0  # Reset jump count when on the ground

    def jump(self):
        if self.jump_count == 0:  # Single jump
            self.is_jumping = True
            self.vel_y = JUMP_VELOCITY
            self.jump_count = 1
        elif self.jump_count == 1:  # Double jump
            self.vel_y = DOUBLE_JUMP_VELOCITY
            self.jump_count = 2

# Obstacle class
class Obstacle:
    def __init__(self):
        self.width = 20
        self.height = random.randint(40, 80)  # Random height for obstacles, can go higher
        self.x = WIDTH
        self.y = HEIGHT - self.height - 10

    def draw(self):
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x -= 5
        if self.x < 0:
            self.x = WIDTH
            self.height = random.randint(40, 80)  # Reset height for new obstacles

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
                # If the dinosaur is in a double jump and passes through the obstacle, continue the game
                if dino.jump_count == 2 and dino.y <= obstacle.y:
                    continue  # Allow passing through the obstacle during double jump
                else:
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
