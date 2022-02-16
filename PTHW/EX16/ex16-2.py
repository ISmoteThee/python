from sys import argv

filename = argv[1]

text = open(filename, 'r')

print(text.read())