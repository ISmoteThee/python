import datetime
start_time = datetime.datetime.now()
bottom = 2
top = 200
#bottom = int(input("enter an integer to start at: "))
#top = int(input("enter an integer to stop at: "))
if top > 1 and bottom > 1:
  for testNum in range(bottom, top):
    for i in  range(2, testNum):
      if (testNum % i) == 0:
        #print(testNum, 'is not a prime number')
        #print(i, 'times', (testNum//i), 'is', testNum)
        break
    else:
      print(testNum, 'is a prime number')
else:
  print('Input must be a integer > 1')
end_time = datetime.datetime.now()
print(end_time - start_time)