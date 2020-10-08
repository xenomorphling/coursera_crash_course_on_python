filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

# newfilenames = []
# print(type(newfilenames))
# for index, filename in enumerate(filenames)
# (filenames):
#   filename = filename.replace(".hpp", ".h")
#   print(filename)
#   newfilenames = newfilenames.insert(index, filename)

# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
 
newfilename = []
print(type(newfilename))
for index, filename in enumerate(filenames):
  print(index, filename)
  filename = filename.replace(".hpp", ".h")
  print(filename)
  