def is_palindrome(input_string):
  input_string = input_string.replace(" ", "");
  input_string = input_string.lower();
  new_string = ""
  reverse_string = ""
  for letter in input_string:
    new_string += letter
    reverse_string = letter + reverse_string
  if new_string == reverse_string:
  	return True
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def convert_distance(miles):
  km = miles * 1.6 
  result = "{} miles equals {:.1f} km".format(miles, km);
  return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
