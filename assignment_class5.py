# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).
# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]

# weeks=len(temperatures)
# print(weeks)
# forweek_28=print(temperatures[27])


# """
# Extracting a Substring from a Sentence
# Objective: Given a sentence, extract and print a specific word using string slicing.
#sentence = "The quick brown fox jumps over the lazy dog"
# # extract third word "brow"

# word=sentence.index("b")
# print(word)
# print(sentence[10:15])

#OR

# word="brown"
# if word in sentence:
#     print(word)
# else:
#     print("word not found")



# """
# Extracting a Sublist of Favorite Colors
# Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
# favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
# # extract first three colors
# # """

# print(favorite_colors[0:3])

# Write a Python program to check if a list is empty or not.
# list=[]
# print(list)

# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc

# students = [1,2,3,4,5,6,7,8,9,10]    
# for x in range(len(students)):
#     print(students[x])
    

# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc

# for x in range(35,51):
#     print(x)

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

# for x in reversed(range(-25,-14)):
#     print(x)

# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

# for x in range(5,-11,-1):
#     print(x)

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

# for x in range(0,51,3):
#     print(x)


# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc
# for x in range(1,11):
#     mul= 2*x
#     print("2 x "+str(x)+" = "+str(mul))

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

# list=[3, 5, 2, 1, 4]
# x=0
# for i in list:
#     x+=i
# print(x)

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

# list=[3, 5, 2, 1, 4]
# x=list[0]
# for i in list:
#     if i > x:
#         x=i
# print("largest number = "+str(x))

# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]
# x=0
# for i in numbers:
#     x+=i
# print("sum of numbers = " + str(x))



# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]
# even=[]
# odd=[]

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     elif i % 2 != 0:
#         odd.append(i)
# print(len(even))
# print(len(odd))



# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# # output should like
# # "Index: 0 Element: apple"
# # "Index: 1 Element: banana"
# # "Index: 2 Element: cherry"
# index=0
# for x in fruits:
#     print("index: " +str(fruits.index(x)) + " Element: " + x) 


# # Create a List of Even Numbers from 1 to 20
# # Objective: Write a Python program that creates a list of all even numbers from 1 to 20.
# for x in range(1,21):
#     if x%2==0:
#         print(x)

# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# list3=[]
# for x in list1:
#     if x in list2:
#         list3.append(x)
# print(list3)

# Find the Length of Each String in a List
# Objective: Write a Python program that finds and prints the length of each string in a given list.
# Example list
# strings = ["apple", "banana", "cherry", "date"]
# for x in strings:
#     print("Element: "+ x +" Lenght: "+str(len(x)))