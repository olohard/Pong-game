import pygame


class Ball(object):
    def __init__(self, screen, ballX, ballY):
        self.screen = screen
        self.ballX = ballX
        self.ballY = ballY
        self.ballRadius = 10
        self.ballSpeedX = 10
        self.ballSpeedY = 10
    
    # Drawing the ball
    def drawBall(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.ballX), int(self.ballY)), self.ballRadius)

    # Moving the ball
    def moveBall(self, a):
        if a == 1:
            self.ballX -= self.ballSpeedX
            self.ballY -= self.ballSpeedY
        if a == 2:
            self.ballX -= self.ballSpeedX
            self.ballY += self.ballSpeedY
        if a == 3:
            self.ballX += self.ballSpeedX
            self.ballY -= self.ballSpeedY
        if a == 4:
            self.ballX += self.ballSpeedX
            self.ballY += self.ballSpeedY
        
        if self.ballY >= 720:
            self.ballSpeedY *= -1
        
        if self.ballY <= 110:
            self.ballSpeedY *= -1

#        if self.ballX >= 1260:
#            self.ballSpeedX *= -1
#
#        if self.ballX <= 0:
#            self.ballSpeedX *= -1


