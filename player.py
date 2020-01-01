import pygame

class Player(object):
    def __init__(self, screen):
        self.screen = screen
        self.playerX = 100
        self.playerY = 310
        self.playerWidth = 10
        self.playerHeight = 150
    
    # Drawing the player
    def drawPlayer(self):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.playerX, self.playerY, self.playerWidth, self.playerHeight))
        
    # Moving the player
    def movePlayer(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.playerY > 100:
            self.playerY -= 10
        elif key[pygame.K_s] and self.playerY < 580:
            self.playerY += 10