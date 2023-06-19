def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return(n + sum_positive_numbers(n-1))

def digital_root(n):
  result = 0
  if len(str(n)) > 1:
    for i in str(n):
      result += int(i)
      print(i)
  print(result)

print(digital_root(384))