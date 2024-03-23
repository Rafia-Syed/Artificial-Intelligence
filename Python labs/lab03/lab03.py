# Exercise 1
# Perform the given operations
# I. a Python program to square and cube every number in a given list of integers using Lambda

list = {2,4,5,6,11}
sq = lambda x: x ** 2
cube = lambda x: x ** 3

print("Original list" , list)
print("Square List:", [sq(num) for num in list])
print("Cube List:", [cube(num) for num in list])


#II. a Python program to find if a given string starts with a given character using Lambda.

starts_with_char = lambda string, char: string.startswith(char)

string = "Hello"
char = "H"


result = starts_with_char(string, char)


if result:
    print(f"The string '{string}' starts with the character '{char}'.")
else:
    print(f"The string '{string}' does not start with the character '{char}'.")


#III. a Python program to extract year, month, date and time using Lambda.
from datetime import datetime

extract_info = lambda dt: (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

current_datetime = datetime.now()

year, month, day, hour, minute, second = extract_info(current_datetime)

print("Year:", year)
print("Month:", month)
print("Date:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)


#Exercise 2
# I. You have collected information about cities in your province. You decide to store each city’s name, population, and mayor in a file. Write a python program to accept the data for a number of cities from the keyboard and store the data in a file in the order in which they’re entered. 
def main():

    num_cities = int(input("Enter the number of cities: "))

    with open("city_data.txt", "w") as file:
        # Iterate over each city
        for i in range(1, num_cities + 1):
            print(f"\nEnter data for city {i}:")
            city_name = input("City name: ")
            population = input("Population: ")
            mayor = input("Mayor: ")

            file.write(f"{city_name},{population},{mayor}\n")

    print("City data has been successfully stored in 'city_data.txt'.")

    with open("city_data.txt", "r") as file:
        print("\nContents of 'city_data.txt':")
        print(file.read())

main()


# II. Write a python program to create a data file student.txt and append the message “Now we are AI   students”s
def main():

    with open("student.txt", "a") as file:
        file.write("Now we are AI students")

    print("Message appended to 'student.txt'.")

main()
