name = input("Hi, what is your name? ")
print('How old are you?', end=' ')
age = int(input())
print('How tall are you in inches?', end=' ')
height = int(input())
print('How much do you weigh in lbs?', end=' ')
weight = int(input())

print(  f"Hello {name}, " +
        f"you're at least {age*52*7*24} hours old, " +
        f"{height//12}\'{height%12}\" tall " +
        f"and {round(weight*0.4536, 1)} kgs."
)
