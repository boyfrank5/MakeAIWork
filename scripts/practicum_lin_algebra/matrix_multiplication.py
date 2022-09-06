#!/usr/bin/python3
import random as ra
from random import randint

# ASSIGNMENT
# Multiplicate two vectors and use a 'for' loop.

# NEXT STEP USE THE RANDOM FUNCTION TO CREATE A MATRIX INCLUSIVE RANDOM LENGTH


matrix_A = [[1,2,3],[4,5,6],[7,8,9]]
matrix_B = [[1,2,3,0],[4,5,6,7],[7,8,9,9]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def multiplier(matrix1, matrix2):

  if len(matrix_A[0]) == len(matrix_B):
    for rowIndex in range(len(matrix_A)):
      for columnIndex in range(len(matrix_B[0])):
        for termIndex in range(len(matrix_A[0])):
          result[rowIndex][columnIndex] += matrix_A[rowIndex][termIndex] * matrix_B[termIndex][columnIndex]

  else:
     print('dat kan niet')
 
  for row in result:
    print(row)


multiplier(matrix_A,matrix_B)

  