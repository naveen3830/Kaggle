#!/usr/bin/env python
# coding: utf-8

# 1) Explain with an example each when to use a for loop and a while loop.

# i) for loop: A for loop is an iteration method that is best used when you know the number of iterations ahead of time. It’s always followed by the initialization, expression and increment statements.
# 
# Ex:Iterating over range 0 to n-1
# 
# n = 4
# 
# for i in range(0, n):
# 
#     print(i)
# 
# ii) while loop: A while loop is an iteration method that is best used when you don't know the number of iterations ahead of time. The contents of the loop are executed as long as the expression evaluates to true.
# 
# Ex: 
# 
# count = 0
# 
# while (count < 3):
# 
#     count = count + 1
#     
#     print("Hello world")

# 2) Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

# In[2]:


# Using for loop
sum1=0
for i in range(1,11,1):
    sum1=sum1+i
print(sum1)


# #Using while loop
# num=int(input("Enter a number:"))
# 
# if num<0:
#     print("Enter a positive integer")
# else:
#     s=0
#     while num>0:
#         s=s+num
#         num=num-1
#     print(s)

# 3) Create a python program to compute the electricity bill for a household.
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.

# In[4]:


units=int(input("Enter the number of units used:"))
if units<=100:
    print("The amount to be paid is",units*4.5,"rupees")
elif units<=200:
    print("The amount to be paid is",(100*4.5)+(units-100)*6,"rupees")
elif units<=300:
    print("The amount to be paid is",(100*4.5)+(100*6)+(units-200)*10,"rupees")
else:
    print("The amount to be paid is",(100*4.5)+(100*6)+(100*10)+(units-300)*20,"rupees")


# 4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list.

# In[2]:


# Using for loop
l=list(range(1,101,1))
l1=[]

for i in l:
    cube=i**3
    if cube%4==0 or cube%5==0:
        l1.append(cube)
        
print(l1)
        


# In[1]:


# Using while loop
numbers = list(range(1, 101))
cubes_divisible_by_4_or_5 = []

index = 0
while index < len(numbers):
    num = numbers[index]
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes_divisible_by_4_or_5.append(cube)
    index += 1

print(cubes_divisible_by_4_or_5)


# 5) Write a program to filter count vowels in the below-given string.string = "I want to become a data scientist"
# 
# 

# In[10]:


string = "I want to become a data scientist"

vowels = "aeiou"
vowel_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)

