#!/usr/bin/python3


# ASSIGNMENT
# Multiplicate two vectors and use a 'for' loop.

import re


matrix_A = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix_B = [[1,2,3,0],
            [4,5,6,7],
            [7,8,9,9]]

def multiplier(matrix_A, matrix_B):
  result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
  if len(matrix_A[0]) == len(matrix_B):
    for rowIndex in range(len(matrix_A)):
      for columnIndex in range(len(matrix_B[0])):
        for termIndex in range(len(matrix_A[0])):
          result[rowIndex][columnIndex] += matrix_A[rowIndex][termIndex] * matrix_B[termIndex][columnIndex]
          #result[rowIndex][columnIndex] = result[rowIndex][columnIndex]+ matrix_A[rowIndex][termIndex] * matrix_B[termIndex][columnIndex]
  else:
     print('Dat kan niet')
 
  for row in result:
    print(row)
  return result



x=multiplier(matrix_A,matrix_B)
print(x)

  