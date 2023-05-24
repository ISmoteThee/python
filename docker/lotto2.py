import random
#mainCount = 6
#mainRange = 70
#specialRange = 30

def lotto2(mainCount = 6, mainRange = 70, specialRange = 30):
   winners = random.sample(range(1, mainRange), mainCount)
   winners.sort()
   winners.append(random.randint(1, specialRange))
   return winners

print('\nThe winning numbers are\n', lotto2(), '\n')
