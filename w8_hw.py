# -*- coding: utf-8 -*-
"""w8 hw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fTvINhlZZkC4S0TRfK5-xPnXPBoJggza
"""

user_int=int(input("請輸入一個正整數"))
if user_int % 3 ==0:
  print("Fizz")

user_int=int(input("請輸入一個正整數"))
if user_int % 3 ==0:
  print("Fizz")
if user_int % 5 ==0:
  print("Buzz")

user_int=int(input("請輸入一個正整數"))
if user_int % 3 ==0 and user_int % 5 ==0:
  print("Fizz Buzz")
elif user_int % 5 ==0:
  print("Buzz")
elif user_int % 3 ==0:
  print("Fizz")
else:
  print(user_int)

user_int=int(input("請輸入一個正整數"))
if user_int % 3 ==0 and user_int % 5 ==0:
  print("Fizz Buzz")
elif user_int % 5 ==0:
  print("Buzz")
elif user_int % 3 ==0:
  print("Fizz")
else:
  print(user_int)

x = int(input("請輸入起始的正整數："))
y = int(input("請輸入終止的正整數："))
i = x 
while i <= y:
  if i % 2 == 1:
    print(i)
  i += 1

x = int(input("請輸入起始的正整數："))
y = int(input("請輸入終止的正整數："))
i = x 
counter = 0
while i <= y:
  if i % 2 == 1:
    print(i)
    counter += 1
  i += 1
print(counter)

i = 1
while i <= 100:
  if i % 15 == 0:
    print("Fizz Buzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
  i += 1