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


  keys = pygame.key.get_pressed() 
  if keys[pygame.K_LEFT]: 
    x -= velocity
  if keys[pygame.K_RIGHT]: 
    x += velocity
  if keys[pygame.K_UP]: 
    y -= velocity 
  if keys[pygame.K_DOWN]: 
    y += velocity

  win.fill((0,0,0)) #makes screen all black before drawing the rectangle again
  pygame.draw.rect(win, (255, 0, 0), (x, y, charWidth, charHeight))
  pygame.display.update() 

pygame.quit()
