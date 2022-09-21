#!/usr/bin/env python

from operator import truediv
import time as tm

'''
Requirements
-
Test spec
-
Design
-

'''
running = True

t = 0.0
dt = 0.1

while (running):
  # t_new = t_old + dt
  # t = t + dt
  t += dt
  tm.sleep (0.1)
  print ("Time: ", t)

  
  
  
  
 