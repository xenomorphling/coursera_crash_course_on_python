# # # # # # friends = ['Taylor', 'Alex', 'Pat', 'Eli']
# # # # # # for friend in friends:
# # # # # #     print("Hi " + friend)
# # # # # # print('Hello')


# # # # # # bill = 47.28
# # # # # # tip = bill * 0.15
# # # # # # total = bill + tip
# # # # # # share = (total/2)

# # # # # # print(tip)
# # # # # # print(total)
# # # # # # print("Each person needs to pay: " + str(total))

# # # # # # def showme(name):
# # # # # #     print("your word is " + name)

# # # # # # showme("Moe")

# # # # # # def print_monthly_expense(month, hours):
# # # # # #   print("In " + month + " we spent: " + str(hours*0.65))
# # # # # # print_monthly_expense("June", 243)
# # # # # # print_monthly_expense("July", 325)
# # # # # # print_monthly_expense("August", 298)

# # # # # # def rectangle_area(base, height):
# # # # # # 	area = (base)*(height)  # the area is base*height
# # # # # # 	print("The area is " + str(area))

# # # # # # rectangle_area(5, 6)

# # # # # # def convert_distance(miles):
# # # # # #   km = miles * 1.6  # approximately 1.6 km in 1 mile
# # # # # #   return(km)

# # # # # # print("first " + str(convert_distance(55)))
# # # # # # print("second " + str(convert_distance(55 * 2)))


# # # # # # def order_numbers(number1, number2):
# # # # # # 	if number2 > number1:
# # # # # # 		return number1, number2
# # # # # # 	else:
# # # # # # 		return number2, number1

# # # # # # var = order_numbers(100, 99)
# # # # # # print(var)

# # # # # # def calculate_storage(filesize):
# # # # # #     block_size = 4096
# # # # # #     # Use floor division to calculate how many blocks are fully occupied
# # # # # #     full_blocks = filesize // block_size
# # # # # #     print("full_blocks" + str(full_blocks))
# # # # # #     # Use the modulo operator to check whether there's any remainder
# # # # # #     partial_block = filesize % block_size
# # # # # #     print("partial_block" + str(partial_block))
# # # # # #     # Depending on whether there's a remainder or not, return the right number.
# # # # # #     if partial_block > 0:
# # # # # #       return ((full_blocks * block_size) + block_size)
# # # # # #     return (filesize)
  

# # # # # # print(calculate_storage(1))
# # # # # # print (' ')    # Should be 4096
# # # # # # print(calculate_storage(4096)) # Should be 4096
# # # # # # print (' ')
# # # # # # print(calculate_storage(4097)) # Should be 8192

# # # # # # def color_translator(color):
# # # # # # 	if color == "red":
# # # # # # 		hex_color = "#ff0000"
# # # # # # 	elif color == "green":
# # # # # # 		hex_color = "#00ff00"
# # # # # # 	elif color == "blue":
# # # # # # 		hex_color = "#0000ff"
# # # # # # 	else:
# # # # # # 		hex_color = "unknown"
# # # # # # 	return hex_color

# # # # # # print(color_translator("blue")) # Should be #0000ff
# # # # # # print(color_translator("yellow")) # Should be unknown
# # # # # # print(color_translator("red")) # Should be #ff0000
# # # # # # print(color_translator("black")) # Should be unknown
# # # # # # print(color_translator("green")) # Should be #00ff00
# # # # # # print(color_translator("")) # Should be unknown

# # # # # # def exam_grade(score):
# # # # # # 	if score > 95:
# # # # # # 		grade = "Top Score"
# # # # # # 	elif score >= 60:
# # # # # # 		grade = "Pass"
# # # # # # 	else:
# # # # # # 		grade = "Fail"
# # # # # # 	return grade

# # # # # # print(exam_grade(65)) # Should be Pass
# # # # # # print(exam_grade(55)) # Should be Fail
# # # # # # print(exam_grade(60)) # Should be Pass
# # # # # # print(exam_grade(95)) # Should be Pass
# # # # # # print(exam_grade(100)) # Should be Top Score
# # # # # # print(exam_grade(0)) # Should be Fail

# # # # # # 

# # # # # # def longest_word(word1, word2, word3):
# # # # # # 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# # # # # # 		word = word1
# # # # # # 	elif len(word2) >= len(word3) and len(word2) >= len(word1):
# # # # # # 		word = word2
# # # # # # 	else:
# # # # # # 		word = word3
# # # # # # 	return(word)

