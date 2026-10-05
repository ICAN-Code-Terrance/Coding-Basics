# This is a comment! You can tell that this is a comment 
# because this line of code starts with a '#' symbol.
# This will allow you to write about what you're doing 
# without affecting your code!

# Variables
# Variables are placeholders for data values 
# The basic 5 variables are char, str, int, float, and bool

# char - This datatype handles singular characters
testChar = 'Z'

# str - This datatype handles multiple characters in an array
testString = "Terrance"

# int - This datatype handles whole numbers 
testInt = 67

# float - This datatype handles decimal numbers
testFloat = 3.14

# bool - This datatype handles where something is true or false
testBool = True

# Let's write our first lines of code

print("Hello World!")
print("Hey " + testString)

print("My favorite letter is " + testChar)

# Sometimes you want a number to be used as a string instead of as a number
# Casting lets you change the datatype of a variable 
x = str(testInt)
y = float(testInt)
z = int(testInt)

print("My favorite number is " + x)

print(z + z)

print(y)
