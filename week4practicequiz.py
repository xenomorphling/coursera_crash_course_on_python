def is_palindrome(input_string):
  # We'll create two strings, to compare them
  input_string = input_string.replace(" ", "");
  input_string = input_string.lower();
  new_string = ""
  reverse_string = ""
  # Traverse through each letter of the input string
  for letter in input_string:
    # Add any non-blank letters to the 
    # end of one string, and to the front
    # of the other string. 
  
    new_string += letter
    reverse_string = letter + reverse_string
  # Compare the strings
  if new_string == reverse_string:
  	return True
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True