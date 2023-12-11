import pygame
import sys
import time
import random
from steak import Steak

# Initialize Pygame
pygame.init()

class Game:
    def __init__(self):
         # Load images
        self.background_image = pygame.image.load("background.png")  
        self.pan_image = pygame.image.load("pan.png")  
        # self.possibilites = {"Raw:": 10, "Rare": 15, "Medium Rare": 20, "Medium": 25, "Medium Well": 30, " Well": 35, "Burnt": 40}
        self.steak = Steak()

        self.clock = pygame.time.Clock()
        self.dt = 0
        
    def play(self):
        # gameover = False
        # while not gameover:
        self.draw()

    def randomize_rarity(self):
        return random.choice(self.possibilites)

    def draw(self):       
        # Set up display
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Virtual Environment")

        # Colors
        white = (255, 255, 255)

        # Load images
        background_image = pygame.image.load("background.png")  # Change "background.png" to your background image file
        pan_image = pygame.image.load("pan.png")  # Change "pan.png" to your pan image file
        steak_image = pygame.image.load("steak.png")  # Load the steak image

        # Resize images
        background_image = pygame.transform.scale(background_image, (width, height))
        pan_image = pygame.transform.scale(pan_image, (300, 120))  # Adjust size as needed
        # Game loop
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw background
            screen.blit(background_image, (0, 0))

            # Draw pan images in the middle, with shifts
            pan_left_position = (width // 4 - 123, height // 2 - 50)
            pan_right_position = (3 * width // 4 - 73, height // 2 - 50)
            
            screen.blit(pan_image, pan_left_position)
            screen.blit(pan_image, pan_right_position)

            # Draw steak image in the middle of each pan
            # steak_left_position = (pan_left_position[0] + 60, pan_left_position[1] + 10)
            # steak_right_position = (pan_right_position[0] + 60, pan_right_position[1] + 10)

            pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 100))


            pygame.display.flip()



# Create a Game object and run the game
if __name__ == "__main__":
    game = Game()  # Create the Game object
    game.play()  # Start the game loop

pygame.quit()
sys.exit()