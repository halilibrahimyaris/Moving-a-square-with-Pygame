import pygame
pygame.init()
ekran = pygame.display.set_mode((800, 600))
pygame.display.set_caption("odev")
#--------------------------------------------------
x = 200
y = 200
width = 15
height = 15
vel = 10
#--------------------------------------------------
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # --------------------------------------------------
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_DOWN] and y < 600 - height:
        y += vel
        # --------------------------------------------------
    if tuslar[pygame.K_UP] and y > 0:
        y -= vel
    # --------------------------------------------------
    if tuslar[pygame.K_LEFT] and x > 0:
        x -= vel
    # --------------------------------------------------
    if tuslar[pygame.K_RIGHT] and x < 800 - width:
        x += vel
    # --------------------------------------------------
    ekran.fill((75, 100, 46))
    pygame.draw.rect(ekran, (0, 0, 0), (x, y, width, height))

    pygame.display.update()
pygame.quit()
