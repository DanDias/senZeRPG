from adapters.SenseHAT.SenseHAT import SenseHatAdapter
from adapters.Display import Display
from core.Images import ImageLoader
import random
import time

senseAdapter = SenseHatAdapter()
display = Display(senseAdapter)

w = (255,255,255)
b = (0,0,0)

colors = (w,b)

snow = ImageLoader().load("Snow.gif")

while True:
  if (senseAdapter.get_temp() <= 30):
    display.draw(snow)
  else:
    display.clear()
  time.sleep(0.3)