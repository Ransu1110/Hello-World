import random

import pygame

pygame.init()

bg = pygame.image.load("sprites/background.png")

icon = pygame.image.load("sprites/Skul.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("JettWreck")
red = (255, 0, 0)
white = (255, 255, 255)
sprite_size = 64
# indicator for which side to dash
right = False
left = False
# for dash
isDash = False
dash_power = 6
# for screen size/ window size/ surface size
x = 500
y = 500
# surface/display/window
window = pygame.display.set_mode((x, y))
# indicator if the user want to shoot
shooting = False
# hit
hit = False
# when play sprite hits enemy sprite
crash = False
# score display
score = 0
scored = False
font = pygame.font.Font("Pixeboy-z8XGD.ttf", 30)
# if the game is over
game_over = False


class Player:

    def __init__(self, p_x, p_y):
        self.p_x = p_x
        self.p_y = p_y
        self.player_speed = 10

    def draw(self, win):
        player_sprite = pygame.image.load("sprites/jett.png").convert_alpha()
        win.blit(player_sprite, (self.p_x, self.p_y))


class Bullet:
    def __init__(self, b_x, b_y, speed):
        self.b_x = b_x
        self.b_y = b_y
        self.speed = speed

    def draw(self, win):
        bullet_sprite = pygame.image.load("sprites/bullet.png")
        win.blit(bullet_sprite, (self.b_x, self.b_y))


class Enemy:
    def __init__(self, e_x, e_y, speed):
        self.e_x = e_x
        self.e_y = e_y
        self.speed = speed

    def draw(self, win):
        enemy_sprite = pygame.image.load("sprites/Enemy.png").convert_alpha()
        win.blit(enemy_sprite, (self.e_x, self.e_y))


def redraws():
    global shooting, hit, crash

    window.blit(bg, (0, 0))
    player.draw(window)
    # remove the "#" to show hitbox
    # pygame.draw.rect(window, red, player_hitbox, 1)
    # pygame.draw.rect(window, red, enemy_hitbox, 1)
    # pygame.draw.rect(window, red, bullet_hitbox, 1)
    # bullet
    if shooting:
        bullet.draw(window)
        bullet.b_y -= bullet.speed
        if bullet.b_y < -1:
            shooting = False
    enemy.draw(window)
    # collision
    if bullet_hitbox.colliderect(enemy_hitbox):
        hit = True
        shooting = False
    if player_hitbox.colliderect(enemy_hitbox):
        crash = True

    # score system
    score_display = font.render("Score:" + str(score), False, white)
    window.blit(score_display, (0, 0))

    pygame.display.update()


# mainloop
player = Player(250, 400)
bullet = Bullet(player.p_x, player.p_y, 20)
enemy = Enemy(0, 60, 3)

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # hitboxes
    player_hitbox = pygame.Rect(player.p_x + 8, player.p_y + 8, sprite_size - 16, sprite_size - 16)
    enemy_hitbox = pygame.Rect(enemy.e_x + 8, enemy.e_y + 8, sprite_size - 16, sprite_size - 16)
    bullet_hitbox = pygame.Rect(bullet.b_x + 4, bullet.b_y + 4, sprite_size / 2.5, sprite_size / 2.5)
    key = pygame.key.get_pressed()

    # enemy movement
    enemy.e_x += enemy.speed
    if enemy.e_x >= x - sprite_size or enemy.e_x <= -1:
        enemy.speed *= -1

    # if enemy and play hits each other
    if crash:
        score -= 1
        enemy.e_y = random.randint(0, 372)
        crash = False
    # enemy random spawn locations adn score
    if hit:
        enemy.e_y = random.randint(0, 372)
        hit = False
        bullet_hitbox.y = player.p_y
        score += 1
        scored = True
        if score == 5:
            enemy.speed *= 2
            if score == 10:
                enemy.speed *= 2
                if score == 20:
                    enemy.speed *= 2

    # W
    if key[pygame.K_w] and player.p_y > -1:
        player.p_y -= player.player_speed

    # S
    if key[pygame.K_s] and player.p_y < y - sprite_size:
        player.p_y += player.player_speed

    # E To shoot bullet/s
    if not shooting:
        if key[pygame.K_e]:
            shooting = True
            bullet.b_x = player.p_x + 16
            bullet.b_y = player.p_y
        else:
            shooting = False

    if not isDash:
        # A
        if key[pygame.K_a] and player.p_x > -1:
            player.p_x -= player.player_speed
            left = True
            right = False
        # D
        if key[pygame.K_d] and player.p_x <= x - sprite_size:
            player.p_x += player.player_speed
            right = True
            left = False

    if left:
        if not isDash:

            # SPACE/Dash
            if key[pygame.K_SPACE]:
                isDash = True
        else:
            if dash_power >= 1 and player.p_x > -1:
                player.p_x -= (dash_power ** 2)
                dash_power -= 1
            else:
                isDash = False
                dash_power = 6
    if right:
        if not isDash:

            # SPACE/Dash
            if key[pygame.K_SPACE]:
                isDash = True
        else:
            if dash_power >= 0 and player.p_x < x - sprite_size:
                player.p_x += (dash_power ** 2)
                dash_power -= 1
            else:
                isDash = False
                dash_power = 6

    # for game over display
    window.fill((0, 0, 0))
    redraws()
pygame.quit()

# game over loop
