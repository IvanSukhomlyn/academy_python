# 1. The Guessing Game.

# import random
#
# while True:
#     a = int(input("type in the digit between 1 and 10"))
#     b = random.randint(1, 10)
#     if a == b:
#         print ("yay")
#         break
#     else:
#         print("try again")
#         continue

# 2. The birthday greeting program.

name = input("Hi, what is your name?")
print("how old are you?")
age = int(input())
age2 = str((age) + 1)
print("Hello " + (name) + ", on your next birthday you’ll be " + (age2) + " years")