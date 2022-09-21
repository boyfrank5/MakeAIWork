#!/usr/bin/env python
import time as tm

'''
# requirements
Programmeer een simulatielus waarin. 

- een auto met een massa van 600kg 
- een netto voortsctuweingskracth F=800N* optrekt
- een over een afstand van 100 meter

Print de eindtijd via een console
 
# test spec
# design

'''
# requirements
# test spec
# design

running = True

t = 0.0
dt = 0.1

m = 600.0
F = 800
v = 0.0
x = 0.0


while (running):
  # t_new = t_old + dt
    # t = t + dt
  
  t += dt
  print ("Time: ", t)
  
  a = F / m 
  dv = a * dt 
  v = v + dv 
  print("v:", v)
  
  dx = v * dt 
  x = x + dx 
  print("x:", x)

  tm.sleep (0.1)
  if x > 100:
    running = False

    
  

  
  
  
  
  
  
  