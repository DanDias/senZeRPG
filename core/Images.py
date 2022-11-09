from PIL import Image
from os import path
from os.path import exists

#  TODO: Probably should define some kind of image path 
#        in config and load it from there. But lets get 
#        this bugger working first.
directory = path.realpath(path.dirname(__file__))

class ImageLoader:
  def __init__(self):
    pass
  
  def load(self, filename):
      # if it exists as passed, cool.
    #  Otherwise lets check where images are supposed to be
    if (exists(filename)):
      fullPath = filename
    else:
      fullPath = f"{directory}/{filename}"
    # Okay, now we're ready to see if it's a bad image path
    if (exists(fullPath)):
      img = Image.open(fullPath)
      # If it's animated, use that.
      if (img.is_animated):
        return AnimatedSprite(img)
      else:
        return Sprite(img)
    else:
      raise Exception(f"Unable to open file: {fullPath}")
  
class DrawableObject:
  def get_data():
    pass

  def update():
    pass

class Sprite:
  def __init__(self, image:Image) -> DrawableObject:
    self.info = image

class AnimatedSprite:
  def __init__(self, image:Image) -> DrawableObject:
    self.info = image
    self.frame = 0
    self.framecount = self.info.n_frames
    
  # TODO: Make it so the animated sprite can have its own
  #       speed. Right now this will go as fast as the draw calls happen
  def get_data(self):
    try:
      if self.frame >= self.framecount:
        self.frame = 0
      self.info.seek(self.frame)
      rgbImage = self.info.convert('RGB')
      frameData = list(rgbImage.getdata())
      # Change frames
      self.frame = self.info.tell()+1
      return frameData
    except:
      print(f"Unable to display frame #{self.frame}")
      pass
  
  # TODO: This is likely where we'll get to define speed
  def update(self):
    pass