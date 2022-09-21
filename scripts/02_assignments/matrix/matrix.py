#!/usr/bin/python3

matrix_A = [[1,2,3],[4,5,6],[7,8,9]]
matrix_B = [[1,2,3,0],[4,5,6,7],[7,8,9,9]]
# result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

class Matrix:
  def __init__(self, vectorList, kleur):
    self.vectorList = vectorList
    self.kl = kleur 
    
  # def Main:
  #   Matrix_A = Matrix[[1,2,3],[4,5,6],[7,8,9]]
  #   matrix_B = Matrix[[1,2,3,0],[4,5,6,7],[7,8,9,9]]
  
  def print_vectorlist(self):
    print(self.vectorList)
    
    
  def add (self, matrix_B):
    self.vectorlist + matrix_B.vectorlist
    
  def multiply(self, matrix_B):
    vectorListB = matrix_B.vectorList
    
    if len(self.vectorList[0]) == len(vectorListB):
      for rowIndex in range ( len(self.vectorList) ):
        for columnIndex in range ( len (self.vectorListB) ):
          for termIndex in range(len(self.vectorList[0])):
            [rowIndex][columnIndex] += self.matrix_A[rowIndex][termIndex] * matrix_B[termIndex][columnIndex]

    else:
      print('Dat kan niet')
 










MatrixA_obj = Matrix(matrix_A,'rood')

MatrixB_obj = Matrix(matrix_B, 'groen')

MatrixA_obj.print_vectorlist()

print(MatrixB_obj.vectorList)

MatrixA_obj.multiply(MatrixB_obj)





#  print(matrix_A+matrix_B)
    
    
    
# def sumOfVectors (a,b):
#     c = [a[0] + b[0], a[1] + b[1], a[2] + b [2]]
#     return c

# a = [0,3,1]
# b = [1,4,9]
# c = sumOfVectors(a,b)

# print (sumOfVectors(a,b))
# print (c)



# #________



# matrix_A = [[1,2,3],[4,5,6],[7,8,9]]
# matrix_B = [[1,2,3,0],[4,5,6,7],[7,8,9,9]]
# result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# def multiplier(matrix_A, matrix_B):

#   if len(matrix_A[0]) == len(matrix_B):
#     for rowIndex in range(len(matrix_A)):
#       for columnIndex in range(len(matrix_B[0])):
#         for termIndex in range(len(matrix_A[0])):
#           result[rowIndex][columnIndex] += matrix_A[rowIndex][termIndex] * matrix_B[termIndex][columnIndex]

#   else:
#      print('Dat kan niet')
 
#   for row in result:
#     print(row)


# multiplier(matrix_A,matrix_B)
