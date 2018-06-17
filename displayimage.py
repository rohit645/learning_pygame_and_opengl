def car(x,y):
	gdisplay.blit(img,(x,y))

import pygame
pygame.init()

d_width=800
d_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

gdisplay=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Let's Race")
clock = pygame.time.Clock()

img=pygame.image.load('img.png')

x=(d_width*0.45)
y=(d_height*0.8)
crashed=False

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
	gdisplay.fill(white)
	car(x,y)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()