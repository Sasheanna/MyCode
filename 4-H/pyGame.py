
# imports
import pygame
import random
import sys

import time


# these tell the program to access these SPECIFIC PARTS of pygame.locals
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)


############################

start = time.time()

###########################


# various variables

pygame.init()

#################################################REMOVE BEFORE MEETING
pygame.display.set_caption("Simple Game")
#################################################REMOVE BEFORE MEETING



# size of the screen variables
width = 800# originally 800 and 600
height = 600

grad_color = 0

#color variables, probably of the form "variable" = (red, blue, green)
red = (255,0,0) # (255,0,0)
black = (0,0,0)
blue = (0,250,grad_color)  # ENEMY color, originally (0,255,0).  If you set this to (0, 255, 255) and background_color to (0,250,250) the enemy becomes much harder to see :)
background_color = (0,255,255)  # Makes a variable called background_color

speed = 10

# ALL CAPS vairables are constants (in general)
#  Question:  why are these variables?  The point of a variable is so that the value can be changed, but why do you want that? Unless you want to standardize sizes...
player_size = 50
xpos = width/2  # I'm guessing 'xpos' is an abbreviated form of the words 'x position', making it more suitable for a variable
ypos = height - 2*player_size
player_pos = [xpos,ypos]  # is this an array?

enemy_size = 50
enemy_pos = [random.randint(0,width-enemy_size),0]

screen = pygame.display.set_mode((width,height))  # makes the variable "screen"?  I think this sets the screen width and height

game_over = False

clock = pygame.time.Clock()

# a user-defined method that detects collision and returns the values of either "true" or false"
def detect_collision(player_pos,enemy_pos):  # note the parameters this function will need

        # What are these?  Do they aide in planning?  Are they perhaps a sketch of the player and enemy?
        
	# e1____e2
	# |      |
	# |      |
	# e3____e4
	#
	#    p1____p2
	#    |      |
	#    |      |
	#    p3____p4

        # A lot of variables, I'm not certain what they do or stand for.

	p1x = player_pos[0]
	p1y = player_pos[1]
	p2x = p1x + player_size
	p2y = p1y  # I'm pretty sure that "py" and "px" stand for "player y" and "player x", which would be the character's position, and the number after "p" would
	p3x = p1x  # distinguish each of the values from one another
	p3y = p1y + player_size
	p4x = p2x
	p4y = p3y

	e1x = enemy_pos[0]
	e1y = enemy_pos[1]
	e2x = e1x + enemy_size
	e2y = e1y  # Does "e" stand for enemy?
	e3x = e1x
	e3y = e1y + enemy_size
	e4x = e2x
	e4y = e3y

        # use of pretty much all the above variables.  Does this check to see if the player and enemy are touching?
	if (p1x >= e1x and p1x <= e2x and p1y >= e1y and p1y <= e3y) or \
	   (p2x >= e1x and p2x <= e2x and p2y >= e1y and p2y <= e3y) or \
	   (p3x >= e1x and p3x <= e2x and p3y >= e1y and p3y <= e3y) or \
	   (p4x >= e1x and p4x <= e2x and p4y >= e1y and p4y <= e3y):
	   return True
	return False

# while it's not game over, that means the game is still running, so this is most of telling the computer how the game is run
while not game_over:

        # a for-loop within a while loop
	for event in pygame.event.get():
		#print(event)

		if event.type == QUIT:
			screen.fill(black)
			pygame.display.update()
			
			pygame.quit()
			quit()# I can only guess at what the keyword "quit" means, but sys.exit turns off the program

		if event.type == KEYDOWN:  # if a key is pressed.  Why isn't elif used here, instead of if?
			if event.key == K_ESCAPE:  # if the key pressed is the escape key, it turns off the program
				game_over = True  # the only reason this while loop is running is because is because game_over is equal to true.  This command
                                                  # would end the game, wouldn't it?

			x = player_pos[0]
			y = player_pos[1]  # these are under the K_ESCAPE if statement because they're only needed for the below if statements

			if event.key == K_LEFT:
				x -= player_size  # what relation does player size have to the x position?
			elif event.key == K_RIGHT:
				x += player_size  # I thought an else statement is required for every if statement.  I understand the reason you wouldn't use one
                                                  # here, but I don't know how you're able to avoid errors.

			player_pos = [x,y]
	screen.fill(background_color)  # sets the screen to the value/color background_color

	if enemy_pos[1] >= 0 and enemy_pos[1] < height:
		enemy_pos[1] += speed
	else:
		enemy_pos[0] = random.randint(0,width-enemy_size)
		enemy_pos[1] = 0

	if detect_collision(player_pos,enemy_pos):  # the collision functin is called.
		print("COLLISION")
		game_over = True

	speed = speed + 0.05  # a variable I added that slowly (but not very slowly) increases the enemy speed.

	if grad_color < 250:

		grad_color = grad_color + .5

	blue = (0,250,grad_color)


        # after all that setup, these two commands draw the enemy and player
	pygame.draw.rect(screen,blue,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
	pygame.draw.rect(screen,red,(player_pos[0],player_pos[1],player_size,player_size))

	clock.tick(20)
	pygame.display.update()  # updates the display with everything that just ran through this program


"""--------------------------------------------------------------------
"""

end = time.time()

score = end - start

print("Your Score: ")
print(round(score))

"""
"""#-------------------------------------------------------------------



screen.fill(black)
pygame.display.update()




"""#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


Experiment.  Disable before 4-H meeting!!!!


"""#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

# define colors
white = (255, 255, 255)

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((width, height)) 
  
# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 32) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font.render('GAME OVER', True, white, black) 
  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. X = the width of the screen, half of that would be the middle.  Same with Y.
textRect.center = (width // 2, height // 2) 
  
# infinite loop 
while True : 
  
	# copying the text surface object 
	# to the display surface object  
	# at the center coordinate. 
	display_surface.blit(text, textRect)


	# iterate over the list of Event objects 
	# that was returned by pygame.event.get() method. 
	for event in pygame.event.get() : 
  
		# if event object type is QUIT 
		# then quitting the pygame 
		# and program both. 
		if event.type == pygame.QUIT : 
  
			# "deactivates the pygame library" (allows it to shut off)
			pygame.quit() 
			# quit the program. 
			quit() 

		# updates the screen   
		pygame.display.update()
