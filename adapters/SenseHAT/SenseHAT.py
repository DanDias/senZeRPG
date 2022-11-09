#from sense_hat import SenseHat
from sense_emu import SenseHat
from adapters.Display import DisplayAdapter

sense = SenseHat()

class SenseHatAdapter(DisplayAdapter):
  def __init__(self):
    # TODO: Figure out how to do rotation that's scalable for other displays
    #       I'm thinking Enum with portrait, landscape, and flippedPortrait and flippedLandscape
    #sense.set_rotation(180)
    pass
  
  def draw(self,frameData):
    sense.set_pixels(frameData)


  def clear(self):
    # TODO: Targetted area clearing support
    sense.clear()

  # TODO: Support Farenheit because we're dumb
  def get_temp(self):
    return sense.get_temperature()
