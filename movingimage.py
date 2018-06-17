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

x=(d_width*0.1)
y=(d_height*0.40)
y_change=0
crashed=False

while not crashed:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed=True
		if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_change+=-5
			elif event.key == pygame.K_DOWN:
				y_change+=5
		if event.type==pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_change=0
	y+=y_change
	gdisplay.fill(white)
	car(x,y)
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()