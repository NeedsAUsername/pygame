player = {
  'x': 50, 
  'y': 50,
  'width': 40,
  'height': 60, 
  'vel': 20 
}

enemy = {
  'x': 200, 
  'y': 200,
  'width': 40,
  'height': 60, 
  'vel': 20 
}

characters = {
  'player': player, 
  'enemy': enemy
}

for char in characters:  
    print(characters[char])