# Variable
# Data types

name = "Jhon Doe" # string
year = 1995 # int
price = 29.99 # float
test = True # boolean

# Data input
# strings
inputName = input("Insert your name: ")
print(inputName)

# numbers
# Can be integers or floats

inputInteger = int(input("Insert your number: ")) # integer
inputFloat = float(input("Insert your float number: ")) # float

print(inputInteger) # if we insert a non integer number -> error
print(inputFloat) # if we insert a number it converts to float. Ex: int 10 -> float 10.0

# We can check the types
print(type(inputName))
print(type(inputInteger))
print(type(inputFloat))


