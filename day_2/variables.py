import math

#Day 2: 30 Days of python programming'
first_name = 'Owen'
last_name = 'Newsome'
full_name = 'Owen Newsome'
country = 'Jamaica'
city = 'Kingston'
age = '20'
year = '2025'
is_married = 'true'
is_true = 'true'
is_light_on = 'true'

#check the type of data
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#check the length of the variables
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(country))
print(len(city))
print(len(age))
print(len(year))
print(len(is_married))
print(len(is_true))
print(len(is_light_on))

#compare the length of first name and last name
# print(len(first_name, last_name))
if len(first_name) > len(last_name):
    print('First name is longer than last name')
elif len(first_name) < len(last_name):
    print('Last name is longer than first name')
else:
    print('They are both the same length')


first_name = input("What is your first name?: ")
first_last = input("What is your last name?: ")
country = input("Which country are you from?: ")
age = input("How old are you?: ")

print("User Info")
print("First Name:", first_name, "Last Name:", last_name, "Country:", country, "Age:", age)
print(age)


#declare 5 and 4
num_one = 5
num_two = 4
total = num_one + num_two
print('the total:', total)
diff = num_one - num_two
print('the dif:', diff)
product = num_one * num_two
print('the product:', product)
division = num_one / num_two
print('the total:', division)

remainder = num_one % num_two
print('the remainder:', remainder)

exp = (num_one)**num_two
print(exp)

floor_division = num_one//num_two
print(floor_division)




try:
    circle_radius = float(input("What is the radius: "))
    area = math.pi * (circle_radius ** 2)
    print(f'This area the circle is: {area:.2f}')

    circum_of_circle = 2 * math.pi * circle_radius
    print(f'This is the circumference: {circum_of_circle:.2f}')
except ValueError:
    print('Please enter a valid number')
