import datetime
# The above code imports a library, a library is a collection of beneficial functions to allow certain common tasks
# to be completed without having to write code

print(datetime.datetime.now())
# Let us format the datetime object
print(datetime.datetime.now().strftime("%d/%m/%y"))
# Let us change from / to -
print(datetime.datetime.now().strftime("%d-%m-%y"))
# Let us change from 2 place year to 4
print(datetime.datetime.now().strftime("%d-%m-%Y"))