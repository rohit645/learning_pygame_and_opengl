# maintaining scores and progress
import pygame
import time
import random
def make_objects(thing_startx,thing_starty,thing_height,level):
	thingcount=random.randint(1,level)
	a=[]
	thing_starty_backup=thing_starty
	for z in range(thingcount):
		if d_height-thing_starty-thing_height>100:
			new_thingy=50*int(random.randint(100,(d_height-thing_starty-thing_height))/50)
			a.append(new_thingy)
			thing_starty+=new_thingy
		if thing_starty_backup>100:
			new_thingy=50*int((random.randint(100,thing_starty))/50)
			a.append(new_thingy)
			thing_starty=new_thingy
	return a
def level_show(level):
	font =pygame.font.Font(None,25)
	text=font.render("Score "+str(level),True,black)
	gdisplay.blit(text,(0,0))

def score(count):
	font =pygame.font.Font(None,25)
	text=font.render("Score "+str(count),True,black)
	gdisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):
	# pygame.draw.rect(gdisplay,color,[thingx,thingy,thingw,thingh])
	gdisplay.blit(img1,(thingx,thingy))
def car(x,y):
	gdisplay.blit(img,(x,y))
def game_loop():
	x=(d_width*0.1)
	y=(d_height*0.40)
	y_change=0
	car_height=78
	car_width =228
	thing_startx=800
	thing_starty=50*(random.randrange(0,d_height)/50)
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	level=1
	a=make_objects(thing_startx,thing_starty,thing_height,level)
	count=0
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
		gdisplay.blit(bgimg,(0,0))




		for n in range(len(a)):
			things(thing_startx,a[n],thing_width,thing_height,red)
		thing_startx-=thing_speed	
		score(count)
		car(x,y)

		if y>d_height-car_height or y<0:
			crash()
		
		for n in range(len(a)):
			if thing_startx<0:
				thing_startx= d_width - thing_width
				a=make_objects(thing_startx,a[n],thing_height,level)
				count+=1
				if count%10==0:
					level+=1
					thing_speed+=1
				# print a
				break
				# thing_speed+=1
				# thing_height+=10
				# thing_width+=10
			else:
				# print a,n
				if a[n]+thing_height>y and a[n]+thing_height<y+car_height and thing_startx<x+car_width:
					crash()
					break

				if a[n]<y+car_height and a[n]+thing_height>y+car_height and thing_startx<x+car_width:
					crash()
					break

				if a[n]<y and a[n]+thing_height>y+car_height and thing_startx<x+car_width:
					crash()
					break


		pygame.display.update()
		clock.tick(60)


def text_objects(text,font):
	textSurface=font.render(text,True,white)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.Font('freesansbold.ttf',85)
	TextSurf,TextRect=text_objects(text,largeText)
	TextRect.center = ((d_width/2),(d_height*0.2))
	gdisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)

	game_loop()

def crash():
	message_display("you are dead!!")
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
img1=pygame.image.load('img1.png')
bgimg=pygame.image.load('bgimg.png')
game_loop()
pygame.quit()
quit()
