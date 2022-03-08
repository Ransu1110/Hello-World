import pygame

bg = pygame.image.load("sprites/background.png")

icon = pygame.image.load("sprites/Skul.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("JettWreck")
right_dash = pygame.image.load("sprites/jett dash right.png")
left_dash = pygame.image.load("sprites/jett dash left.png")
right = False
left = False
x = 500
y = 500
isDash = False
dash_power = 6
window = pygame.display.set_mode((x, y))


class Player:

    def __init__(self, p_x, p_y):
        self.p_x = p_x
        self.p_y = p_y
        self.player_speed = 10

    def draw(self, win):
        player_sprite = pygame.image.load("sprites/jett.png").convert_alpha()
        win.blit(player_sprite, (self.p_x, self.p_y))


class Enemy:
    def __init__(self, e_x, e_y):
        self.e_x = e_x
        self.e_y = e_y

    def draw(self, win):
        enemy_sprite = pygame.image.load("sprites/enemy.png").convert_alpha()
        win.blit(enemy_sprite, (self.e_x, self.e_y))


def redraws():
    window.blit(bg, (0, 0))
    player.draw(window)
    enemy.draw(window)

    pygame.display.update()


# mainloop
player = Player(250, 400)
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
    if key[pygame.K_s] and player.p_y < y:
        player.p_y += player.player_speed

    if not isDash:
        # A
        if key[pygame.K_a] and player.p_x > -1:
            player.p_x -= player.player_speed
            left = True
            right = False
        # D
        if key[pygame.K_d] and player.p_x < x - 64:
            player.p_x += player.player_speed
            right = True
            left = False
    if left:
        if not isDash:

            # SPACE/Dash
            if key[pygame.K_SPACE]:
                isDash = True
        else:
            if dash_power >= 1:
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
            if dash_power >= 0:
                player.p_x += (dash_power ** 2)
                dash_power -= 1
            else:
                isDash = False
                dash_power = 6
    window.fill((0, 0, 0))
    print(player.p_x)
    print(dash_power)
    redraws()
pygame.quit()
