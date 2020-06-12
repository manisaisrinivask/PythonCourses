print("hello")
# This is a comment
# The below code sets a variable to equal a value
myVariable = 'Some String here'

# We will now print the variable
print(myVariable)

# Now lets concatenate a value to our string
print(myVariable+'Some Other Value Here')

# Lets use formatting to combine a string an a variable
stringVariable = 'This is a test of adding a variable: {}'.format(myVariable)
print(stringVariable)
# The double curly brackets act like a place holder that the internal function format subs {} with the variable value in this case "Some String Here"
# Format does this in order lets add a few variable to a format string

variable1 = "Hello"
variable2 = "Are"
variable3 = "Today"

myString = '{}, How {} You Doing {}?'.format(variable1,variable2,variable3)
print(myString)

# What happens if you change the order of formation
myString = '{}, How {} You Doing {}?'.format(variable3,variable2,variable1)
print(myString)