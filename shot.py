from circleshape import CircleShape
import constants
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0 or self.position.x > constants.SCREEN_WIDTH or self.position.y < 0 or self.position.y > constants.SCREEN_HEIGHT:
            self.kill()