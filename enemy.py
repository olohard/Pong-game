import pygame


class Enemy(object):
    def __init__(self, screen):
        self.screen = screen
        self.enemyX = 1180
        self.enemyY = 310
        self.enemyWidth = 10
        self.enemyHeight = 150
    
    # Drawing the opponent
    def drawEnemy(self):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.enemyX, self.enemyY, self.enemyWidth, self.enemyHeight))
    
    # Moving the opponent
    def moveEnemy(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.enemyY > 100:
            self.enemyY -= 10
        elif key[pygame.K_DOWN] and self.enemyY < 580:
            self.enemyY +=10