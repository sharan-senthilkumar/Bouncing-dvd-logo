import pygame
import sys
import random

pygame.init()

x = random.randint(0,400)
y = random.randint(0,300)

width = 800
height = 600

x_speed = 0.25
y_speed = 0.25

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bouncing DVD")
color = (255, 255, 255)

img_x = 150
img_y = 130

image = pygame.image.load("th (1).jpg")
image = pygame.transform.scale(image, (img_x,img_y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    window.fill((0,0,0))

    x = x + x_speed
    y = y + y_speed

    if x + img_x > width or x<0:
        x_speed = x_speed * (-1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if y+ img_y > height or y<0:
        y_speed = y_speed * (-1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    
    tinted_image = image.copy()  
    tinted_image.fill(color, special_flags=pygame.BLEND_MULT) 
    window.blit(tinted_image, (x, y))

    pygame.display.update()




