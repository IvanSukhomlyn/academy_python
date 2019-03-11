# 1.  A simple function.
#
# Create a simple function called favourite_movie, which takes a string
# containing the name of your favourite movie. The function should then
# print “My favourite movie is name”.

def favourite_movie():
    movie = input("Tell me your favourite movie ")
    return "My favourite movie is " + str(movie)


movie = favourite_movie()
print(movie)


# 2. Creating a dictionary.
#
# Create a function called make_country, which takes in a country’s name and
# capital as parameters. Then create a dictionary from those parameters,
# with ‘name’ and ‘capital’ as keys. Make the function print out the values
# of the dictionary to make sure that it works as intended.

def make_country(name: str, capital: str):
    return {name, capital}

name = "Ukraine"
capital = "Kyiv"
print(make_country(name, capital))

# 3. A simple calculator.
#
# Create a function called make_operation, which takes in a simple
# arithmetic operator as a first parameter (to keep things simple let it
# only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only
# numbers) as second parameter. Then return the sum or product of all the
# numbers in the arbitrary parameter. For example:
#
# the call make_operation(‘+’, 7, 7,
# 2) should return 16
#
# The call make_operation(‘-’, 5, 5,
# -10, -20) should return 30
#
# The call make_operation(‘*’, 7, 6)
# should return 42

def make_operation(arithmetic_operator: str,  *args: int):
    return_value = args[0]
    for num in args[1:]:
        if arithmetic_operator == "*":
                return_value *= num
        elif arithmetic_operator == "-":
                return_value -= num
        elif arithmetic_operator == "+":
                return_value += num
        else:
            print("choose simple arithmetic operators only: ('*' or '-' or '+')")
        break
    return return_value

print(make_operation("*", 5,6))
print(make_operation("-", 5,6))
print(make_operation("+", 5,6))
print(make_operation("/", 5,6))



