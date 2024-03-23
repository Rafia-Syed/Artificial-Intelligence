# Exercise: Dir and Help

s = 'hello world'

print(s.capitalize())

print(s.count('l'))

print(s.endswith('d'))

print(s.isalpha())

print(s.replace('hello', 'AI'))

print(s.find('o'))
print(s.find('x'))

# Write a Python program to swap 4 variables values
a = 5
b= 72
c= 46
d= 9
print("Before Swapping")
print('a=',a,'b=',b,'c=',c,'d=',d)

a,b,c,d = d,c,b,a

print("After Swaping")
print('a=',a,'b=',b,'c=',c,'d=',d)


# Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.

# celsius = float(input("Enter a temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperature in Fahrenheit is: {fahrenheit}F")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)


# list1.reverse()
# print(list1)

# list1.remove(3)
# print(list1)

# list1.append(4)
# print(list1)

# help(list.append)


# Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings.

list1 = ['abc', 'xyu', 'bab', '1221']
count = 0
for word in list1:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print(count)

# Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result = {**dic1,**dic2,**dic3}
print(result)


lowercase=[s.lower() for s in list1 if len(s)>5]

# Write a Python program to print a specified list after removing the 0th, 4th and 5th element

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
del sample_list[5]
del sample_list[4]
del sample_list[0]
print(sample_list)


# Identity Operators in Python
x = 6
if (type(x) is int):
    print ("true")
else:
    print ("false")

# Answer is True


# if(type(x) x = 7.2):
#     if (type(x) is not int):
#         print ("true")
# else:
#     print ("false")

# Answer is True


# Membership operator:
list1=[1,2,3,4,5]
list2=[6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")

#  Answer is nor overlapping


a = 7
a //= 3
a **= 5
print("floor divide =", a)
print("exponent =", a)


# Exercise Create a Python Program that perform following tasks for any problem of your choice: Task 1: Introduction Task 2: Terminal Task 3: Python Interpreter Task 4: Variables Task 5: Text Editor Task 6: Functions Task 7: Lists and Tuples Task 8: Conditional Statements Task 9: The For Loop Task 10: User Input and the While Loop

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")

import random

# Generate a random number between 1 and 100
hidden_number = random.randint(1, 100)

def guess_number():
    return int(input("Enter your guess: "))

# Lists and Tuples
guesses = []


while True:
    user_guess = guess_number()
    guesses.append(user_guess)
    
    if user_guess < hidden_number:
        print("Too low! Try again.")
    elif user_guess > hidden_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {hidden_number} correctly!")
        print(f"It took you {len(guesses)} guesses.")
        print("Your guesses:", guesses)
        break
