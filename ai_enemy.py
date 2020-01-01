import pygame
from ball import Ball


class AI_enemy(object):
    def __init__(self, screen):
        self.screen = screen
        self.ai_enemyX = 1180
        self.ai_enemyY = 310
        self.ai_enemyWidth = 10
        self.ai_enemyHeight = 150
        self.ai_enemySpeed = 10
        self.ball = Ball(screen, 640, 360)
    
    # Drawing the AI opponent
    def drawAI_enemy(self):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.ai_enemyX, self.ai_enemyY, self.ai_enemyWidth, self.ai_enemyHeight))
        
    # Moving the AI opponent
    def moveAI_enemy(self):
        self.ai_enemyY += self.ai_enemySpeed
        if self.ai_enemyY >= 580:
            self.ai_enemySpeed *= -1
        if self.ai_enemyY <= 100:
            self.ai_enemySpeed *= -1

