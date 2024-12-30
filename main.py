import pygame
import constants

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        # Add this event handling block
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        # Modified fill call
        screen.fill((0, 0, 0))  # Black color
        pygame.display.flip()

if __name__ == "__main__":
    main()