import pygame 
pygame.init() 


displayWidth = 500
displayHeight = 500
win = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Pygame') 

player = {
  'x': 50, 
  'y': 50,
  'width': 40,
  'height': 60, 
  'vel': 20 
}

running = True 

def preventMovementOffScreen(character): 
  if character['x'] < 0: 
    character['x'] = 0 
  if character['y'] < 0: 
    character['y'] = 0 
  if character['x'] > displayWidth - character['width']: 
    character['x'] = displayWidth - character['width']
  if character['y'] > displayHeight - character['height']: 
    character['y'] = displayHeight - character['height']

def drawCharacter(character): 
  pygame.draw.rect(win, (255, 0, 0), (character['x'], character['y'], character['width'], character['height']))

while running: 
  pygame.time.delay(100) #milliseconds 

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

  keys = pygame.key.get_pressed() 
  if keys[pygame.K_LEFT]: 
    player['x'] -= player['vel']
  if keys[pygame.K_RIGHT]:
    player['x'] += player['vel']
  if keys[pygame.K_UP]: 
    player['y'] -= player['vel']
  if keys[pygame.K_DOWN]: 
    player['y'] += player['vel']

  preventMovementOffScreen(player)

  win.fill((0,0,0)) #makes screen all black before drawing the rectangle again
  drawCharacter(player)
  pygame.display.update() 

pygame.quit()
