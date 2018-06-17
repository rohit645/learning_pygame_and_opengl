import pygame
import time
def car(x,y):
	gdisplay.blit(img,(x,y))
def game_loop():
	x=(d_width*0.1)
	y=(d_height*0.40)
	y_change=0
	car_height=78
	crashed=False

	while not crashed:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
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
		if y>d_height-car_height or y<0:
			crash()
		pygame.display.update()
		clock.tick(60)
def text_objects(text,font):
	textSurface=font.render(text,True,black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect=text_objects(text,largeText)
	TextRect.center = ((d_width/2),(d_height/2))
	gdisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)

	game_loop()

def crash():
	message_display("you crashed!!")
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
game_loop()
pygame.quit()
quit()