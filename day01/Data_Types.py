#Create one variable for each data type — str, int, float, bool, None and print each one.
name = "Satya Narayana"
age = 19
hight = 5.9
is_student = True
relation_status = None

print(f"my name is {name}, my age is {age}, my hight is {hight}, i a student {is_student}, relationship status is {relation_status}")


#Create any variable and print its type using type().
print(type(name))
print(type(age))
print(type(hight))


#Create 3 variables with different types and print all their types in one go.
print(type(name), type(age), type(hight))

#Create a variable age = "25" (as string) and convert it to an integer, then print the type to confirm.
age = "25"
age = int(age)
print(type(age))


#Create a float variable price = 9.99 and convert it to an integer — what happens to the decimal?
price = 9.99
price = int(price)
print(price)


#Create an integer 100 and convert it to a string, then join it with another string and print.
interger = 100
interger = str(interger)
print(interger + " is my lucky number")


#Create variables of 3 different types, check their types using type() and print a sentence describing each one.
name = "Satya Narayana"
age = 19
hight = 5.9
name_type = type(name)
age_type = type(age)
hight_type = type(hight)

print(f"{name} = {name_type} {age} = {age_type} {hight} = {hight_type} ")


#Try converting "hello" to an integer — what happens? What error do you get and why?
message = "hello"
conversion = int(message)
print(conversion)