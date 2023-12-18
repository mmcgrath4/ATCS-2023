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
        self.possibilites = {"Raw:": 0, "Rare": 30, "Medium Rare": 60, "Medium": 90, "Medium Well": 120, " Well": 150, "Burnt": 180}
        self.steak = Steak(self)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.flips = 0
        self.red_change = 0
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.current_time = 0
        self.start_time = 0
        self.flipped_time = 0
        self.reference_time = 1

        
    def play(self):
        running = True
        self.setup()
        goal_state = self.randomize_rarity()
        self.print_starting_message()
        self.draw_goal_steak(goal_state)

        gameStarted = False
        gameOver = False
        first_side_state = ""
        second_side_state = ""
        while running and not gameOver:
            self.dt += self.clock.tick(100)
            side = 1
            # Handle closing the window and Keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.flips += 1
                        # Flip steak
                        self.reference_time = 1
                        self.red_change = 0
                        side = 2
                        first_side_state = self.steak.get_current_state()
                        self.steak.update(False, side)
                        self.flipped_time = pygame.time.get_ticks()
                    elif event.key == pygame.K_s:
                        self.start_time = pygame.time.get_ticks()
                        gameStarted = True
                    elif event.key == pygame.K_d:
                        second_side_state = self.steak.get_current_state()
                        gameOver = True
            
            if self.flips == 0:
                self.current_time = (pygame.time.get_ticks() - self.start_time)/1000
            elif self.flips == 1:
                self.current_time = (pygame.time.get_ticks() - self.flipped_time)/1000

            # Change steak color and change state if needed
            if gameStarted and not gameOver:
                if self.dt > 100:
                    self.dt = 0
                    self.red_change += 3
                    self.change_color()
                self.steak.update(self.isTimerUp(), side)
                
            pygame.display.flip()
        
        print(first_side_state)
        print(second_side_state)
        print(goal_state)
        if first_side_state == goal_state and second_side_state == goal_state:
            self.print_winning_message()
        elif first_side_state != goal_state:
            self.print_losing_message(1)
        elif second_side_state != goal_state:
            self.print_losing_message(2)
        else:
            self.print_losing_message(0)
            
    def print_starting_message(self):
        self.draw_text("Goal Steak:", (630, 230))
        self.draw_text("Click 'S' to start cooking", (400, 420))
        self.draw_text("Click 'F' to flip the steak", (400, 450))
        self.draw_text("Click 'D' to finish cooking the steak", (400, 480))

    # Function to print text on the screen (ChatGPT generated)
    def draw_text(self, text, position):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def print_winning_message(self):
        self.screen.fill((255,255,255))
        self.draw_text("Congratulations! You won the game!", (self.WIDTH // 2, self.HEIGHT // 2))
        pygame.display.flip()
        time.sleep(3)  

    def print_losing_message(self, side):
        self.screen.fill((255,255,255))
        if side == 0:
            self.draw_text("You lost! Neither of the sides were cooked correctly", (self.WIDTH // 2, self.HEIGHT // 2))
        elif side == 1:
            self.draw_text("You lost! The first side was cooked incorrectly", (self.WIDTH // 2, self.HEIGHT // 2))
        else:
            self.draw_text("You lost! The second side was cooked incorrrectly", (self.WIDTH // 2, self.HEIGHT // 2))
        pygame.display.flip()
        time.sleep(3) 

    def change_color(self):
        if self.red_change > 255:
            self.red_change = 255      
        self.steak.draw_steak(self.screen, self.red_change,  True)

    def randomize_rarity(self):
        return random.choice(list(self.possibilites))
    
    def draw_goal_steak(self, goal):
        self.steak.draw_steak(self.screen, self.possibilites[goal], False)
    
    def isTimerUp(self):
        if abs(self.current_time - self.reference_time) < 0.05:
            self.reference_time += 1
            return True
        return False

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