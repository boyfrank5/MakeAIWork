import math
# math.exp()

# define symbols

symbolVecs = {'0': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items())


class Node:
  def __init__(self):
  self.value = None
  self.inLinks = []
  

class Link:
  def __init__(self,inputNode, outputNode):
  self.inputNodes = 1
  self.inputNodes = 1
  self.outputNodes = 1
  
  
# define

trainingsSet = (
  ((
    (1, 1, 1),
    (1, 0, 1),
    (1, 1, 1)
), '0'),
  (( 
    (0, 1, 0),
    (1, 0, 1),
    (0, 1, 0)
), '0'),
  (( 
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 0)
), 'X'),
    (( 
    (1, 0, 1),
    (0, 1, 0),
    (1, 0, 1)
), 'X'),
)                                                 


