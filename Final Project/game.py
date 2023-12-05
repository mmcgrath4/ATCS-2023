import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Environment")

# Colors
white = (255, 255, 255)

# Load images
background_image = pygame.image.load("background.png")  # Change "background.jpg" to your background image file
pan_image = pygame.image.load("pan.jpg")  # Change "pan.png" to your pan image file

# Resize images
background_image = pygame.transform.scale(background_image, (width, height))
pan_image = pygame.transform.scale(pan_image, (100, 100))  # Adjust size as needed

# Set up fonts
font = pygame.font.Font(None, 36)

# Stopwatch variables
start_time = None

def start_stopwatch():
    global start_time
    start_time = time.time()

def get_elapsed_time():
    if start_time is not None:
        return time.time() - start_time
    else:
        return 0

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw pan images in the middle
    screen.blit(pan_image, (width // 4 - 50, height // 2 - 50))
    screen.blit(pan_image, (3 * width // 4 - 50, height // 2 - 50))

    # Draw stopwatch at the bottom
    elapsed_time = get_elapsed_time()
    stopwatch_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, white)
    screen.blit(stopwatch_text, (10, height - 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
