#!/usr/bin/env python3

import random

random.seed

start = 1 
stop = 11

factor1 = random.randrange (start, stop)
factor2 = random.randrange (start, stop)

while True:
  answer = int (input (f'Hoeveel is {factor1} x {factor2}? '))
  if answer == factor1 * factor2:
    break
  print (f'Helaas, {factor1} x {factor1} is geen {answer} ')
  
print ('Programma afgelopen')
  
 