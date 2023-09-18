import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)
DICE_SIZE = 200

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Dice Roller")

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        rolled_number = roll_dice()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the dice if rolled_number is defined
    if 'rolled_number' in locals():
        dice_image = pygame.image.load(f'dice{rolled_number}.png')
        dice_image = pygame.transform.scale(dice_image, (DICE_SIZE, DICE_SIZE))
        screen.blit(dice_image, (WIDTH // 2 - DICE_SIZE // 2, HEIGHT // 2 - DICE_SIZE // 2))

    # Update the display
    pygame.display.flip()

pygame.quit()
