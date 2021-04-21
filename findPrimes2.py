def findPrimes(bottom = 1, top = 200):
    import datetime
    start_time = datetime.datetime.now()
    primes = []
    #bottom = 420000
    #top = 421000
    #bottom = int(input("enter an integer to start at: "))
    #top = int(input("enter an integer to stop at: "))
    if bottom >= 1 and top > bottom:
        while bottom in [1,2,3]:
            #print(bottom, 'is a prime number')
            primes.append(bottom)
            bottom += 1
        if (bottom % 2 == 0):
            bottom += 1
        for testNum in range(bottom, (top + 1), 2):
            for i in  range(3, testNum, 2):
                if (testNum % i) == 0:
                    #print(testNum, 'is not a prime number')
                    #print(i, 'times', (testNum//i), 'is', testNum)
                    break
            else:
                #print(testNum, 'is a prime number')
                primes.append(testNum)
    else:
        print('Input must be a integer > 1')
    #print(primes)
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    return(primes)

if __name__ == "__main__":
    findPrimes()