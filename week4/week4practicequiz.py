# def is_palindrome(input_string):
#   input_string = input_string.replace(" ", "");
#   input_string = input_string.lower();
#   new_string = ""
#   reverse_string = ""
#   for letter in input_string:
#     new_string += letter
#     reverse_string = letter + reverse_string
#   if new_string == reverse_string:
#   	return True
#   return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def convert_distance(miles):
#   km = miles * 1.6 
#   result = "{} miles equals {:.1f} km".format(miles, km);
#   return result

# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# 



# def full_emails(people):
#   result = []
#   for email, name in people:
#     result.append("{} <{}>".format(name, email))
#   return result
# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))


# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#   print(len(animal))
#   chars += len(animal)
# print("Total characters: {}, Average langth: {}".format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
#   print("{} - {}".format(index + 1, person))

# def skip_elements(elements):
#   # code goes here
#   new=[]
#   for element in elements:
#     # print(element)
#     # print(elements.index(element))
#     if elements.index(element) % 2 == 0:
#       new.append(element)
#   return new

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []


# multiples = []
# for x in range(1, 11):
#   multiples.append(x*7)
# print(multiples)

# multiples = [x*7 for x in range(1, 11)]
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)

# def odd_numbers(n):
#   return [x for x in range(0, n+1) if x % 2 == 1]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

# Quiz
# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#   chars += len(animal)

# print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
#   print("{} - {}".format(index + 1, person))


# def skip_elements(elements):
#   # result = ([])
# for index, element in enumerate(elements):
#   if index % 2 == 0:
#     result += element
# print(result)

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# multiples = []
# for x in range(1,11):
#   multiples.append(x*7)
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [x for x in range(0,300) if x % 3 == 0]
# print(z)


# def odd_numbers(n):
#   return [x for x in range(0, n+1) if x % 2 == 1]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []


# def multiple(n):
#   return [x*2 for x in range(0, n+1)]

# print(multiple(3))


# file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
# for extension in file_counts:
#     print(extension) 

# for ext, amount in file_counts.items():
#     print("There are {} files with the .{} extenstion".format(amount, ext))

# print(file_counts.keys())

# print(file_counts.values())

# for value in file_counts.values():
#     print(value)


# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for animal, item in cool_beasts.items():
#     print("{} have {}".format(animal, item))

# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result

# print(count_letters("aaaaa"))
# print(count_letters("whos your daddy"))
     

# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for cloth in wardrobe.keys():
#     for color in wardrobe[cloth]:
#         print("{} {}".format(color, cloth))