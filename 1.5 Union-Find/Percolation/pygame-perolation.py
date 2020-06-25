import pygame
from assignment_percolation import Percolation


TILES = 8
TILE_WIDTH = 100 if TILES < 6 else 50
WIDTH = min(TILES * TILE_WIDTH, 600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

model = Percolation(TILES)

pygame.init()
display = pygame.display.set_mode((WIDTH, WIDTH))
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  display.fill(WHITE)

  for i, row in enumerate(model.nodes):
    for j, col in enumerate(row):
      if model.isOpen(i, j):
        pygame.draw.rect(display, BLACK, 
        (i*TILE_WIDTH, j*TILE_WIDTH, TILE_WIDTH, TILE_WIDTH), 1)
      else:
        pygame.draw.rect(display, BLACK, 
        (i*TILE_WIDTH, j*TILE_WIDTH, TILE_WIDTH, TILE_WIDTH))

  try:
    next(model())
  except StopIteration:
    pass

  pygame.display.update()
  clock.tick(2)