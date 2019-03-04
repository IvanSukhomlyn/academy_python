# # 1. List of squared values
#
# x = list(range(1,101,1))
# r = []
# for element in x:
#     y = (element * element)
#     r.append(y)
# print(list(r))

# # 2. List of car names
#
# a = ("Name a car, or print 'q' to quit")
# print(a)
# car = input()
# cars_list = []
# while car != "q":
#     cars_list.append(car)
#     print("type in another car")
#     if car == "q":
#         break
#     car = input()
# print(cars_list)

# 3. Print the list of 10 elements in reverse order

x = list(range(1, 11, 1))
print (x[::-1])