import time as tm 

class Car:
  
  def __init__(self, name, force, mass):
    self.name = name
    self.force = force
    self.mass = mass
    self.x = 0.0
    self.v = 0.0
    
  def move(self, dt):
    a = self.force / self.mass
    dv = a * dt 
    self.v = self.v + dv 
          
    print("snelheid:", self.name, self.v)
        
    dx = self.v * dt 
    self.x = self.x + dx 
          
    print("afstand: ", self.name, self.x)
