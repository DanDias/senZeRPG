# Display functionality, passing adapter to use
class Display:
  # TODO: initialize with x and y scale
  def __init__(self, adapter, xScale=1, yScale=1) -> None:
    self.adapter = adapter
    pass

  def draw(self,data,x=0,y=0,width=8,height=8):
    if (x > 8 or x < 0):
      raise Exception('Value out of range for x coordinate {x}')
    if (y > 8 or y < 0):
      raise Exception('Value out of range for y coordinate {y}')
    imageData = data.get_data()
    clippedData = self.clipToArea(imageData,x,y,width,height)
    self.adapter.draw(clippedData)
    
  def clipToArea(self,data,x,y,width,height) -> list:
    # TODO: clip off any bit of the array that's over the boundary
    return data

  # TODO: Implement scaling (for now assume SenseHAT)
  def clear(self,x=0,y=0,width=8,height=8,color=(0,0,0)):
    # TODO: Targetted area clearing support
    self.adapter.clear()
    pass

class DisplayAdapter:
  def draw(self,data):
    #Interface for drawing
    pass

  def clear(self,x=0,y=0,width=0,height=0,color=(0,0,0)):
    #Interface for clearing the screen
    pass