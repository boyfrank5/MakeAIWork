#!/usr/bin/env python3
# # Programmeren in Python - Lussen: while en for, blokken, break

granniesEuros = 100
honnestBillBankBalance = granniesEuros
trickyDickBankBalance = granniesEuros

year = 1


print ()
print ('  YR  |   HBB  |   TBB   |')
print ('======|========|=========|')

while honnestBillBankBalance <= 2*trickyDickBankBalance:
  honnestBillBankBalance *= 1.05
  trickyDickBankBalance += 10
  
  print (f'{year:2d}    : {honnestBillBankBalance:6.2f}     {trickyDickBankBalance:6.2f}')
  year += 1


     