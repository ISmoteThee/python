def fib(count, a=0, b=1):
    if count > 0:
        print(a)
        fib(count-1, b, a+b)

if __name__ == "__main__":
    fib(20)
