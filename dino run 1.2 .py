'''
libraries-----------------------------------------------------------------------------------------------------------
'''


import pygame
import random
import sys
import sprite_anim


'''
game variables and settings-----------------------------------------------------------------------------------------
'''


# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
OBSTACLE_COLOR = (128, 0, 0)

# Scroll multiplier (not working)
scroll = 0

# game physics
JUMP_VELOCITY = -15
DOUBLE_JUMP_VELOCITY = -12  # Velocity for the second jump
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrome Dinosaur Game")

# dino animation and sprite:
sprite_image = pygame.image.load('DinoSprites - vita.png').convert_alpha()
sprite = sprite_anim.spriteSheet(sprite_image) # create instance for the class

# create list of frames to animate:
animation_list = []
animation_step = 8

# adding corresponding sprites to animation list
for steps in range(animation_step):
    animation_list.append(sprite.get_image(steps,24,24,3,BLACK))

# generate list of background layers
bg_layers = []
for i in range (1,6):
    bg_img = pygame.image.load(f'plx-{i}.png').convert_alpha()
    bg_img = pygame.transform.scale (bg_img, (384*2,216*2))
    bg_layers.append(bg_img) 
bg_width = bg_layers[0].get_width()


'''
game functions------------------------------------------------------------------------------------------------------
'''
# draw a scrolling background (scrolling not working)
def draw_bg():
    for x in range(50):
        speed = 0.5
        for i in bg_layers:
            screen.blit(i,((x*bg_width)-scroll*speed,0))
            speed += 0.2

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

    #def draw(self):
    #pygame.draw.rect(screen, DINO_COLOR, (self.x, self.y, self.width, self.height))
    def get_position(self): # the fucntion to return the current position of dino, used for updateing sprite to match actual dino position
        x_pos = self.x
        y_pos = self.y
        return (x_pos,y_pos)

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


'''
main game loop------------------------------------------------------------------------------------------------------
'''


def main():
    clock = pygame.time.Clock()
    dino = Dinosaur()
    obstacles = [Obstacle()]
    score = 0
    run = True
    scroll = 0
    
    # animation frame updates 
    last_update = pygame.time.get_ticks()
    animation_cooldown = 120
    frame = 3

    while run:
        #load background to screen
        screen.fill(WHITE)
        draw_bg()
        scroll += 2.5
        
        #draw a simple ground
        pygame.draw.rect(screen,(92,64,51),(0,380,600,20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False
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
        screen.blit(animation_list[frame],dino.get_position())
        
        #update dino's sprite animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time 
            if frame >= len(animation_list):
                frame = 3

        # Score (simplified)
        score += 1
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)  # 60 FPS
        
        

'''
Run the game--------------------------------------------------------------------------------------------------------
'''


if __name__ == "__main__":
    main()
