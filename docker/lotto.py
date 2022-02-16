import random

def lottery():
    # returns 6 numbers between 1 and 70
    for i in range(5):
        yield random.randint(1, 70)

    # returns a 7th number between 1 and 25 
    yield random.randint(1,25)

for random_number in lottery():
       print(f"And the next number is... {random_number}!")


