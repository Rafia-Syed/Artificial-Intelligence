# Excercise 1
# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:

# def calc_volume(height, width, depth):
#     return height * width * depth

# def get_vol_label(volume):

#     if volume<=10:
#         return "Extra Small"

#     elif volume<=25:
#         return "Small"
    
#     elif volume <= 75:
#         return "Medium"
    
#     elif volume <= 100:
#         return "Large"
    
#     elif volume <= 250:
#         return "Extra Large"
    
#     else:
#         return "Extra-Extra Large"

# def main():
#     height = float(input("Enter the height of the cube: "))
#     width = float(input("Enter the width of the cube: "))
#     depth = float(input("Enter the depth of the cube: "))

#     volume = calc_volume(height, width, depth)
#     label = get_vol_label(volume)

#     print("Volume:", volume, "cm3")
#     print("Label:", label)

# main()

# (II)In a company ,worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas
# to leave the company, If the time taken by the worker is input through the keyboard,find the
# efficiency of the worker

# def calc_eff(time_taken):
#     if time_taken>=2 and time_taken<=3:
#         return "Highly Efficient"
#     elif time_taken>=3 and time_taken<=4:
#         return "Improve Speed"
#     elif time_taken>=4 and time_taken<=5:
#         return "Training Required"
#     elif time_taken>=5:
#         return "Leave the Company"
#     else:
#         return "Invalid Input"
    
# def main():
#     time_taken = float(input("Enter the time taken by the worker (in hours):"))
#     efficiency = calc_eff(time_taken)
#     print("Efficiency of the worker:", efficiency)

# main()        


# The program must prompt the user for a username and password. The program should compare
# the password given by the user to a known password. If the password matches, the program should
# display “Welcome!” If it doesn’t match, the program should display “I don’t know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123

# def main():
#     username = input("Enter your username: ")
#     password = input("Enter a password: ")

#     known_passwords = ['abc$123','ABC$123']

#     if password.lower() in known_passwords:
#         print("Welcome!")
#     else:
#         print("I don't know you.")
    
# main()


# Exercise 2:
# (i)What Would Python Print?

# n=3
# while n>=0:
#     n-=1
#     print(n)

# output is
    # 2
    # 1
    # 0
    # -1

# (ii): What Would Python Print?

# n=4
# while n>0:
#     n -=1
#     print(n)

# output is 3
    # 2
    # 1
    # 0

# (ii)Try the scenrio below:
# Make a program that lists the countries in the set
# 1. Create a loop that counts from 0 to 100

# for i in range(101):  #range start from the given value and ends before the given value
    # print(i)

# 2. Make a multiplication table using a loop
    
# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j, end='\t' )
#     print()    


# 3. Output the numbers 1 to 10 backwards using a loop
# for i in range(10,0,-1):
#     print(i)


# 4. Create a loop that counts all even numbers to 10
# num=0
# while num<=10:
#     print(num)
#     num += 2

# 5. Create a loop that sums the numbers from 100 to 200
# sum =0
# for i in range(100,201):
#     sum += i
#     print("Sum of the numbers from 100 to 200",sum)


# (iii) Try the exercise below:
# 1. Make a program that lists the countries in the set below using a while loop
# clist = ["Canada","USA","Mexico"]
# index=0

# while index < len(clist):
#     print(clist[index])
#     index +=1


# 3. Can you sum numbers in a while loop?
# sum=0
# i=1
# while i <= 10:
#     sum += i
#     i += 1
# print("the sum of no. from 1 to 10 is: ",sum)  


# 4. Can a for loop be used inside a while loop?
# Initialize a variable
# count = 0

# while count<2:
#     print("While Loop iteration",count)

#     #inner loop
#     for i in range(3):
#         print("Inner For Loop",i)

#     count +=1


# Lab 2b
# Task# 01:
# Write a program that converts a positive integer into the Roman number system. The Roman number system has digits I (1), V (5), X (10), L (50), C(100), D(500) and M(1000). Numbers up to 3999 are formed according to the following rules:  
# a) As in the decimal system, the thousands, hundreds, tens and ones are expressed separately.
#  b) The numbers 1 to 9 are expressed as: 1 I 6 VI 2 II 7 VII 3 III 8 VIII4 IV 9 IX 5 V (An I preceding a V or X is subtracted from the value, and there cannot be more than threeI’s in a row.) 
#  c) Tens and hundreds are done the same way, except that the letters X, L, C, and C, D, Mare used instead of I, V, X respectively.  
# Example: Your program should take an input, such as 1978, and convert it to Roman numerals, MCMLXXVIII
# def int_to_roman(num):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#     ]
#     symbol = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#     ]
#     roman_num = ''
#     i = 0
#     while num > 0:
#         for _ in range(num // val[i]):
#             roman_num += symbol[i]
#             num -= val[i]
#         i += 1
#     return roman_num

# # Get input from the user
# try:
#     number = int(input("Enter a positive integer: "))
#     if number < 1 or number > 3999:
#         raise ValueError("Number out of range (1-3999).")
#     roman = int_to_roman(number)
#     print(f"The Roman numeral representation of {number} is: {roman}")
# except ValueError as e:
#     print(e)


# Task# 02:
# Write a program that calculates the user’s body mass index (BMI) and classify it as underweight, normal, overweight, or obese, based on the table from the United States Centers for Disease Control
# def bmi_calc(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# def classify_bmi(bmi):
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 30:
#         return "Normal"
#     elif bmi <= 60:
#         return "Overweight"
#     else:
#         return "Obese"
    
# def main():
#     weight = float(input("Enter your weight in kilograms: "))
#     height = float(input("Enter your height in meters: "))

#     if weight <= 0 or height <= 0:
#         print("Please enter a valid positive values for weight and height.")
#         return

#     bmi = bmi_calc(weight, height)
#     print("Your BMI is: ",bmi)

#     classification = classify_bmi(bmi)
#     print("You are classified as: ",classification)


# main()


#Task # 03:
# Write a program to compute quotient and remainder of a number without using division ('/') operator and modulo ('%') operator. Also mention procedure for calculating
def quo_remaind(dividend, divisor):
    quotient = 0
    remainder = 0

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    remainder = dividend

    return quotient, remainder

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if divisor == 0:
        print("Error: Cannot divide by Zero.")
        return
    
    quotient, remainder = quo_remaind(dividend, divisor)
    print("Quotient", quotient)
    print("Remainder", remainder)

main()

# theory
# To compute the quotient and remainder of a number without using the division (/) operator and modulo (%) operator, we can use repeated subtraction. Here's the procedure:
# Initialize two variables, dividend and divisor, with the given dividend and divisor, respectively.
# Initialize two more variables, quotient and remainder, to 0.
# Repeat the following steps until the dividend is greater than or equal to the divisor:
# a. Subtract the divisor from the dividend.
# b. Increment the quotient by 1.
# The remainder is the final value of the dividend, and the quotient is the number of times the divisor was subtracted from the dividend.