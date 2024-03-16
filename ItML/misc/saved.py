# #7/11/22
# #A
# print("hello class")
# First_name = input("what is your name?")
# print(First_name)
# How_old = input("Enter the birth year")
# current_age = 2022 - int(How_old)
# print(current_age)

# #9/11/22
# #A
# languages=['C++','Python','Scratch']
# list1=[1,[2, 3],(4, 5),False,'No']
# print(list1)
# list1[3]

# print(list1[:-2])

# del list1[0]
# print(list1)

# #B
# mytuple = 1,2,3
# print(mytuple)
# a,b,c = mytuple
# print(a,b,c)

# #11/11/22
# #A
# str1 = 'hello students '
# str2 = 'how are you? '
# print(str1)
# print(str1[0:2]) #printing first two characters using slice operator
# print(str1[4]) #printing 4th character of the string
# print(str1*2) #printing the string twice
# print(str1 + str2) #printing the concatenation of str1 and str2

# #B
# list1=[1,"hi", "Python",2]
# #checking type of given list
# print(type(list1))
# print(list1)
# print(list1[3:])
# print(list1[:3])
# print(list1[0:2])
# print(list1 + list1)
# print(list1*3)

# #C
# tuple = ("hi","Python",2)
# print(type(tuple))
# print(tuple)
# print(tuple[1:])
# print(tuple[0:1])
# print(tuple + tuple)
# print(tuple*3)
# t[2] = "hi" #error dikhayega

# #D
# #Dictionary
# d = {1:' JIMMY',2:' ALEX',3:' JOHN',4:' MIKE'}
# #Accessing value using keys
# print("1st name is" +d[1])
# print("2nd name is" + d[4])
# #Printing dictionary
# print(d)
# print(d.keys())
# print(d.values())

# #E
# #Creating Empty set
# set1 = set()
# set2 = {'James',2,3,'Python'}
# #Printing set value
# print(set2)
# #Adding element to the set
# set2.add(10)
# print(set2)
# #Removing element from set
# set2.remove(2)
# print(set2)

# #31-11-22
# #A
# num1 = int(input("Enter the value of A"))
# num2 = int(input("Enter the value of B"))
# if int(num1)>int(num2):
#     print(int(num1) - int(num2))
# else:
#     print(int(num2) - int(num1))

# #B
# num1 = float(input("Enter the value"))
# num2 = float(input("Enter the value"))
# sum = num1 + num2
# print(sum)
# multiplication = num1*num2
# print(multiplication)
# if num1 > num2:
#     print(num1 - num2)
# else:
#     print((num2-num1))
# if num1 > num2:
#         print(num1/num2)
# else: print(num2/num1)

# #C
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if (num % 2) == 0:
#         print(num, 'is an even number')
#     elif (num % 3) == 0:
#         print(num, 'is an odd number')
#     else: print(num, 'is a prime number')

# #2-12-22
# #A
# def myFunction():
#     return True
# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# #B
# marks = int(input("Enter the marks"))
# if (marks > 85) and (marks < 100):
#     print("Congrats! You scored grade A")
# elif (marks > 60) and (marks < 85):
#     print("You scored grade B+")
# elif (marks > 40) and (marks <= 60):
#     print("You scored grade B")
# elif (marks > 30) and (marks <= 40):
#     print("You scored grade C")
# else:
#     print("Sorry you are fail")

# #5-12-22
# #A
# def sum(a,b):
#     return a+b
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# print("Sum=", sum(a,b))

# def sub(a,b):
#     if a>b:
#         return a-b
#     else:
#         return b-a
# print("Sub=", sub(a,b))

# def mul(a,b):
#     return a*b
# print("mul=", mul(a,b))

# def div(a,b):
#     if a>b:
#         return a/b
#     else:
#         b/a
# print("div=", div(a,b))

# #B
# def addnum():
#     fnum = int(input("Enter A:"))
#     snum = int(input("Enter B:"))
#     sum = fnum + snum
#     print("The sum of", fnum, "and", snum, "is", sum)
# addnum()

# #C
# def sum():
#     a = 10
#     b = 7
#     c = a + b
#     return c
# print("The sum is", sum())

# #7-12-22
# #A
# def calcAreaPeri(Length, Breadth):
#     area = Length*Breadth
#     peri = 2 * (Length + Breadth)
#     return (area, peri)
# length = float(input("Enter the length of the rectangle:"))
# breadth = float(input("Enter the value of the rectangle:"))
# area, perimeter = calcAreaPeri(length, breadth)
# print("Area is", area, "\nPerimeter is", perimeter)

# #B
# def printme(name,age=22):
#     print("My name is", name, "and age is", age)
# printme(name= "John")
# printme(age=10, name="David")

