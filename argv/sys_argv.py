from sys import argv
script, first, second, third = argv
print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# argv is a list with argv[0] = to the name of the python script.
# Could hav used:
  # print("The script is called: ", argv[0])
  # print("Your first variable is: ", argv[1])
  # print("Your second variable is: ", argv[2])
  # print("Your third variable is: ", argv[3])
# to get the same result without unpacking.