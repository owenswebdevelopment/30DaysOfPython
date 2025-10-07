import math

#Check the python version you are using
#Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition(+)
#subtraction(-)
#multiplication(*)
#modulus(%)
#division(/)
#exponential(**)
#floor division operator(//)
#Write strings on the python interactive shell. The strings are the following:
#Your name
#Your family name
#Your country
#I am enjoying 30 days of python

print(2+3)
print(2-4)
print(4*5)
print(20%2) #result=0
print(9/18)
print(3**6) #3*3*3*3*3*3=729
print(10//2) #5
print('Owen')
print('Newsome')
print('Jamaica')
print('I am enjoying 30 days of python')

#data types
print(type('Owen')) #string
print(type([1, 2, 3, 4, 5])) #integer
print(type((1, 2, 3, 2.3, 5))) #list
print(type({'Owen': 'first name'})) #dictionary
print(type({.5, 2, 'owen'}))


x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2) #put everthing in
print(distance)
