import pygame 
from characters import characters
pygame.init() 


displayWidth = 500
displayHeight = 500
window = pygame.display.set_mode((displayWidth, displayHeight)) #creates display surface
pygame.display.set_caption('Pygame') 

def drawCharacter(character): 
  pygame.draw.rect(window, (255, 0, 0), (character['x'], character['y'], character['width'], character['height']))
  
def preventMovementOffScreen(character): 
  if character['x'] < 0: 
    character['x'] = 0 
  if character['y'] < 0: 
    character['y'] = 0 
  if character['x'] > displayWidth - character['width']: 
    character['x'] = displayWidth - character['width']
  if character['y'] > displayHeight - character['height']: 
    character['y'] = displayHeight - character['height']


running = True 
while running: 
  pygame.time.delay(100) #milliseconds 

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 

  player = characters['player']
  keys = pygame.key.get_pressed() 
  if keys[pygame.K_LEFT]: 
    player['x'] -= player['vel']
  if keys[pygame.K_RIGHT]:
    player['x'] += player['vel']
  if keys[pygame.K_UP]: 
    player['y'] -= player['vel']
  if keys[pygame.K_DOWN]: 
    player['y'] += player['vel']

  window.fill((0,0,0)) #makes screen all black before drawing characters

  for character in characters: 
    preventMovementOffScreen(characters[character])
    drawCharacter(characters[character])

  pygame.display.update() 

pygame.quit()
