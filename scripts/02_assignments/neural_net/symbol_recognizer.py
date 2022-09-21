#!/usr/bin/python3

import math

'''
Requirements:
-
Testspecs:
-
Design:
-
'''

# define symbols

symbolVecs = {'0': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items())


# class Node:
#   def __init__(self):
#   self.value = None
#   self.inLinks = []
  

# class Link:
#   def __init__(self,inputNode, outputNode):
#   self.inputNodes = 1
#   self.inputNodes = 1
#   self.outputNodes = 1
  

# define

trainingsSet = (
  ((
    (1, 0, 1),
    (1, 0, 1),
    (1, 1, 1)
), 'O'),
  (( 
    (0, 1, 0),
    (1, 0, 1),
    (0, 1, 0)
), 'O'),
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

set1 = trainingsSet[0][0]
set_1=[]

for i in set1:
  for mainlist in i:
    set_1.append(mainlist)
    print(i)

weightX = [1,1,1,1,5,1,1,1,1]
weightO = [1,1,1,3,1,1,1,1,1]

outputX = []

output_set1_X = [a * b for a,b in zip(set_1, weightX)]
print(output_set1_X) 

output_set1_O = [a * b for a,b in zip(set_1, weightO)]
print(output_set1_O)

sum_X = sum(output_set1_X)
sum_O = sum(output_set1_O)
print("sum_X = ", sum_X, " ", "som_O =", sum_O, )

# softmaxfunction X=7 O=9
def softMax(sum_X, sum_O):
  help = math.exp(sum_X)/(math.exp(sum_X)+ math.exp(sum_O))
  sos = math.exp(sum_O)/(math.exp(sum_O)+ math.exp(sum_X)) 

#FRANK 

def softMax(outputs):
  exponentials = []
  for item in outputs:
    exponentials.append(math.exp(item))
  sum_exponentials = sum(exponentials)
  probabilities = []
  for item in exponentials:
    probabilities.append(item/sum_exponentials)
  return probabilities

# MEAN SQUARED ERRROR

def loss_function (probabilities, labels):
  loss = 0 
  if len(probabilities) != len(labels):
    raise IndexError("Labels en probabilities ijn niet even lang!")
  for i in range (len(probabilities)):
      error = labels[i]-probabilities[i]
      squared_error = error **2
      loss += squared_error
  return loss

outputs = [9,7]
labels = [1,0]
probabilities = [0.8, 0.2]

print(loss_function(softMax(outputs), labels))



""" 
oplossing Ruud: 
  def initWeights(set1)
  
    n = len(set_1)
    
    weights = []
    
    for index in range (0,n):
      weights.append(1.0)
    return weights
    
 v = mat2vec(s[0])
  weights = initWeights(v)
  
 print weight
 
 
def in2out)vec, weights):

  n = len(vec)
  
  Sum = 0.0
  
  #compute vec(i) * weigts[i]
  for i in range(0,n):
  
  
    Som += vec(i) * weigts[i]
  #TODO: softmax
  return math.sqrt.(Sum)
  
  v = mat2vec(s[0])
  w = initWeights(v)
  out = in2out (v, w)
  """
  #sum and return softmax
  
