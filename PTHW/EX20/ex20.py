from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

current_file = open(input_file)

print("First print the entire file:\n")
print_all(current_file)

print("Now rewind like a tape.")
rewind(current_file)

print("Now print 3 lines.")
current_line = 1
while current_line<4:
    print_a_line(current_line, current_file)
    current_line+=1


