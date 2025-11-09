import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Colors
WHITE = (255, 255, 255)



RED = (255, 0, 0)

# Player settings
player_size = 50
player_x = 400
player_y = SCREEN_HEIGHT - player_size * 2
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_speed = 2
enemy_spawn_rate = 30  # Lower value means more enemies spawn frequently

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape from Enemies")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, ( x, y, player_size, player_size))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def main():
    running = True
    enemies = []
    global player_x
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed

        # Spawn enemies randomly
        if random.randint(0, enemy_spawn_rate) == 0:
            enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
            enemy_y = 0 - enemy_size
            enemies.append([enemy_x, enemy_y])

        for enemy in enemies:
            enemy[1] += enemy_speed
            draw_enemy(enemy[0], enemy[1])

            # Check collision with the player
            if (enemy[1] + enemy_size > player_y and enemy[1] < player_y + player_size and
                    enemy[0] + enemy_size > player_x and enemy[0] < player_x + player_size):
                print("Game Over!")
                running = False

        draw_player(player_x, player_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
