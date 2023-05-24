def count(i):
    if i <= 100:
        print(i)
        i += 1
        count(i)

if __name__=="__main__":
    count(1)