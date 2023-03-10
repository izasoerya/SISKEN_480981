# -*- coding: utf-8 -*-
"""TUGAS SISKEN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yu3nRhp_emPm_rcgVZgi81LzEK1pjEzw
"""

#Nama : Ihza Surya Pratama
#NIM : 21/480981/PA/20923

def hitungrouth(valueinput, k):
  n = len(valueinput)
  tabelrouth = [[0 for j in range(n)] for i in range(n)]
  
  for i in range(0, n, 2):
    tabelrouth[0][i] = valueinput[i]
  for i in range(1, n, 2):
    tabelrouth[0][i] = k * valueinput[i]
  for i in range(1, n):
    tabelrouth[1][i-1] = -tabelrouth[0][0+i%2] * tabelrouth[0][1+i%2] / tabelrouth[0][0]
  for i in range(2, n):
    for j in range(0, n-i):
      tabelrouth[i][j] = ((tabelrouth[i-2][0] * tabelrouth[i-1][j+1]) - (tabelrouth[i-1][0] * tabelrouth[i-2][j+1])) / tabelrouth[i-2][0]
  return tabelrouth

def is_system_stable(tabelrouth):
  n = len(tabelrouth)
  num_sign_changes = 0
  for i in range(n-1):
    if tabelrouth[i][0] * tabelrouth[i+1][0] < 0:
      num_sign_changes += 1
    if num_sign_changes == 0:
      print("Sistem STABIL")
    elif num_sign_changes != 0:
      print("Sistem tidak STABIL")
    
if __name__ == '__main__':
  valueinput = list(map(float, input("Masukan nilai (pisahkan dengan koma): ").split(",")))
  k = float(input("Masukan nilai K: "))
  tabelrouth = hitungrouth(valueinput, k)
  print("Routh Table:")
  for row in tabelrouth:
      print(row)
  is_system_stable(tabelrouth)