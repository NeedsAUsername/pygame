import pygame 
pygame.init() 


displayWidth = 500
displayHeight = 500
win = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('First Game') 

x = 50 
y = 50
charWidth = 40
charHeight = 60 
velocity = 5 

running = True 

while running: 
  pygame.time.delay(100) #milliseconds 

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

pygame.quit()
