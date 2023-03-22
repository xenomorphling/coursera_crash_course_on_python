"""
1. The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 
Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:
accept a string through the parameters of the function;
separate the address string into new strings: house_number and street_name; 
return the variables in the string format: "House number X on a street named Y". 
"""

# def format_address(address_string):
#     house_number = ""
#     street_name = ""
#     # Separate the house number from the street name.
#     address_parts = address_string.split()
#     for address_part in address_parts:
#        # Complete the if-statement with a string method.
#        if address_part.isdigit():
#          house_number = address_part
#        else:
#          street_name += address_part + " "
#     # Remove the extra space at the end of the last "street_name".
#     street_name = ("House number {} on a street named {}".format(house_number, street_name.rstrip()))
#     # Use a string method to return the required formatted string.
#     return street_name

# print(format_address("123 Main Street"))
# # Should print: "House number 123 on a street named Main Street"
# print(format_address("1001 1st Ave"))
# # Should print: "House number 1001 on a street named 1st Ave"
# print(format_address("55 North Center Drive"))
# # Should print "House number 55 on a street named North Center Drive"


"""
Question 2
Fill in the blank to complete the “highlight_word” function. This function should change the given “word” to its upper-case version in a given “sentence”. Complete the string method needed in this function so that a function call like "highlight_word("Have a nice day", "nice")" will return the output "Have a NICE day".
"""

# def highlight_word(sentence, word):
#     # Complete the return statement using a string method.
#     return sentence.replace(word, word.upper())


# print(highlight_word("Have a nice day", "nice"))
# # Should print: "Have a NICE day"
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# # Should print: "Shhh, don't be so LOUD!"
# print(highlight_word("Automating with Python is fun", "fun"))
# # Should print: "Automating with Python is FUN"

# print(highlight_word("Have a nice day", "nice"))
# # Should print: "Have a NICE day"
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# # Should print: "Shhh, don't be so LOUD!"
# print(highlight_word("Automating with Python is fun", "fun"))
# # Should print: "Automating with Python is FUN"


"""
Question 3
Consider the following scenario about using Python lists: 
A professor gave his two assistants, Jaime and Drew, the task of keeping an attendance list of students in the order they arrive in the classroom. Drew was the first one to note which students arrived, and then Jaime took over. After the class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one, in the order of each student's arrival. Jaime emailed a follow-up, saying that her list is in reverse order. 
Complete the code to combine the two lists into one in the order of: the contents of Drew's list, followed by Jaime’s list in reverse order, to produce an accurate list of the students as they arrived. This function should: 
    accept two lists through the function’s parameters;
    reverse the order of “list1”; 
    combine the two lists so that “list2” comes first, followed by “list1”;
    return the new list. 
"""

# def combine_lists(list1, list2):

#   combined_list = [] # Initialize an empty list variable
#   # Reverse the order of "list1"
#   list1.reverse()
#   # Combine the two lists 
#   combined_list = list2 + list1
#   return combined_list  
  
# Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
# Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

# print(combine_lists(Jaimes_list, Drews_list))
# # Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

"""Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”."""

# def squares(start, end):
#     result = []
#     for number in range(start, end+1):
#         result.append(number**2)
#     return result # Create the required list comprehension.

# print(squares(2, 3)) # Should print [4, 9]
# print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Fill in the blanks to complete the “car_listing” function. This function accepts a “car_prices” dictionary. It should iterate through the keys (car models) and values (car prices) in that dictionary. For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". Each new string should appear on its own line."""

# def car_listing(car_prices):
#   result = ""
#   # Complete the for loop to iterate through the key and value items 
#   # in the dictionary.
#   for key, value in car_prices.items():
#     result += ("A {} costs {} dollars \n".format(key, value)) # Use a string method to format the required string. 
#   return result

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

"""Question 6
Consider the following scenario about using Python dictionaries and lists: 
Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.  
Complete the function so that it accepts a list of people, then iterates over the list and adds all of the names (elements) to the dictionary as keys with a starting value of 0. Tessa and Rick plan to update these values with the number of guests their friends will bring with them to the party. Then, print the new dictionary.
This function should:
    accept a list variable named “guest_list” through the function’s parameter;
    add the contents of the list as keys to a new, blank dictionary;
    assign each new key with the value 0;
    print the new dictionary."""

# def setup_guests(guest_list):
#     # loop over the guest list and add each guest to the dictionary with
#     # an initial value of 0
#     result = {} # Initialize a new dictionary 
#     for index in guest_list: # Iterate over the elements in the list 
#         # Add each list element to the dictionary as a key with 
#         result[index] = 0
#             # the starting value of 0
#     return result

# guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

# print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

"""Question 7
Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:
    accept a string “text” variable through the function’s parameters;
    iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);
    populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;
    return the new dictionary."""

# def count_letters(text):
#   # Initialize a new dictionary.
#   dictionary = {}
#   # Complete the for loop to iterate through each "text" character and 
#   # use a string method to ensure all letters are lowercase.
#   for letter in text:
#     # Complete the if-statement using a string method to check if the
#     # character is a letter.
#     letter = letter.lower()
#     if letter.isalpha():
#       # Complete the if-statement using a logical operator to check if 
#       # the letter is not already in the dictionary.
#       if letter not in dictionary.keys():
#            # Use a dictionary operation to add the letter as a key
#            # and set the initial count value to zero.
#         dictionary[letter] = 0
#       # Use a dictionary operation to increment the letter count value 
#       # for the existing key.
#       dictionary[letter] += 1
      
#       # Increment the letter counter. 
#   return dictionary

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# genre = "transcendental"
# print(genre[:-8])
# print(genre[-7:9])

# music_genres = ["rock", "pop", "country"]
# music_genres.append("blues")
# print(music_genres)

