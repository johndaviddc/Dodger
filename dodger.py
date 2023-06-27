import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dodger")

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_size = 50
player_color = (255, 255, 0)
player_x = WINDOW_WIDTH // 2 - player_size // 2
player_y = WINDOW_HEIGHT - player_size
player_speed = 10

# Set up the enemy
enemy_size = 50
enemy_color = (255, 0, 0)
enemy_x = random.randint(0, WINDOW_WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

# Set up the score
score = 0
font = pygame.font.SysFont(None, 30)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_size:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > WINDOW_HEIGHT:
        enemy_x = random.randint(0, WINDOW_WIDTH - enemy_size)
        enemy_y = -enemy_size
        score += 1
        enemy_speed += 1

    # Check for collision
    if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
        pygame.quit()
        quit()

    # Draw the game objects
    window.fill((0, 0, 0))
    pygame.draw.rect(window, player_color, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, enemy_color, (enemy_x, enemy_y, enemy_size, enemy_size))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
    