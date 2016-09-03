import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode([800,600])

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
