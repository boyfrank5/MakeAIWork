#!/usr/bin/env python
import random


# requirements: 
# test spec: 
# design:

startTableNr = 5
nrOfTables = 6

startLineNr = 5
nrOfLines = 4

for tableNr in range (startTableNr, startTableNr + nrOfTables):
  for lineNr in range (startLineNr, startLineNr + nrOfLines):
    while True:
      answer = int (input (f'Hoeveel is {lineNr} x {tableNr}?'))
      if answer == lineNr * tableNr:
        break
      print('Try again!') 
    
  #  print (f'{lineNr} x {tableNr} = {lineNr * tableNr}')1
  
  print()
  
   