# # # # # # print(longest_word("chair", "couch", "table"))
# # # # # # print(longest_word("bed", "bath", "beyond"))
# # # # # # print(longest_word("laptop", "notebook", "desktop"))

# # # # # # def fractional_part(numerator, denominator):
# # # # # #   # Operate with numerator and denominator to 
# # # # # #   if denominator == 0:
# # # # # #     return 0
# # # # # #   else:
# # # # # #     ans = numerator / denominator
# # # # # #     return ans
# # # # # # # keep just the fractional part of the quotient


# # # # # # print(fractional_part(5, 5)) # Should be 0
# # # # # # print(fractional_part(5, 4)) # Should be 0.25
# # # # # # print(fractional_part(5, 3)) # Should be 0.66...
# # # # # # print(fractional_part(5, 2)) # Should be 0.5
# # # # # # print(fractional_part(5, 0)) # Should be 0
# # # # # # print(fractional_part(0, 5)) # Should be 0

# # # # # # def print_prime_factors(number):
# # # # # #   # Start with two, which is the first prime
# # # # # #   factor = 2
# # # # # #   # Keep going until the factor is larger than the number
# # # # # #   while factor <= number:
# # # # # #     # Check if factor is a divisor of number# # # # # #     if number % factor == 0:
# # # # # #       # If it is, print it and divide the original number
# # # # # #       print(factor)
# # # # # #       number = number / factor
# # # # # #     else:
# # # # # #       # If it's not, increment the factor by one
# # # # # #       factor += 1
# # # # # #   return "Done"

# # # # # # print_prime_factors(100) # Should print 2,2,5,5



# # # # # # def is_power_of_two(n):
# # # # # #   # Check if the number can be divided by two without a remainder
# # # # # #   while n % 2 == 0:
# # # # # #     n = n / 2
# # # # # #   # If after dividing by two the number is 1, it's a power of two
# # # # # #   if n == 1:
# # # # # #     return True
# # # # # #   return False

# # # # # # print(is_power_of_two(5))



# # # # # def is_power_of_two(n):
# # # # #   # Check if the number can be divided by two without a remainder
# # # # #   while n >= 1:
# # # # #     if n % 2 == 1:
# # # # #       n -= 1
# # # # #       while n % 2 == 0:
# # # # #         n = n / 2
# # # # #       # If after dividing by two the number is 1, it's a power of two
# # # # #         if n == 1:
# # # # #           return True
# # # # #   return False

# # # # # print(is_power_of_two(7))
# # # # # print(is_power_of_two(30))
# # # # # #print(is_power_of_two(322))


# # # # # # def sum_divisors(n):
# # # # # #   i = 1
# # # # # #   sum = 0
# # # # # #   while n > i:
# # # # # #     if n % i == 0:
# # # # # #       print(i)
# # # # # #       sum = sum + i
# # # # # #       i += 1
# # # # # #     else:
# # # # # #       i += 1
# # # # # #   return sum

# # # # # # print(sum_divisors(6)) # Should be 1+2+3=6
# # # # # # print(sum_divisors(12)) # Should be 1+2+3+4+6=
# # # # # # print(sum_divisors(100))

# # # # # # def square(n):
# # # # # #     return n*n

# # # # # # def sum_squares(x):
# # # # # #     sum = 0
# # # # # #     for n in range(x):
# # # # # #         sum += square(n)
# # # # # #         print(sum)
# # # # # #     return sum

# # # # # # print(sum_squares(10)) # Should be 285


# # # # # # def is_power_of(number, base): 
# # # # # #     if (number == 0): 
# # # # # #         return False
# # # # # #     while (number != 1): 
# # # # # #             if (number % base != 0): 
# # # # # #                 return False
# # # # # #             number = number // base
              
# # # # # #     return True

# # # # # # print(is_power_of(8,2)) # Should be True
# # # # # # print(is_power_of(64,4)) # Should be True
# # # # # # print(is_power_of(70,10)) # Should be False

# # # # # # def count_users(group):
# # # # # #   count = 0
# # # # # #   for member in get_members(group):
# # # # # #     count += 1
# # # # # #     if is_group(member):
# # # # # #       count += count_users(member)
# # # # # #   return count

