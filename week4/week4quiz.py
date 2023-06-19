# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = ([])
# for index, filename in enumerate(filenames):
#     var = newfilenames == newfilenames.append(filename.replace(".hpp", ".h"))
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



# def pig_latin(text):
#   say = ""
#   words = text.split()
#   for word in words:
#     say += ("" + word[1:] + word[0] + "ay ")
#   return(say)

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

"""
Fill in the blanks to make the code convert a permission in octal format into a string format.
"""

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     # Iterate over each of the digits in octal
#     for right in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if right >= value:
#                 result += letter
#                 right -= value
#             else:
#                 result += "-"
#     return result
    
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------


# def group_list(group, users):
#   members = []
#   members = (("\"{}: {}\"".format(group,users)).replace('[', ''))
#   members = members.replace(']', '')
#   members = members.replace('\'', '')
#   return members

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) 
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) 
# print(group_list("Users", "")) 

# def group_list(group, users):
#   result = []
#   for user in users:
#     result.append("{}".format(user))
#   return result

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) 
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) 
# print(group_list("Users", "")) 
# Should be "Marketing: Mike, Karen, Jake, Tasha"
# Should be "Engineering: Kim, Jay, Tom"
# Should be "Users:"

# def full_emails(people):
#   result = []
#   for email, name in people:
#     result.append("{} <{}>".format(name, email))
#   return result
# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

# def guest_list(guests):
#   for tuple in guests:
#     print("{} is {} years old and works os {}".format(tuple[0], tuple[1], tuple[2]))
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39 # Epilogue starts on page 39
# toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
# print(toc) # What are the current contents of the dictionary?
# print("Chapter 5" in toc) # Is there a Chapter 5?


"""
Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1. 
"""

# def get_word(sentence, n):
# 	# Only proceed if n is positive 
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words 
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")

# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing

"""
Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
"""

# def file_size(file_info):
# 	name, type, size = file_info
# 	return("{:.2f}".format(size / 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
# print(file_size(('Notes', 'txt', 496))) # Should print 0.48
# print(file_size(('Program', 'py', 1239))) # Should print 1.21

"""
Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.
"""

# def skip_elements(elements):
#     result = []
#     for index, element in enumerate(elements):
#         if index % 2 == 0:
#             result.append(element)
#     return result

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

"""
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
"""

# def odd_numbers(n):
#     return [x for x in range(1,n+1) if x % 2 == 1]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []


"""
Now, it's your turn! Have a go at iterating over a dictionary!
Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
"""

# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for animal, item in cool_beasts.items():
#     print("{} have {}".format(animal, item))

"""
Use the len() function to measure a string.
"""

# This function accepts a string variable "data_field".  
# def count_words(data_field):

#     # Splits the string into individual words. 
#     split_data = data_field.split()
#     # Then returns the number of words in the string using the len()
#     # function. 
#     return len(split_data)
#     # Note that it is possible to combine the len() function and the 
#     # .split() method into the same line of code by inserting the 
#     # data_field.split() command into the the len() function parameters.

# # Call to the function
# count_words("Catalog item 3523: Organic raw pumpkin seeds in shell")
# # Should print 9

