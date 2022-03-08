import pygame

pygame.init()

x = 700
y = 500
r_x = 350
r_y = 250
JumpCount = 10
isJump = False

win = pygame.display.set_mode((x, y))

# main
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (r_x, r_y, 40, 60))

    keys = pygame.key.get_pressed()

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            neg = 1
            if JumpCount < 0:
                neg = -1
            r_x -= (JumpCount ** 2) / 2 * neg
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10

    print(r_y)
    print(JumpCount)
    pygame.display.update()

pygame.quit()