# # # # # # print(count_users("sales")) # Should be 3
# # # # # # print(count_users("engineering")) # Should be 8
# # # # # # print(count_users("everyone")) # Should be 18

# # # # # # def sum_positive_numbers(n):
# # # # # #   sum = 0
# # # # # #   for i in range(1, n+1):
# # # # # #     sum = sum + sum_positive_numbers(n-1)
# # # # # #   return (sum)

# # # # # # print(sum_positive_numbers(3)) # Should be 6
# # # # # # print(sum_positive_numbers(5)) # Should be 15


# # # # # def show_letters(word):
# # # # # 	for i in range(len(word)):
# # # # # 		print(word[i])

# # # # # show_letters("Hello")
# # # # # # Should print one line per letter



# # # # # def digits(n):
# # # # #   count = 0
# # # # #   if n == 0:
# # # # #     return 1
# # # # #   while (n>=1):
# # # # #     n = (n / 10)
# # # # #     count += 1
# # # # #     # print("count " + str(count))
# # # # #     # print("n " + str(n))
# # # # #   return count

# # # # # print(digits(25))   # Should print 2
# # # # # print(digits(144))  # Should print 3
# # # # # print(digits(1000)) # Should print 4
# # # # # print(digits(0))    # Should print 1


# # # # # def multiplication_table(start, stop):
# # # # # 	for x in range(start, stop+1):
# # # # # 		for y in range(start, stop+1):
# # # # # 			print(str(x*y), end="      ")
# # # # # 		print()

# # # # # multiplication_table(1, 6)
# # # # # # Should print the multiplication table shown above


# # # # def counter(start, stop):
# # # #   x = start
# # # #   if x < stop:
# # # #     return_state = "Counting up: "
# # # #     while x <= stop:
# # # #       return_state += (str(x))
# # # #       if x != stop:
# # # #         return_state += (",")
# # # #       x+=1
# # # #     return return_state
# # # #   if x > stop:
# # # #     return_state = "Counting down: "
# # # #     while x >= stop:
# # # #       return_state += (str(x))
# # # #       if x != stop:
# # # #         return_state += (",")
# # # #       x-=1
# # # #     return return_state
# # # #   if x == stop:
# # # #     return_state = ("Counting down: " + str(x))
# # # #   return return_state



# # # # print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# # # # print(counter(20, 1)) # Should be "Counting down: 2,1"
# # # # print(counter(5, 5)) # Should be "Counting up: 5"




# # # # def loop(start, stop, step):
# # # # 	return_string = ""
# # # # 	if step == 0:
# # # # 		stop = 1
# # # # 	if step < 0:
# # # # 		step = abs(step) * -1
# # # # 	else:
# # # # 		step = abs(step)
# # # # 	for count in (start, stop):
# # # # 		return_string += str(count) + " "
# # # # 		count+=step
# # # # 	return return_string.strip()

# # # # print(loop(11,2,3)) # Should be 11 8 5
# # # # print(loop(1,5,0)) # Should be 1 2 3 4
# # # # print(loop(-1,-2,0)) # Should be -1
# # # # print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
# # # # print(loop(1,1,1)) # Should be empty


# # # for x in range(10):
# # #     for y in range(x):
# # #         print(y)



# # def votes(params):
# # 	for vote in params:
# # 	    print("Possible option:" + vote)


# # votes(['yes', 'no', 'maybe'])l



# def double_word(word):
#     return (str(word) + str(word) + str(len(word*2)))

# print(double_word("hello")) # Should return hellohello10
# print(double_word("abc"))   # Should return abcabc6
# print(double_word(""))      # Should return 0




# def initials(phrase):
#     words = phrase.split()
#     result = ""
#     for word in words:
#         result += word[0].upper()
#     return result

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS
# print(initials("asdf asdfja;g fd gjfkdldg;"))

# def differ(string):
#   for i  len(string)



# print(differ("abc"))


# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#   chars += len(animal)
# print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
#   print("{} - {}".format(index + 1, person))



# def skip_elements(elements):
#   result = tuple()
#   for index, element in enumerate(elements):
#     if index % 2 == 0:
#       print(element)
#       result += element
#   return result

#   # for index, element in enumerate(elements):
#   #   if index % 2 == 0:
#   #     result += element
#   # print(result)

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']