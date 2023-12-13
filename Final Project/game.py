import pygame
import sys
import time
import random
from steak import Steak

# Initialize Pygame
pygame.init()

class Game:
    #CONSTANTS
    WIDTH, HEIGHT = 800, 600

    def __init__(self):
         # Load images
        self.background_image = pygame.image.load("background.png")  
        self.pan_image = pygame.image.load("pan.png")  
        self.possibilites = {"Raw:": 1.5, "Rare": 2, "Medium Rare": 3, "Medium": 4, "Medium Well": 5, " Well": 6, "Burnt": 7}
        self.steak = Steak(self)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.clock = pygame.time.Clock()
        self.dt = 0
        
    def play(self):
        running = True
        self.setup()

        red_change = 0
        green_change = 0
        while running:
            self.dt += self.clock.tick(120)

            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.dt > 120:
                self.dt = 0
                self.steak.update()
                red_change + 1

                if red_change > 105:
                    red_change = 105

                if red_change > 25:
                    green_change = red_change - 25
                self.steak.draw_steak(self.screen, red_change, green_change, True)
            pygame.display.flip()


    def randomize_rarity(self):
        return random.choice(self.possibilites)
    
    def isTimerUp(self):
        return True

    def setup(self):       
        pygame.display.set_caption("Virtual Environment")

        # Load images
        background_image = pygame.image.load("background.png")  
        pan_image = pygame.image.load("pan.png") 

        # Resize images
        background_image = pygame.transform.scale(background_image, (self.WIDTH, self.HEIGHT))
        pan_image = pygame.transform.scale(pan_image, (300, 120)) 

        # Draw background
        self.screen.blit(background_image, (0, 0))

        # Draw pan images in the middle, with shifts
        pan_left_position = (self.WIDTH // 4 - 123, self.HEIGHT // 2 - 50)
        pan_right_position = (3 * self.WIDTH // 4 - 73, self.HEIGHT // 2 - 50)
        
        self.screen.blit(pan_image, pan_left_position)
        self.screen.blit(pan_image, pan_right_position)



# Create a Game object and run the game
if __name__ == "__main__":
    game = Game()  # Create the Game object
    game.play()  # Start the game loop

pygame.quit()
sys.exit()