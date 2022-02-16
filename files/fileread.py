from sys import argv
# Set variables from command arguments
script, filename = argv
# open file to variable txt
txt = open(filename)
# print filename confirmation
print(f"Here's your file {filename}:")
# print contents of file
print(txt.read())
# prompt for filename again
print("Type that filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())