# #C
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))
# num = 5
# print("The factorial of", num, "is", factorial(num))

# #D
# def func(name1, message, name2):
#     print("Printing the message with", name1, ",", message, name2)
# func(name2="Tarun",message="hello",name1="Dheeraj")
# #positional argument > keyword argument

# #9-12-22
# #A
# #main file
# def summation(a,b):
#     return a+b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     return a/b
# #pythoon file
# #from main import summation
# a = float(input("Enter the first number\n"))
# b = float(input("Enter the second number\n"))
# print("Sum=", summation(a, b))

# #B
# #mymodule file
# def greeting(name):
#     print("hello," + name)
# #pytron file
# import mymodule
# mymodule.greeting("Tarun")

#  #14-12-22
#  #A
# i = 1
# while True:
#     if i % 3 == 0:
#       break
#     print(i)
# i += 1

# #Fibonacci Series
# num = int(input("Enter any number"))
# n1, n2 = 0, 1
# sum = 0

# if num<=0:
#     print('Please enter number greater than 0')
# else:
#     for i in range (0, num):
#         print(sum, end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2

# # Reversing a string
# def reverse_str(str):
#     str1=str[::-1]
#     return str1

# str=input("enter a string: ")
# temp=str
# print("orginal string: ",str)
# print("after reversing the string: ",reverse_str(str))

# # sum of sqrt of 3 numbers
# num1 = float(input('Enter a number:'))
# num1_sqrt = num1 ** 0.5
# num2 = float(input('Enter a number:'))
# num2_sqrt = num2 ** 0.5
# num3 = float(input('Enter a number:'))
# num3_sqrt = num3 ** 0.5

# sum = num1_sqrt + num2_sqrt + num3_sqrt
# print(sum)

# #25-1-23
# #A
# from array import *
# array1 = array('i', [10, 20, 30, 40, 50, 60, 70])
# count = 0
# for x in array1:
#     count = count + 1
# print(count)
# print(len(array1))

# #PYTHON ESSENTIALS
# currencies = set()
# num_currencies = int(input("Enter Number of Currencies: "))
# for i in range(num_currencies):
#     country = input("Enter the name of the country: ")
#     currencies.add(country)
# print(len(currencies))

# employees = {
#     "Sunny": {"salary": 25000},
#     "Ravi": {"salary": 23000},
#     "Vijay": {"salary": 26000},
#     "Messi": {"salary": 30000}
# }
# employee_name = input("Enter the name of the employee: ")
# if employee_name in employees:
#     employees.pop(employee_name)
# print(employees)

# import statistics

# marks = list(map(int, input("Enter 7 integers with spaces: ").split()))

# if len(marks) < 7:
#     print("Error: Not enough students.")
# else:
#      mean = statistics.mean(marks)
#      stdev = statistics.stdev(marks)
#      print(f"Mean is: {mean}")
#      print(f"Standard Deviation is: {stdev}")


# num_words = int(input("Enter the number of words: "))
# words = []
# for i in range(num_words):
#     words.append(input("Enter a word: "))
# longest_word = ""
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print(f"The word with the longest length is: {longest_word}")

# fruits = {"apple": 1, "banana": 2, "cherry": 3}
# remo = input("Enter a key to remove: ")
# fruits.pop(remo, None)
# print(fruits)

# #27-1-23
# #A
# setn = {5, 10, 3, 15, 2, 20}
# print("Original set elements: ")
# print(setn)
# print(type(setn))
# print("\nMximum value of the said set: ")
# print(max(setn))
# print("\nMinimum value of the said set: ")
# print(min(setn))

# #13-2-23
# #A
# a = [1, 1, 1, 3, 4, 5, 5, 5, 5, 7, 7, 7, 7, 9, 9]
# i = 0
# l = len(a) - 1
# while i < l :
#     if a[i] == a[i+1]:
#         del a[i+1]
#         l -= 1
#     else :
#         i += 1
# print(a)

# #B
# a = [1, 1, 1, 3, 4, 5, 5, 5, 5, 7, 7, 7, 7, 9, 9]
# for i in range(len(a)-1,0,-1):
#     if a[i] == a[i-1]:
#         del a[i]
# print(a)

# print("\U0001F61D")

# n=1
# counta = 0
# countb = 0
# for i in range(1,6):
#     a = int(input("Enter a number: "))
#     if a ==1:
#         print("Player 1 has won the toss")
#         counta = counta+1
#     elif a==2:
#         print("Player 2 has won the toss")
#         countb = countb+1
#     n=n+1
# if counta>countb:
#     print("Player 1 wins the cake")
# else:
#     print("Player 2 wins the cake")

