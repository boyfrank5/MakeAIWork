# define symbols

symbolVecs = {'0': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items())


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