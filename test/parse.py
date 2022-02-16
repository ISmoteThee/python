with open('output', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line[0] == '*':
            peices = line.split()
            mode = peices[-1]
            print(peices)
            print(mode)
