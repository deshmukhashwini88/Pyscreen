import pygame
import sys

pygame.init()

# Get input from user (console)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

product = num1 * num2

# Create window
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Product")

font = pygame.font.Font(None, 40)

# Create text
text = font.render(f"Product = {product}", True, (0, 0, 0))

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(text, (80, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()