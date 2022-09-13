#!/usr/bin/env python

class Dog:
    pass
  
myDog = Dog ()
yourDog = Dog ()

def init (dog, sound, kind = None, name = 'naamloos'):
    dog.sound = sound
    dog.kind = kind
    dog.name = name
    print (f'Een{_getSpecies (dog)} is geinstantieerd, {dog.name}' )

def eat (dog, food = 'Wat de pot schaft'):
    _introduce (dog)
    print (f'en ik eet {food}' )
    
def move (dog):
    _introduce (dog)
    print (f'en ik loop' )
    
def reproduce (dog, aantal = 3):
    _introduce (dog)
    print (f'en ik krijg gemiddeld {aantal} jongen' )
    
def wagTail (dog):
    _introduce (dog)
    print ('en ik kwispel' )
    
def _introduce (dog):
    print (
      f'Hallo, ik ben {dog.name}, mijn soort is {_getSpecies (dog)}',
      end =''      
    )
    
def _getSpecies (dog):
    return dog.kind 
  
init (myDog, 'Wraff', 'Ritriever ', 'Bello')
init (yourDog, 'Kef', 'Poodle ', 'Nouchka')

eat (myDog, 'blikvoer')
wagTail (myDog)
eat (yourDog, 'droogvoer')
reproduce (myDog, 4)
move (yourDog)
reproduce (yourDog, 5) 
move (myDog)
wagTail (yourDog)
 


    