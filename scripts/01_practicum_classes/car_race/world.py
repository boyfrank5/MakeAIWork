import time as tm
from car import Car

class World:
  
  # Constructor:
  def __init__(self):
  
    self.t = 0.0
    self.dt = 0.1
    self.running = True
    self.tesla = Car("Tesla", 800.0, 600.0)
    self.bmw = Car("BMW", 1500.0, 1000.0)

  def bang(self):
    while self.running:
      self.t += self.dt
      self.tesla.move(self.dt)
      self.bmw.move(self.dt)
      if self.tesla.x > 100:
        self.running = False
        print ('CONGRATULATIONS ELON')
      if self.bmw.x > 100:
        self.running = False 
        print('CONGRATULATIONS A.MERKEL')
    
      print("Time: ", self.t)
      tm.sleep(self.dt)

  def stop(self):
    self.running = False 
