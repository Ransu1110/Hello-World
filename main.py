import pygame

bg = pygame.image.load("sprites/background.png")

icon = pygame.image.load("sprites/Skul.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("JettWreck")
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
        bullet_sprite = pygame.image.load("sprites/orangeball.png")
        win.blit(bullet_sprite, (self.b_x, self.b_y))


class Enemy:
    def __init__(self, e_x, e_y):
        self.e_x = e_x
        self.e_y = e_y

    def draw(self, win):
        enemy_sprite = pygame.image.load("sprites/enemy.png").convert_alpha()
        win.blit(enemy_sprite, (self.e_x, self.e_y))


def redraws():
    global shooting
    window.blit(bg, (0, 0))
    player.draw(window)
    # bullet
    if shooting:
        bullet.draw(window)
        bullet.b_y -= bullet.speed

        if bullet.b_y < -1:
            shooting = False
    #    enemy.draw(window)

    pygame.display.update()


# mainloop
player = Player(250, 400)
bullet = Bullet(0, 0, 15)
enemy = Enemy(0, 60)

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    # W
    if key[pygame.K_w] and player.p_y > -1:
        player.p_y -= player.player_speed

    # S
    if key[pygame.K_s] and player.p_y < y - 64:
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
        if key[pygame.K_d] and player.p_x <= x - 64:
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
            if dash_power >= 0 and player.p_x < x - 64:
                player.p_x += (dash_power ** 2)
                dash_power -= 1
            else:
                isDash = False
                dash_power = 6
    window.fill((0, 0, 0))
    print(shooting)
    redraws()
pygame.quit()
