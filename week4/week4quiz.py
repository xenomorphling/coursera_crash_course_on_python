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

