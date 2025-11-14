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
