try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf:
    print(fnf)