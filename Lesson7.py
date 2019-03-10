# 1.  dict comprehension exercise.
# #
# # Make a program that given a whole sentence (a string) will make a dict
# # containing all unique words as keys and the number of occurrences as
# # values.

given_sentence = "The sun is shining shining brightly, extremely brightly today".split()
result_dict = {element: given_sentence.count(element) for element in given_sentence}

print(result_dict)


# 2. List comprehension exercise I.
#
# Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Now, make a program (no longer than one line) that makes a new list
# containing all the values in a
# but no even numbers.


given_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([element for element in given_list if element%2 !=0])

# 3. List comprehension exercise II.
#
# Use a list comprehension to make a list containing tuples (i, j) where i
# goes from 1 to 10 and j is corresponding i squared.

given_list = [(i, i**2)for i in range(1,11)]
print(given_list)