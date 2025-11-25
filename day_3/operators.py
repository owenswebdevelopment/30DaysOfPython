print("Addition:", 2 + 3)
print("Subtraction:", 2 - 3)
print("division:", 2 - 8)
print("multiplication:", 10 * 8)
print("Modulus:", 10 % 8) #It gives the reminder
print("Float:", 3.19) #float
print("multiplying complex numbers:", (3 + 7j) * (4 -6j))#float



#Declaring a variable

a = 2
b = 3

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


num_one = 2
num_two = 4

total = num_one + num_two
diff = num_one - num_two
division = num_one / num_two
multi = num_one * num_two
remainder = num_one % num_two

print('total:', total)
print('diff:', diff)
print('multi:', multi)
print('remainder:', remainder)


#calculating area of circle
radius_1 = 30
radius_of_circle_1 = 3.14 * radius_1 **2
print("Radius of Circle_1:", radius_of_circle_1)


radius = 10
radius_of_circle = 3.14 * radius **2
print("Area of circle:", radius_of_circle)

length = 10
width = 20
area_of_rectangle = length * width
print("Area of Rectangle", area_of_rectangle)

#calculating weight of an object

mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, "N")

#calculating density of a liquid
mass = 75 #kg
volume = 0.075 #cubic meter
density = mass / volume
print(density)

#comparison operator
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


print("1 is 1", 1 is 1)
print("1 is not 1", 1 is not 2)
print("O in Owen", "o" in "Owen")
print("4 is 2 ** 2", 4 is 2 ** 2)


#Logical operator

print(3 > 2 and 4 < 10)
print(10 > 30 and 4 < 10)
print("true and true", True and True)
print(10 > 30 and 4 < 10)
print(10 > 30 or 4 < 10)
print(10 > 2 or 4 < 1)
print(not 3 > 1)
print(not 3 < 1)
print(not False)
print(not True)
print(not not True)
print(not not False)

# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
