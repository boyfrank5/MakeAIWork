class Dog:
  pass

#objecten kunnen dingen onthouden. Je kunt er dingen instoppen. 
myDog = Dog ()
yourDog = Dog ()

#init -> initialize -> startpositie
def init (dog, sound, kind = None, name = 'naamloos'):
  dog.sound = sound 
  dog.kind = kind
  dog.name = name
  print (f'Een {_getSpecies (dog) } is geinstantieerd, {dog.name}')
  
  
