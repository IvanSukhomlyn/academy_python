# # 1.  Exclusive common numbers
#
# import random
# x=[]
# y=[]
# for i in range (10):
#     x.append(random.randrange(1,10,1))
#     y.append(random.randrange(1,10,1))
# print("First list is: ", x)
# print("Second list is ", y)
# print
# z = (set(x).intersection(y))
# print("Common numbers are: ", z)

# 2. Extracting numbers.

x = list(range(1, 101))
y = []
print("The list is: ", x)
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        y.append(i)

print("All integers from the list that are divisible by 7 but not a multiple of 5 are: ",  list(y))
