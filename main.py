import pygame, time
from player import Player
from enemy import Enemy
from ai_enemy import AI_enemy
from ball import Ball
import random

# Game initialization
pygame.init()

# Config parameters
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
dark_red = (200, 0, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)
dark_blue = (0, 0, 200)

# Title of this game
pygame.display.set_caption("Let's PONG")

# Font initialization
pygame.font.init()


def score_a_point(ball):
    player_score = 0
    enemy_score = 0

    if ball.ballX >= 1200:
        player_score += 1

    elif ball.ballX <= 80:
        enemy_score += 1

    font = pygame.font.SysFont('comicsans', 115)
    player_points = font.render("Score: " + str(player_score), True, white)
    enemy_points = font.render("Score: " + str(enemy_score), True, white)

    screen.blit(player_points, (170, 10))
    screen.blit(enemy_points, (820, 10))


# Button on which is testing any action
def testing_button(color, active_color, x, y, width, height, action=None):
    mouseX, mouseY = pygame.mouse.get_pos()
    a, b, c = pygame.mouse.get_pressed()

    if x + width > mouseX > x and y + height > mouseY > y:
        pygame.draw.rect(screen, active_color, pygame.Rect(x, y, width, height))

        if a == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))


# Nice looking button :P
def button(x, y, file, action=None):
    img = pygame.image.load(file)
    screen.blit(img, (x, y))

    mouseX, mouseY = pygame.mouse.get_pos()
    a, b, c = pygame.mouse.get_pressed()

    if x + img.get_width() > mouseX > x and y + img.get_height() > mouseY > y and a == 1 and action != None:
        action()


# Quitting the game
def quit_game():
    pygame.quit()
    quit()


# Starting screen
def start_screen():
    font = pygame.font.SysFont('comicsans', 115)
    text = font.render("Let's PONG!", True, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))

        button(315, 400, "play.png", Player2Game)
        button(860, 400, "quit.png", quit_game)
        testing_button(dark_blue, bright_blue, 620, 400, 60, 60, Player1Game)

        screen.blit(text, (screenWidth - text.get_width() - 395, screenHeight - text.get_height() - 500))

        pygame.display.update()
        clock.tick(60)


# ================= Player vs Player ===================== #

class Player2Game:
    def __init__(self):
        # Created objects
        player = Player(screen)
        enemy = Enemy(screen)
        ball = Ball(screen, int(screenWidth / 2), int(screenHeight / 2))

        self.a = random.randint(1, 4)
            
        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit_game()

            screen.fill((0, 0, 0))

            # Drawing players and ball
            self.draw(player, enemy, ball)

            # Moving players and ball
            self.move(player, enemy, ball)

            # Collision when ball hits the rect
            self.player_collision(player, ball)
            self.enemy_collision(enemy, ball)

            # Drawing splitting lines
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(screenWidth / 2, 0, 1, screenHeight))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 100, screenWidth, 1))

            # Game-pausing button
            testing_button(dark_blue, bright_blue, 620, 650, 60, 60, Player2Game)

            # Back to start button
            testing_button(dark_red, bright_red, 720, 650, 60, 60, start_screen)

            # Scoring a point
            score_a_point(ball)

            # Adding an new ball
            add_a_new_ball(ball)

            # Updating screen and setting frames per second
            pygame.display.update()
            clock.tick(60)

    # Drawing the created objects
    @staticmethod
    def draw(player, enemy, ball):
        player.drawPlayer()
        enemy.drawEnemy()
        ball.drawBall()

    # Moving the created object
    def move(self, player, enemy, ball):
        player.movePlayer()
        enemy.moveEnemy()
        ball.moveBall(self.a)

    # Players collision
    @staticmethod
    def player_collision(player, ball):
        if ball.ballX <= player.playerX + player.playerWidth and ball.ballX + ball.ballRadius >= player.playerX:
            if ball.ballY >= player.playerY and ball.ballY + ball.ballRadius <= player.playerY + player.playerHeight:
                ball.ballSpeedX *= -1

    # Opponents collision
    @staticmethod
    def enemy_collision(enemy, ball):
        if ball.ballX <= enemy.enemyX + enemy.enemyWidth and ball.ballX + ball.ballRadius >= enemy.enemyX:
            if ball.ballY >= enemy.enemyY and ball.ballY + ball.ballRadius <= enemy.enemyY + enemy.enemyHeight:
                ball.ballSpeedX *= -1


# ================== Player vs Computer ==================== #


class Player1Game:
    def __init__(self):
        # Created objects
        player = Player(screen)
        ai_enemy = AI_enemy(screen)
        ball = Ball(screen, int(screenWidth / 2), int(screenHeight / 2))

        self.a = random.randint(1, 4)
        
        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit_game()

            screen.fill((0, 0, 0))

            # Drawing objects
            self.draw(player, ai_enemy, ball)

            # Moving objects
            self.move(player, ai_enemy, ball)

            # Collision when ball hits the rect
            self.player_collision(player, ball)
            self.ai_enemy_collision(ai_enemy, ball)

            # Drawing splitting lines
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(screenWidth / 2, 0, 1, screenHeight))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 100, screenWidth, 1))

            # Scoring a point
            score_a_point(ball)

            # Game-pausing button
            testing_button(dark_blue, bright_blue, 620, 650, 60, 60, Player1Game)

            # Back to start button
            testing_button(dark_red, bright_red, 720, 650, 60, 60, start_screen)

            # Adding an new ball
            add_a_new_ball(ball)

            # Screen updating and setting frames per second
            pygame.display.update()
            clock.tick(60)

    # Drawing objects
    @staticmethod
    def draw(player, ai_enemy, ball):
        player.drawPlayer()
        ai_enemy.drawAI_enemy()
        ball.drawBall()

    # Moving objects
    def move(self, player, ai_enemy, ball):
        player.movePlayer()
        ai_enemy.moveAI_enemy()
        ball.moveBall(self.a)

    # Players collision
    @staticmethod
    def player_collision(player, ball):
        if ball.ballX <= player.playerX + player.playerWidth and ball.ballX + ball.ballRadius >= player.playerX:
            if ball.ballY >= player.playerY and ball.ballY + ball.ballRadius <= player.playerY + player.playerHeight:
                ball.ballSpeedX *= -1

    # Opponents collision
    @staticmethod
    def ai_enemy_collision(ai_enemy, ball):
        if ball.ballX <= ai_enemy.ai_enemyX + ai_enemy.ai_enemyWidth and ball.ballX + ball.ballRadius >= ai_enemy.ai_enemyX:
            if ball.ballY >= ai_enemy.ai_enemyY and ball.ballY + ball.ballRadius <= ai_enemy.ai_enemyY + ai_enemy.ai_enemyHeight:
                ball.ballSpeedX *= -1


if __name__ == '__main__':
    start_screen()
    pygame.font.quit()
