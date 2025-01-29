import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Snake and food size
SNAKE_SIZE = 10
SNAKE_SPEED = 15

# Font
font = pygame.font.SysFont("bahnschrift", 25)

# Function to display the score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, [10, 10])

# Function to draw the snake
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], SNAKE_SIZE, SNAKE_SIZE])

# Function to display game over message
def message(msg, color, x, y):
    text = font.render(msg, True, color)
    win.blit(text, [x, y])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x, y = WIDTH / 2, HEIGHT / 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    # Generate food position
    food_x = random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10
    food_y = random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10

    score = 0  # Initialize score

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            win.fill(WHITE)
            message(f"You Lost! Score: {score}. Press Q-Quit or C-Play Again", RED, WIDTH // 6, HEIGHT // 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_SIZE
                    x_change = 0

        # Snake movement
        x += x_change
        y += y_change

        # Check for boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

        # Update snake body
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(score)  # Display score
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10
            food_y = random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10
            snake_length += 1
            score += 10  # Increase score by 10

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
