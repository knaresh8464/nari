# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# x=input("enter:")
# value=[]
# items=x.split(",")
# for p in items:
#     q=int(p,10)
#     if q%5==0:
#         value.append(p)
# print(value)
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
# digit of the number is an even number.


# l=['0','2','4','6','8']
# for i in range(1000, 3001):
#     for j in str(i):
#         if j not in l:
#             break
#     else:
#         print(i)
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# s = input("enter the test and numbers: ")
# d={"DIGITS": 0 ,"LETTERS": 0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
#
# print("LETTERS", d["LETTERS"])
#  print("DIGITS", d["DIGITS"])
# # Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# while True:
#  r=input("text:")
#  m={"upper case":0 , "lower case":0}
#  for c in r:
#     if c.isupper():
#         m["upper case"]+=1
#     elif c.islower():
#         m["lower case"]+=1
#     else:
#         pass
#  print("upper case" , m["upper case"])
#  print("lower case" , m["lower case"])
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# a = input()
# n1 = int("%s" % (a))
# n2 = int("%s%s" % (a,a))
# n3 = int("%s%s%s" % (a,a,a))
# n4 = int("%s%s%s%s" % (a,a,a,a))
# print(n1+n2+n3+n4)
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print(numbers)
# Write a program that computes the net amount of a bank account based a transaction log from console input. The
# transaction log format is shown as following:
# D 100,W 200
# D means deposit while W means withdrawal.
# netamount=0
# while True:
#     d=input()
#     if not d:
#         break
#     values=d.split(" ")
#     operation=values[0]
#     amount= int (values[1])
#     if operation=="D":
#         netamount+=amount
#     elif operation=="w":
#         netamount-=amount
#     else:
#         pass
# print(netamount)
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# import re
# value = []
# items=[x for x in input("enter the password:").split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(value)
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# from operator import itemgetter
# l=[]
# while True:
#     e=input("input data:")
#     if not e:
#         break
#     l.append(tuple(e.split(",")))
#
# print(sorted(l,key=itemgetter(0,1,2)))
# can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# class iterator(object):
#   def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# for i in iterator():
# #  print (i)
# class iterator(object):
#     """docstring for iterator"""
#     def __init__(self, n):
#         super(iterator, self).__init__()
#         self.n = n
#     def divBySeven(self):
#         for i in range(0, self.n):
#             if i % 7 == 0:
#                 yield i
# for num in iterator(100).divBySeven():
#     print(num)
import math
pos =[0,0]
while True:
    s=input(">")
    if not s:
        break
    movement=s.split(",")
    direction=movement[0]
    steps=int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFET":
       pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))